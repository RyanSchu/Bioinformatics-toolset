import gzip
import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument('input', help = 'file path of the target to be parsed')
parser.add_argument('SNPinput', help = 'file path of the associated SNP ref IDs')
parser.add_argument('output', help = 'file path of the output')
args = parser.parse_args()

#make a dictionary of all the rsIDs
d={}
with gzip.open(args.SNPinput, 'r') as SNPfile:
    for line in SNPfile:
        line = line.decode('utf-8')
        ID = line.strip('\n').split('\t')
        if(ID[-1] != '.'):
            key = ID[0] + ':' + ID[1]
            d[key] = ID[-1]

#now begin to filter your input
filtered =[]
with gzip.open(args.input, 'r') as f:
    lines = []
    #first add the header to the line and begin filtering your subsequent lines
    for line in f:
        line = line.decode('utf-8')
        if ('#CHOM' in line):
            filtered.append(line)
        elif (line[0] != '#'):
            lines.append(line)
    
    #now go line by line
    for line in lines:
        words = line.strip('\n').split('\t')
        #check your MAF and R2 scores above threshold
        MafR2 = words[7].split(';')
        if (float(MafR2[1][4:]) > .01) and (float(MafR2[2][3:]) >0.8): 
            #grab DS values
            DSScores =[]
            for i in range(8, 11):
                DSScores.append(words[i].split(':')[1])
            #switch the position for the rsID if applicable
            if words[2] in d:
                words[2] = d[words[2]]
            #now simply bind everything in the proper order and add it to our filtered list
            newwords = words[0:words.index("GT:DS:GP")] + DSScores
            filtered.append('\t'.join(newwords))
            
with gzip.open(args.output, 'w') as output_file:
    #write out
    for line in filtered:
        output_file.write((line + '\n').encode('utf-8'))
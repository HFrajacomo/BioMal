from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import argparse

parser = argparse.ArgumentParser(description='Extracts features of target sequences (GFF | FASTA)', add_help=True)
parser.add_argument('-f','--fasta', dest='fast', metavar='inputFasta', type=str, help='Genomic sequence', required=True)
parser.add_argument('-x','--start', dest='start', metavar='inputStartpos', type=int, help='Genomic sequence start position', required=True)
parser.add_argument('-y','--end', dest='end', metavar='inputEndpos', type=int, help='Genomic sequence end position', required=True)

args = parser.parse_args()

file = SeqIO.parse(args.fast, "fasta")

for record in file:
	auxList = record.seq[args.start:args.end]
	break
file.close()

#print(auxList)

for i in range(0, len(auxList)-1):
	if(auxList[i] == 'A' or auxList[i] == 'a'):
		if(auxList[i+1] == 'U' or auxList[i+1] == 'u'):
			if(auxList[i+2] == 'G' or auxList[i+2] == 'g'):
				print("Found Start Codon at " + str(i))
				break

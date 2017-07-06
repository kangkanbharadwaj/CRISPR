import argparse
import sys
import os

sys.path.append('/scratch/0/bharadwk/CRISPR/CRISPR/py_files')

from crispr import runCRTTool
from write_repeat_file import write_repeat_file
from write_CP_id import write_CP_id
from write_spacer_file import write_spacer_file
from final_draft import final_draft
from final_draft_creation import final_draft_create
from com_diff import common_difference
from crispr_motif import create_motif_crispr
from write_consensus_file import write_Consensus
from cpID_consensus import cp_id_consensus
from encoding import create_encoding

def file_choices(choices,fname):
    ext = os.path.splitext(fname)[1][1:]
    if ext not in choices:
       parser.error("file doesn't end with one of {}".format(choices))
    return fname

	
parser = argparse.ArgumentParser(prog='MASTER_CRISPR_PROG', usage='%(prog)s [options]', 
description='This program aims to generate CRISPR files with fasta as input files, subsequently generating REPEAT and SPACER array files.',	
epilog='The final mapped file is created and from there the encoded file')


parser.add_argument("--G", type=str, metavar="--GENOME", help="Run CRT, generates .out file", default="G")

parser.add_argument("fasta_file", help="Please provide the fasta file", type=lambda s:file_choices(("fa"),s), nargs='?', default="/scratch/0/bharadwk/CRISPR/CRISPR/masterCrisprStrand/fasta_file/CP000505.fa")

parser.add_argument("minNR", type=int, help="minimum number of repeats a CRISPR must contain", nargs='?', default=3)
parser.add_argument("minRL", type=int, help="minimum length of a CRISPR's repeated region",  nargs='?', default=19)
parser.add_argument("maxRL", type=int, help="maximum length of a CRISPR's repeated region", nargs='?', default= 38)
parser.add_argument("minSL", type=int, help="minimum length of a CRISPR's non-repeated region (or spacer region)", nargs='?', default=19)
parser.add_argument("maxSL", type=int, help="maximum length of a CRISPR's non-repeated region (or spacer region)",  nargs='?', default=48)
parser.add_argument("screen", type=int, help="print results to the screen, instead of a file; (range: 0-1)", nargs='?', default=0)
parser.add_argument("searchWL", type=int, help="length of search window used to discover CRISPRs; (range: 6-9)", nargs='?', default=8)	

parser.add_argument("crispr_destination", help="Please provide the crispr spacer file destination path", type=str, nargs='?', default="/scratch/0/bharadwk/CRISPR/CRISPR/masterCrisprStrand/crispr_file/repeat_spacers.out")
parser.add_argument("repeat_dest", help="Please provide the crispr repeat array file destination", type=str, nargs='?', default="/scratch/0/bharadwk/CRISPR/CRISPR/masterCrisprStrand/repeat_file/repeat.txt")
parser.add_argument("spacer_dest", help="Please provide the crispr spacer array file destination", type=str, nargs='?', default="/scratch/0/bharadwk/CRISPR/CRISPR/masterCrisprStrand/spacer_file/spacers.txt")
parser.add_argument("mapped_dest", help="Please provide the mapped file destination", type=str, nargs='?', default="/scratch/0/bharadwk/CRISPR/CRISPR/masterCrisprStrand/mapped_file/map.txt")

parser.add_argument("--A", type=str, metavar="--ARRAYS", help="Reads repeats and spacer file", default="A")
parser.add_argument("encode_dest", help="Please provide the encode file destination", type=str, nargs='?', default="/scratch/0/bharadwk/CRISPR/CRISPR/masterCrisprStrand/encode_file/encode.txt")
parser.add_argument("cp_consensus", help="Please provide the cp&consensus file destination", type=str, nargs='?', default="/scratch/0/bharadwk/CRISPR/CRISPR/masterCrisprStrand/cp_consensus_file/cp_consensus.txt")

parser.add_argument("--R", type=str, metavar="--REPEATS", help="Generate consensus repeat file", default="R")
parser.add_argument("consensus_repeat", help="Please provide the consensus_repeat file destination", type=str, nargs='?', default="/scratch/0/bharadwk/CRISPR/CRISPR/masterCrisprStrand/consensus_repeat_file/consensus_repeat.txt")

args = parser.parse_args() 
'''
if args.G=='g':
	print "genomes"
elif args.A=='a':
	print "arrays"
elif args.R=='r':
	print "repeats"
else:
	print "invalid arg"
'''
if args.G == 'g':
	
	cp_id = write_CP_id()
	repeat = write_repeat_file()
	spacer = write_spacer_file() 
	file_creation = final_draft_create()
	final_df = final_draft()
	encode_file = create_encoding()		
	crtOnTheGo = runCRTTool(args.minNR, args.minRL, args.maxRL, args.minSL, args.maxSL, args.screen, args.searchWL)
	crtOnTheGo.runCRT(args.fasta_file, args.crispr_destination)	
	cp_ID = cp_id.get_CP_Id(args.crispr_destination)				   
	repeat.write_Repeat_File(cp_ID, args.crispr_destination, args.repeat_dest)    
	spacer.write_spacer_File(cp_ID, args.crispr_destination, args.spacer_dest)
	file_creation.file_create(args.mapped_dest)
	final_df.final_draft_file(cp_ID, args.crispr_destination, args.repeat_dest, args.mapped_dest)
	encode_file.create_encoded_file(args.repeat_dest, args.encode_dest)

elif args.A == 'a':
	
	encode_file = create_encoding()
	cp_con = cp_id_consensus()
	encode_file.create_encoded_file(args.repeat_dest, args.encode_dest)		
	cp_con.write_cpID_consensus(args.repeat_dest, args.cp_consensus)

elif args.R == 'r':
	
	write_cons = write_Consensus()
	write_cons.write_consensus_repeat(args.repeat_dest, args.consensus_repeat)	

else:
	print "Please provide a valid optional argument"


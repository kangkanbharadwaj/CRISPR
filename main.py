import sys
import os
import argparse
import glob

sys.path.append('/scratch/0/bharadwk/CRISPR/CRISPR/py_files')

from crispr import runCRTTool
from write_repeat_file import write_repeat_file
from write_CP_id import write_CP_id
from write_spacer_file import write_spacer_file
from final_draft import final_draft
from final_draft_creation import final_draft_create
from com_diff import common_difference
from crispr_motif import create_motif_crispr
from write_consensus_file import write_consensus
from cpID_consensus import cp_id_consensus

def argparse_setup():

    parser = argparse.ArgumentParser(prog='CRISPR', usage='%(prog)s [options]', description='A set of parameters to run CRT tool', epilog='Followed by repeat and spacer files creation')
    
    parser.add_argument("minNR", type=int, help="minimum number of repeats a CRISPR must contain", nargs='?', default=3)
    parser.add_argument("minRL", type=int, help="minimum length of a CRISPR's repeated region",  nargs='?', default=19)
    parser.add_argument("maxRL", type=int, help="maximum length of a CRISPR's repeated region", nargs='?', default= 38)
    parser.add_argument("minSL", type=int, help="minimum length of a CRISPR's non-repeated region (or spacer region)", nargs='?', default=19)
    parser.add_argument("maxSL", type=int, help="maximum length of a CRISPR's non-repeated region (or spacer region)",  nargs='?', default=48)
    parser.add_argument("screen", type=int, help="print results to the screen, instead of a file; (range: 0-1)", nargs='?', default=0)
    parser.add_argument("searchWL", type=int, help="length of search window used to discover CRISPRs; (range: 6-9)", nargs='?', default=8)
    
    parser.add_argument("--GENOME", type=str, help="Run CRT, generates .out file")
    parser.add_argument("--ARRAYS", type=str, help="Generates repeats and spacer file")
    parser.add_argument("--REPEATS", type=str, help="Get consensus repeat and generate final draft")
  
    return parser

def main(args=None):
	
	path_name = "/scratch/genomes/bacteria_archaea_omar/Genomes/*.fa"
	files = glob.glob(path_name)
	
	file_creation = final_draft_create()
	dest_path2 = "/scratch/0/bharadwk/CRISPR/CRISPR/crisper_repeat_array_files/crisper_repeat_array.txt"
	dest_path3 = "/scratch/0/bharadwk/CRISPR/CRISPR/crisper_spacer_array_files/crisper_spacer_array.txt"
	dest_path5 = "/scratch/0/bharadwk/CRISPR/CRISPR/final_draft.txt"	
		
	crtOnTheGo = runCRTTool(args.minNR, args.minRL, args.maxRL, args.minSL, args.maxSL, args.screen, args.searchWL)
	file_creation.file_create(dest_path5)	
	cp_id = write_CP_id()
	repeat = write_repeat_file()
	spacer = write_spacer_file() 
	final_df = final_draft()	
	c_d_obj = common_difference()			
		
	for name in files:
		tmp_name = name.split('/')[5]	
		dest_path4 = "/scratch/0/bharadwk/CRISPR/CRISPR/fasta_files/CRISPRs_Repeats_Spacers_%s.out" %(tmp_name)	 		
		crtOnTheGo.runCRT(name, dest_path4)
		path1 = "/scratch/0/bharadwk/CRISPR/CRISPR/fasta_files/CRISPRs_Repeats_Spacers_%s.out" %(tmp_name)			
		
		cp_ID = cp_id.get_CP_Id(path1)				   
		repeat.write_Repeat_File(cp_ID, path1, dest_path2)    
		spacer.write_spacer_File(cp_ID, path1, dest_path3)	
		final_df.final_draft_file(cp_ID, path1, dest_path2, dest_path5) 
	
	c_d_obj.find_comm_diff()
	motif_obj = create_motif_crispr()
	cp_con = cp_id_consensus()				
	motif_obj.create_fasta_file()
	motif_obj.get_repeat_spacer_file()
	motif_obj.create_encoded_file()
	#cp_con.write_cpID_consensus()		
	#write_cons = write_consensus()
	#write_cons.write_consensus_repeat()

			
def main_script():	
    
    parser = argparse_setup()
    args = parser.parse_args()   
    main(args)
    
if __name__ == '__main__':
    main_script()

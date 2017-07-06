class write_CP_id(object):
		
	def get_CP_Id(self, path1=""):
		
		cp_ID = 0
		#path = '/scratch/0/bharadwk/CRISPR/CRISPR/fasta_files/CRISPRs_Repeats_Spacers_'+tmp_name+".out"
		crispr_file = open(path1, 'r')				
		num_of_crispers = 0
		
		for line in crispr_file:
			print line
			if len(line) <= 20:
				cp_ID = line.split()[1]
			elif len(line) > 20 and len(line) < 100:
				cp_ID = line.split()[1]
			elif len(line) < 108:				
				cp_ID = line.split('|')[3]				
			else:
				cp_ID = line.split(' ')[2]
			break
		
		crispr_file.close()
		return cp_ID
		
















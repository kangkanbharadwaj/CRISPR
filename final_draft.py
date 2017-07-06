from consensus_repeat import consensus_repeat

class final_draft(object):	

	def final_draft_file(self, cp_ID=0, path1="", dest_path2="", dest_path=""):	

		#tmp_name1 = "/scratch/0/bharadwk/CRISPR/CRISPR/fasta_files/CRISPRs_Repeats_Spacers_"+tmp_name+".out"
		crispr_file = open(path1, 'r')
		#tmp_name2 = "/scratch/0/bharadwk/CRISPR/CRISPR/crisper_repeat_array_files/crisper_repeat_array.txt"
		
		fo1 = open(dest_path2, 'r')
		fo2 = open(dest_path, 'a')		
		
		res = []
		result = []		
		no_of_crispers = 0
		
		con_rep_seq = consensus_repeat()
		consensus = con_rep_seq.get_Consensus_Repeat(path1)
		
		i = 0
		
		for line in fo1:
			res.append(line.split())
		
		for line in crispr_file:
			result.append(line.split())

		for pos, line in enumerate(result):
			start_no = 0
			end_no = 0
			rep_avg_len = 0
			spc_avg_len = 0			
			
			for word in line:								
					
				if 'CRISPR' in word:
					tmp_ind = 0
					no_of_crispers = no_of_crispers+1
					start_no = result[pos][3]
					end_no = result[pos][5]											
					fo2.write(cp_ID+'_'+'CRISPR'+'_'+'{}'.format(no_of_crispers))
					fo2.write('{:>39}'.format(consensus[i]))
					'''
					for line_x in res:
						
						if tmp_ind == 1:
							break							
						for word_x in line_x:
							seq = consensus[i]
							if seq in word_x:
								fo2.write('{:>22}'.format('F'))
								tmp_ind = tmp_ind+1
								break
							if seq[::-1] in word_x:
								fo2.write('{:>22}'.format('R'))
								tmp_ind = tmp_ind+1
								break							
					'''							
					fo2.write('{:>31}'.format(start_no)+'{:>16}'.format(end_no))
					i = i+1									
			
				if 'Repeats' in word:
					rep_avg_len = result[pos][4]
					spc_avg_len = result[pos][7]
					fo2.write('{:>15}'.format(rep_avg_len)+'{:>25}'.format(spc_avg_len))	
					fo2.write('\n')
				break			
			
		crispr_file.close()
		fo1.close()
		fo2.close()

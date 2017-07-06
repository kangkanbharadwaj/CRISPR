class common_difference(object):

	def find_comm_diff(self):
		
		fo1 = open("/scratch/0/bharadwk/CRISPR/CRISPR/final_draft.txt", 'r')
		fo2 = open("/scratch/0/bharadwk/CRISPR/CRISPR/4719Repeats_24Families_18Motifs_Orignal_new_IDs_Fullnames.tab", 'r')
		fo3 = open("/scratch/0/bharadwk/CRISPR/CRISPR/common_attributes.txt", 'a')
		fo4 = open("/scratch/0/bharadwk/CRISPR/CRISPR/unique_att_final.txt", 'a')
		fo5 = open("/scratch/0/bharadwk/CRISPR/CRISPR/unique_att_Motif.txt", 'a')

		fo3.write('{a:^10}{b:^25}{c:^5}{d:^15}{e:^25}'.format(a='CP_CRISPR', b='Strand', c='Start', d='End', e='Repeat Average length'))
		fo3.write('\n\n')
		fo4.write('{a:^10}{b:^25}{c:^5}{d:^15}{e:^25}'.format(a='CP_CRISPR', b='Strand', c='Start', d='End', e='Repeat Average length'))
		fo4.write('\n\n')
		fo5.write('{a:^10}{b:^25}{c:^5}{d:^15}{e:^25}'.format(a='CP_CRISPR', b='Strand', c='Start', d='End', e='Repeat Average length'))
		fo5.write('\n\n')

		result1=[]
		result2=[]

		for line in fo1:
			result1.append(line.split())

		for line in fo2:
			result2.append(line.split())

		l_o_list1 = len(result1)
		l_o_list2 = len(result2)
				
		for pos1, line1 in enumerate(result1):
			
			pos1 = pos1+2
			if pos1 == l_o_list1:
				break
			num1 = 0		
			cr_name = result1[pos1][0]	
			cr_name = cr_name.split('.')[0]
			strand = result1[pos1][2]
			start = result1[pos1][3]	
			stop = result1[pos1][4]
			rep_avg_len = result1[pos1][5]
			
			for pos2, line2 in enumerate(result2):		
				
				pos2 = pos2+1		
				if pos2 == l_o_list2:
					break
				tmp_list = []
				cr_name_x = ''
				strand_x = ''
				start_x = 0
				stop_x = 0
				rep_avg_len_x = 0		
				tmp_line = result2[pos2][4]		
				tmp_line = tmp_line.split('_')
				
				if tmp_line[0] == 'NC':					
					tmp_list.append(tmp_line[0])
					tmp_list.append(tmp_line[1])		
					tmp_list = '_'.join(tmp_list)
					tmp_line.pop(0)
					tmp_line.pop(0)
					tmp_line.insert(0, tmp_list)
					strand_x = result2[pos2][5]
					
					if strand_x == 'plus':
						strand_x = 'F'
					elif strand_x == 'minus':
						strand_x = 'R'
					
					start_x = tmp_line[2]
					stop_x = tmp_line[3]		
					rep_avg_len_x = tmp_line[5]
					cr_name_x = tmp_line[0]			
				
				else:
					cr_name_x = tmp_line[0]			
					strand_x = result2[pos2][5]
					
					if strand_x == 'plus':
						strand_x = 'F'
					elif strand_x == 'minus':
						strand_x = 'R'
					
					start_x = tmp_line[2]
					stop_x = tmp_line[3]
					rep_avg_len_x = tmp_line[5]
				
				if cr_name == cr_name_x and strand == strand_x and rep_avg_len == rep_avg_len_x:
					if abs(int(start)-int(start_x)) <=50 and abs(int(stop)-int(stop_x)) <= 50:
						num1 = num1+1
						fo3.write(cr_name_x+'{:>15}'.format(strand_x)+'{:>15}'.format(start_x)+'{:>15}'.format(stop_x)+'{:>15}'.format(rep_avg_len_x))
						fo3.write('\n')
						break		
				
			if num1 == 	0:
				fo4.write(cr_name+'{:>15}'.format(strand)+'{:>15}'.format(start)+'{:>15}'.format(stop)+'{:>15}'.format(rep_avg_len))
				fo4.write('\n')


		for pos2, line2 in enumerate(result2):
			num1 = 0
			pos2 = pos2+1
			if pos2 == l_o_list2:
					break
			tmp_list = []
			cr_name_x = ''
			strand_x = ''
			start_x = 0
			stop_x = 0
			rep_avg_len_x = 0		
			tmp_line = result2[pos2][4]		
			tmp_line = tmp_line.split('_')
				
			if tmp_line[0] == 'NC':					
				tmp_list.append(tmp_line[0])
				tmp_list.append(tmp_line[1])		
				tmp_list = '_'.join(tmp_list)
				tmp_line.pop(0)
				tmp_line.pop(0)
				tmp_line.insert(0, tmp_list)
				strand_x = result2[pos2][5]
					
				if strand_x == 'plus':
					strand_x = 'F'
				elif strand_x == 'minus':
					strand_x = 'R'
				
				start_x = tmp_line[2]
				stop_x = tmp_line[3]		
				rep_avg_len_x = tmp_line[5]
				cr_name_x = tmp_line[0]			
				
			else:
				cr_name_x = tmp_line[0]			
				strand_x = result2[pos2][5]
				
				if strand_x == 'plus':
					strand_x = 'F'
				elif strand_x == 'minus':
					strand_x = 'R'
				
				start_x = tmp_line[2]
				stop_x = tmp_line[3]
				rep_avg_len_x = tmp_line[5]
			
			for pos1, line1 in enumerate(result1):		
				pos1 = pos1+2
				if pos1 == l_o_list1:
					break
						
				cr_name = result1[pos1][0]	
				cr_name = cr_name.split('.')[0]
				strand = result1[pos1][2]
				start = result1[pos1][3]	
				stop = result1[pos1][4]
				rep_avg_len = result1[pos1][5]
					
				
				
				if cr_name_x == cr_name and strand_x == strand and rep_avg_len_x == rep_avg_len:
					if abs(int(start_x)-int(start)) <=50 and abs(int(stop_x)-int(stop)) <= 50:
						num1 = num1+1				
						break		
				
			if num1 == 	0:
				fo5.write(cr_name_x+'{:>15}'.format(strand_x)+'{:>15}'.format(start_x)+'{:>15}'.format(stop_x)+'{:>15}'.format(rep_avg_len_x))
				fo5.write('\n')
				
		fo1.close()
		fo2.close()
		fo3.close()
		fo4.close()
		fo5.close()

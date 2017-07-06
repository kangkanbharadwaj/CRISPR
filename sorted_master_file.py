class sorted_master(object):

	def sort_master_file(self):

		fo1 = open('/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/tmp_masterfile.txt', 'r')
		fo2 = open('/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/masterfile.txt', 'a')
		fo2.write('{a:^10}{b:^30}{c:^0}{d:^10}{e:^20}'.format(a='CP_CRISPR', b='Strand', c='Start', d='End', e='Repeat_Average_length'))
		fo2.write('\n\n')


		master_list = fo1.read()
		master_list = master_list.split("\n")[2:-1]

		tmp_list3 = []
		len_of_list = len(master_list)


		for pos,line in enumerate(master_list):
			k = 0
			p = 0
			tmp_count = 0
			tmp_var1 = ''
			tmp_list2 = []
			tmp_var1 = line.split()[0]
			for k in range(pos,len_of_list):		
				tmp_list1 = []
				tmp_var2 = ''
				if tmp_var1 == master_list[k].split()[0]:
					p = p+1
					tmp_var2 = master_list[k]	
					tmp_list1 = tmp_var2.split()
					tmp_list1[0] = tmp_var1+'-CRISPR%d' %(p)
					tmp_list2.append(tmp_list1)			
					
			for xline in tmp_list3:				
				for items in xline:
					for xitems in items:																						
						if tmp_var1 in xitems:
							tmp_count = tmp_count+1
			if tmp_count == 0:
				tmp_list3.append(tmp_list2)	


		for line in tmp_list3:
			tmp_var3 = ''
			for items in line:
				tmp_var3 = items
				tmp_var3 = '		'.join(tmp_var3)
				fo2.write(tmp_var3)
				fo2.write('\n')

		fo1.close()		
		fo2.close()	

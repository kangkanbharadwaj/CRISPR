from itertools import islice

class valid_crispr(object):
	
	def found_not_found(self):
		fo1 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/original_files/NewDataset_sorted.tab", 'r')
		fo2 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_repeat/bio_repeat_array.txt", "r")
		fo3 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/crispr_genome/crispr_found.txt", "a")
		fo4 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/empty_genome/no_crispr_found.txt", "a")

		fo3.write('{a:^10}{b:^30}{c:^0}{d:^20}{e:^40}'.format(a='CP_CRISPR', b='Strand', c='Start', d='End', e='Repeat_Average_length'))
		fo3.write('\n\n')
		fo4.write('{a:^10}{b:^30}{c:^0}{d:^20}{e:^40}'.format(a='CP_CRISPR', b='Strand', c='Start', d='End', e='Repeat_Average_length'))
		fo4.write('\n\n')

		list1 = []
		list2 = []
		list_of_crispr = []

		for line in islice(fo1, 2, None):
			list1.append(line.split())

		for line in fo2:
			list2.append(line.split())


		for i in range(0, len(list2), 2):

			cp_id = list2[i][0]		
			tmp_var = cp_id.split('>')
			print tmp_var[1]
			if "." in tmp_var:
				var1, var2 = tmp_var[1].split('.')
				var2 = var2.split('-')
				var2 = var2[1]
				cp_id = var1+'-'+var2
			else:
				cp_id = tmp_var[1]
				
			total_len = 0
			avg_len = 0
			count = 0	
			
			strand = ''
			start = ''
			end = ''
			repeat_avg_len = ''
			
			seq_list = list2[i+1]
			for items in seq_list:
				length = len(items)		
				total_len = total_len + length
			avg_len = total_len/len(seq_list)
			
			for items in list1:		
				if cp_id == items[0] and avg_len == len(items[4]):			
					
					count = count + 1
					list_of_crispr.append(cp_id)
					fo3.write('{:>10}'.format(items[0]))
					fo3.write('{:>10}'.format(items[1]))
					fo3.write('{:>30}'.format(items[2]))
					fo3.write('{:>10}'.format(items[3]))
					fo3.write('{:>40}'.format(items[4]))
					fo3.write("\n")			
					break


		for x_items in list1:
			if x_items[0] not in list_of_crispr:
				fo4.write('{:>10}'.format(x_items[0]))
				fo4.write('{:>10}'.format(x_items[1]))
				fo4.write('{:>30}'.format(x_items[2]))
				fo4.write('{:>10}'.format(x_items[3]))
				fo4.write('{:>40}'.format(x_items[4]))
				fo4.write("\n")


		fo1.close()
		fo2.close()
		fo3.close()
		fo4.close()

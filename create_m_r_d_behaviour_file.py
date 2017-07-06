import re

class m_r_d_variations(object):
	
	def create_m_r_d_files(self, folder_name=None, file_name=None):

		#fo1 = open("/scratch/0/bharadwk/CRISPR/CRISPR/%s/%s" %(folder_name, file_name), "r")		
		fo1 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/%s/%s" %(folder_name, file_name), "r")
		
		name_list = []
		filename = file_name
		name_list = filename.split('_')
		str1 = name_list[2]
		str2 = name_list[3]
		str3 = name_list[4].split('.')[0]
		str1 = ''.join(re.findall('\d+', str1 ))
		str2 = ''.join(re.findall('\d+', str2 ))
		str3 = ''.join(re.findall('\d+', str3 ))			

		file_list = []
		file_list = fo1.readlines()
		data_coll_list = []

		final_list = []
		tmp_list1 = []
		tmp_list2 = []
		tmp_list3 = []
		tmp_list4 = []
		tmp_list5 = []
		
		match_string = 'Performance on data set in cross validation'

		for pos, line in enumerate(file_list):
			if match_string in line:
				x_pos = pos + 1		
				for i in range(x_pos, x_pos+9):
					data_coll_list.append(file_list[i])
				
		for pos, line in enumerate(data_coll_list):	
			if pos < 3:
				tmp_list1.append(line.split(':')[1])		
			if pos > 3:
				tmp_list2.append(line.split(' '))
				
		tmp_list5.append(tmp_list1[0])
		
		for pos, items in enumerate(tmp_list1):	
			x_list = []	
			pos = pos + 1
			if pos < len(tmp_list1):
				x_list = tmp_list1[pos].split(' ')
				tmp_str1 = x_list[1]
				tmp_str2 = "{:.2f}".format(float(x_list[3]))
				tmp_str3=tmp_str1+'/'+str(tmp_str2)+'%'
				tmp_list5.append(tmp_str3)
			
		for x_lists in tmp_list2:
			del x_lists[:4]

		for x_lists in tmp_list2:
			for items in x_lists:
				tmp_str = ''.join(str(items))
				tmp_list3.append(tmp_str)

		for items in tmp_list3:
			tmp_list4.append(items.split(':')[1])

		final_list = tmp_list5 + tmp_list4
		final_list = map(lambda s: s.strip(), final_list)

		fo2 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/m_r_d_specifications/%s.txt" %(folder_name), "a")
		fo2.write('\n')
		final_list.insert(0,str1)
		final_list.insert(1,str2)
		final_list.insert(2,str3)

		for n in range(0, len(final_list)):
			if n < 3: 
				fo2.write(str(final_list[n]))
				fo2.write('/')			
			if n == 3:
				fo2.write('{:>7}'.format(final_list[n]))
			if n == 4:
				fo2.write('{:>13}'.format(final_list[n]))
			if n == 5:
				fo2.write('{:>13}'.format(final_list[n]))
			if n > 5 and n < 10:
				fo2.write('{:>8}'.format(final_list[n]))
			if n >= 10 and n < 18:
				fo2.write('{:>15}'.format(final_list[n]))
			if n == 18:
				fo2.write('{:>10}'.format(final_list[n]))				

		fo2.close()
		fo1.close()

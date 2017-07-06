f = open('/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/original_files/NewDataset.tab', 'r')
g = open('/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/original_files/NewDataset_updated.tab', 'a')
g.write('{a:^10}{b:^20}{c:^0}{d:^20}{e:^40}'.format(a='Accession Number', b='Strand', c='Start', d='End', e='Consensus Repeat'))
g.write('\n\n')

f.readline()
for lines in f:
    if lines.strip():
		lines = lines.split()						
		del lines[4]
		del lines[4]
		g.write('{:>0}'.format(lines[0]))
		g.write('{:>15}'.format(lines[3]))
		g.write('{:>20}'.format(lines[1]))
		g.write('{:>10}'.format(lines[2]))		
		g.write('{:>50}'.format(lines[4]))
		g.write('\n')
				

f.close()
g.close()

fo1 = open('/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/original_files/NewDataset_updated.tab', 'r')
fo2 = open('/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/original_files/NewDataset_sorted.tab', 'a')
fo2.write('{a:^10}{b:^20}{c:^0}{d:^20}{e:^40}'.format(a='Accession Number', b='Crispr ID', c='Start', d='End', e='Consensus Repeat'))
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

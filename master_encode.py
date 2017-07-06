import glob
import itertools
from crispr_motif import create_motif_crispr
from rev_complementary import get_reverse_comp
from sorted_master_file import sorted_master
from valid_crispr_collection import valid_crispr

fo = open("/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/tmp_masterfile.txt", "w")
fo.write('{a:^10}{b:^30}{c:^0}{d:^10}{e:^20}'.format(a='CP_CRISPR', b='Strand', c='Start', d='End', e='Repeat_Average_length'))
fo.write('\n\n')
fo.close()

path_name = "/scratch/0/bharadwk/CRISPR/CRISPR/our_dataset/*.txt"
filenames = glob.glob(path_name)

with open('/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/tmp_masterfile.txt', 'a') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in itertools.islice(infile, 2, None):												
                outfile.write(line)

outfile.close()
sort_obj = sorted_master()
sort_obj.sort_master_file()

motif_obj = create_motif_crispr()
rev = get_reverse_comp()
found_not_found = valid_crispr()
motif_obj.create_fasta_file()
motif_obj.get_repeat_spacer_file()

fo1 = open("/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/master_repeat/master_repeat_array.txt", "r")
fo2 = open("/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/masterfile.txt", "r")
fo3 = open("/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/target_true_file/target_true.txt", "a")
fo4 = open("/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/target_false_file/target_false.txt", "a")

path1 = "/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/master_encoded_files/enclode_true.txt"
path2 = "/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/master_encoded_files/encode_false.txt"

result1 = []
result2 = []

for line in fo1:
	result1.append(line.split())

for line in itertools.islice(fo2, 2, None):
	result2.append(line.split())

for i in range(0,len(result1),2):
	
	sequence = ''
	list3 = []
	avg_len_of_repeat = 0
	total_len = 0
	avg_len = 0
	tmp_list = []
	var = ''
	var2 = ''
	var = result1[i][0].split('>')[1]
	var = var.split('.')
	var2 = var[1]
	var2 = var2.split('-')[1]
	var = var[0]+'-'+var2	
	tmp_list = result1[i+1]
	
	for items in tmp_list:
		length = len(items)		
		total_len = total_len + length
	avg_len = total_len/len(tmp_list)		
	
	for j in range(0,len(result2)):	
		avg_len_of_repeat = 0	
		tmp_id = result2[j][0]
		tmp_strand = result2[j][1]
		avg_len_of_repeat = int(result2[j][4])	
		list1 = []
		list2 = []
		
		if var == tmp_id and tmp_strand == 'F' and avg_len == avg_len_of_repeat:			
			motif_obj.create_encoded_file(path1, result1[i+1])
			fo3.write(str(1))
			fo3.write('\n')
			break
			
		elif var == tmp_id and tmp_strand == 'R' and avg_len == avg_len_of_repeat:
			list1 = result1[i+1]			
			list2 = list1[::-1]				
			for j in range(0,len(list2)):
				rev.reverse_complementary(list2[j])
				fo5 = open("/scratch/0/bharadwk/CRISPR/CRISPR/master_dataset/reverse_complementary/INPUT_R.SEQUENCE", "r")
				sequence = fo5.readline()				
				list3.append(sequence)
				fo5.close()									
			#motif_obj.create_encoded_file(path2, result1[i+1])
			motif_obj.create_encoded_file(path2, list3)
			fo4.write(str(-1))
			fo4.write('\n')
		
			break
	
found_not_found.found_not_found()
		
fo1.close()
fo2.close()
fo3.close()
fo4.close()


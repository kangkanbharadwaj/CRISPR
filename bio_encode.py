import glob
import itertools
from bio_crispr_motif2 import create_bio_crispr
from rev_complementary import get_reverse_comp
#from bio_sort_datafile2 import sorted_bio
from valid_crispr_collection import valid_crispr
from for_rev import for_rev

#bio_obj = sorted_bio()
#filename = bio_obj.sort_bio_file(data_file = 'ar_acc_id_positions_repeat')
#bio_obj.replace_crispr_to_strand(filename)

motif_obj = create_bio_crispr()
rev = get_reverse_comp()
found_not_found = valid_crispr()
f_r_obj = for_rev()
#motif_obj.create_fasta_file()
#motif_obj.get_repeat_spacer_file()

fo1 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_repeat/bio_repeat_array.txt", "r")
fo2 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/original_files/NewDataset_sorted.tab", "r")
fo3 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/target_true_file/target_true.txt", "a")
fo4 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/target_false_file/target_false.txt", "a")

fo5 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/for_rev/for_rev.txt", "w")
fo5.write('{a:^10}{b:^80}'.format(a='Original String', b='Reverse Complementary'))
fo5.write("\n\n")
fo5.close()

path1 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_encoded_files/enclode_true.txt"
path2 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_encoded_files/encode_false.txt"

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
	if "." in var:
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
		avg_len_of_repeat = len(result2[j][4])	
		list1 = []
		list2 = []
		
		#if var == tmp_id and tmp_strand == 'F' and avg_len == avg_len_of_repeat:			
		#	motif_obj.create_encoded_file(path1, result1[i+1])
		#	fo3.write(str(1))
		#	fo3.write('\n')
		#	break
			
		if var == tmp_id and avg_len == avg_len_of_repeat:
			
			motif_obj.create_encoded_file(path1, result1[i+1])
			fo3.write(str(1))
			fo3.write('\n')
			
			list1 = result1[i+1]			
			list2 = list1[::-1]				
			for j in range(0,len(list2)):
				rev.reverse_complementary(list2[j])
				fo5 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/reverse_complementary/INPUT_R.SEQUENCE", "r")
				sequence = fo5.readline()				
				list3.append(sequence)
				fo5.close()									
			#motif_obj.create_encoded_file(path2, result1[i+1])
			motif_obj.create_encoded_file(path2, list3)
			fo4.write(str(-1))
			fo4.write('\n')
		
			break
	
#found_not_found.found_not_found()
#f_r_obj.encode_to_org()
		
fo1.close()
fo2.close()
fo3.close()
fo4.close()
fo5.close()

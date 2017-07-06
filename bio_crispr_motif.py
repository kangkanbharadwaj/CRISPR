import os
import subprocess as sp
import glob
import re
from collections import Counter
from download_file import download_fasta_file

from write_repeat_file import write_repeat_file
from write_CP_id import write_CP_id
from write_spacer_file import write_spacer_file
from consensus_repeat import consensus_repeat

class create_bio_crispr(object):


    def create_fasta_file(self):

		fo1 = open('/scratch/0/bharadwk/CRISPR/CRISPR/biological_data/original_files/ar_acc_id_positions_repeat_sorted.tab', 'r')
		fo2 = open('/scratch/0/bharadwk/CRISPR/CRISPR/biological_data/original_files/ar.fna', 'r')
		
		list1 = []
		list2 = []

		list1 = fo1.read()
		list1 = list1.split("\n")[2:-1]
		dwn_obj = download_fasta_file()

		for lines in fo2:
			list2.append(lines.split())

		for pos,line in enumerate(list1):
			crispr_str = ''
			ycount = 0
			tmp_name = ''
			tmp_str = line.split('\t')[0]			
			tmp_name, count = tmp_str.split('-')
			print tmp_str
			print count
			x_tmp_name = '>'+tmp_name
			
			start = line.split()[2]
			end = line.split()[3]	
			
			start = int(start)
			end = int(end)
			
			if start > end:
				tmp = start
				start = end
				end = tmp
				start = start - 50
				end = end + 50
			else:
				start = start + 50
				end = end - 50
			
			start = str(start)
			end = str(end)
			list3 = []	
			list4 = []	
			
			fo3 = open('/scratch/0/bharadwk/CRISPR/CRISPR/biological_data/fasta_files/%s__%s.fa' %(tmp_name, count), 'a')	
			
			for pos, xline in enumerate(list2):
				for xitems in xline:			
					if xitems.startswith('>') and x_tmp_name == xitems:
						ycount = ycount + 1
						crispr_str = xitems
						pos = pos+1					
						for ylines in list2[pos::]:
							for yitems in ylines:							
								if yitems.startswith('>'):
									break
								list3.append(yitems)
						break
						
			if ycount == 0:
				dwn_obj.download_file(tmp_name, count)
			
			if ycount > 0:
				xlist3 = "".join(list3)
				for i in range(int(start), int(end)):
					list4.append(xlist3[i])

				xlist4 = "".join(list4)
				fo3.write(crispr_str)
				fo3.write('\n')
				fo3.write(xlist4)	
				fo3.close()

		fo1.close()
		fo2.close()

    def get_repeat_spacer_file(self):

            import subprocess as sp
            import re
            import glob
            from write_repeat_file import write_repeat_file
            from write_CP_id import write_CP_id
            from write_spacer_file import write_spacer_file

            cp_id = write_CP_id()
            repeat = write_repeat_file()
            spacer = write_spacer_file()

            path3 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data/fasta_files/*.fa"
            dest_path1 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data/bio_repeat/bio_repeat_array.txt"
            dest_path2 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data/bio_spacer/bio_spacer_array.txt"

            files = []
            files = glob.glob(path3)

            for name in files:
				tmp_name = name.split('/')[8]                                    
				tmp_name = tmp_name.split('.')[0]
				print tmp_name
				fo = open(name, "r")
				num_lines = sum(1 for line in fo)

				if num_lines > 1:
					cmd = "java -cp /scratch/0/bharadwk/CRISPR/bin/CRT1.2-CLI.jar crt %s /scratch/0/bharadwk/CRISPR/CRISPR/biological_data/bio_crispr/CRISPRs_Repeats_Spacers_%s.out" %(name,tmp_name)
					sp.call(cmd, shell=True)
					path4 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data/bio_crispr/CRISPRs_Repeats_Spacers_%s.out" %(tmp_name)
					tmp1 = path4.split('.')[0]
					tmp2 = tmp1.split('__')[1]
					cp_ID = cp_id.get_CP_Id(path4)
					repeat.write_Repeat_File(cp_ID, path4, dest_path1, tmp2)
					spacer.write_spacer_File(cp_ID, path4, dest_path2, tmp2)
				fo.close()


    def create_encoded_file(self, path="", tmp_list=[]):
            
		fo2 = open(path, "a")
		result = []  		
		tmp_list1=[]
		tmp_list2=[]
		string1 = ""
		string2 = ""
		string3 = ""
		consensus = []
		consensus_str = ''
		DominantRepeat = {}	
		con_rep_seq = consensus_repeat()
		
		for seq in tmp_list:
			eachRepeat = seq
			DominantRepeat[eachRepeat] = DominantRepeat.get(eachRepeat, 0) + 1
		consensus_seq = max(DominantRepeat, key = DominantRepeat.get)
		consensus.append(consensus_seq)
		
		consensus_str = consensus[0]		
		tmp_list1 =  tmp_list
		tmp_list2 = tmp_list1[-3:]				

		if len(tmp_list2)>=3:
			string1 = tmp_list2[0]
			string2 = tmp_list2[1]
			string3 = tmp_list2[2]

			length1 = len(string1)
			length2 = len(string2)
			length3 = len(string3)

			len_of_str = max(length1, length2, length3)
			if len_of_str>=17:
				count1 = 1
				count2 = 1
				position_no_1 = 0
				position_no_2 = -5
				position_no_3 = 0
				first_threshold = 8
				second_threshold = len_of_str-8

				for i in range(0, 8):
					tmp_list3=[]
					block_no=1

					if i>3:
						block_no=2
						count1=count1+1

					if count1==2:
						position_no_1=0 

					if consensus_str[i] == string1[i] and consensus_str[i] == string2[i] and consensus_str[i] == string3[i]:
						position_no_1=position_no_1+1
						fo2.write(consensus_str[i])
						fo2.write(str(block_no))
						fo2.write("N")
						fo2.write(str(position_no_1))                         	                 

					else:
						#tmp_list3.append(string1[i])
						#tmp_list3.append(string2[i])
						#tmp_list3.append(string3[i])
						position_no_1=position_no_1+1

						#common_char= [ite for ite, it in Counter(tmp_list3).most_common(1)]

						fo2.write(consensus_str[i])
						fo2.write(str(block_no))
						fo2.write("Y")
						fo2.write(str(position_no_1))

				for i in range(first_threshold, second_threshold):

					position_no_3 = position_no_3 + 1
					fo2.write(consensus_str[i])
					fo2.write('3')
					fo2.write("X")
					fo2.write(str(position_no_3))


				for i in range(len_of_str-8, len_of_str):
					tmp_list3=[]
					block_no=4

					if i>=(len_of_str-4):
							block_no=5
							count2=count2+1

					if count2==2:
							position_no_2=-5

					if consensus_str[i] == string1[i] and consensus_str[i] == string2[i] and consensus_str[i] == string3[i]:
						position_no_2=position_no_2+1
						fo2.write(consensus_str[i])
						fo2.write(str(block_no))
						fo2.write("N")
						fo2.write(str(position_no_2))
					else:
						#tmp_list3.append(string1[i])
						#tmp_list3.append(string2[i])
						#tmp_list3.append(string3[i])
						position_no_2=position_no_2+1

						#common_char= [ite for ite, it in Counter(tmp_list3).most_common(1)]

						fo2.write(consensus_str[i])
						fo2.write(str(block_no))
						fo2.write("Y")
						fo2.write(str(position_no_2))

				fo2.write("\n")

		fo2.close()
            

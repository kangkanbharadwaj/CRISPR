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

        fo =  open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/original_files/NewDataset_sorted.tab", "r")
        result = []
        tmp_item = ""
        start = 0
        end = 0
        xcount = 0

        list_of_files = []	

        result=fo.read()
        result= result.split("\n")[2:-1]
        dwn_obj = download_fasta_file()
        
        for pos, line in enumerate(result):			
			tmp_name = ""            
			tmp_str = line.split('\t')[0]			
			tmp_name, count = tmp_str.split('-')         
			start = line.split()[2]
			end = line.split()[3]
			cmd = "find /scratch/genomes/bacteria_archaea_omar/Genomes/ -type f -name '%s*'" %(tmp_name)
			proc = sp.Popen(cmd, stdout=sp.PIPE, shell=True)
			path1 = proc.stdout.read().strip()
			
			if path1 != "":
				fo1 = open(path1, 'r')				

				crispr_str = fo1.readline().strip()

				result1=[]
				result2=[]
				result3=""
				pos = 0

				for pos,line in enumerate(fo1):
					 result1.append(line.split())

				for line in result1:
						for item in  line:
								result2.append(item)

				start = int(start)
				end = int(end)
				start = start - 100
				end = end + 100
				result3 = "".join(result2)
				result3 = result3[start:end]

				path2 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/fasta_files/%s__%s.fa" %(tmp_name, count)
				fo2 = open(path2, "a")

				fo2.write(crispr_str)
				fo2.write("\n")					
				fo2.write(result3)
				fo2.close()
				fo1.close()
			
			else:
				dwn_obj.download_file(tmp_name, count)

        fo.close()

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

            path3 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/fasta_files/*.fa"
            dest_path1 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_repeat/bio_repeat_array.txt"
            dest_path2 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_spacer/bio_spacer_array.txt"

            files = []
            files = glob.glob(path3)

            for name in files:
				tmp_name = name.split('/')[8]                                    
				tmp_name = tmp_name.split('.')[0]
				print tmp_name
				fo = open(name, "r")
				num_lines = sum(1 for line in fo)

				if num_lines > 1:
					cmd = "java -cp /scratch/0/bharadwk/CRISPR/bin/CRT1.2-CLI.jar crt %s /scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_crispr/CRISPRs_Repeats_Spacers_%s.out" %(name,tmp_name)
					sp.call(cmd, shell=True)
					path4 = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_crispr/CRISPRs_Repeats_Spacers_%s.out" %(tmp_name)
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

from CRISPRstand import crispr_strand
from consensus_repeat import consensus_repeat
from rev_complementary import get_reverse_comp

class write_repeat_file(object):
	
	def write_Repeat_File(self, cp_ID=0, path1="", dest_path2="", r_tmp=""):		
		
		crispr_file = open(path1, 'r')		
		fo1 = open(dest_path2, "a")

		result = []
		for line in crispr_file:
			result.append(line.split())

		num = 0
		pos = 0
		ind_space = []
		num_of_crispers = 0
		index1 = 0
		tmp_val = []
		s = 0

		for ind, z in enumerate(result):
			for y in z:
				if '--------' in y:
					ind_space.append(ind)
				
		myset = set(ind_space)
		myset = sorted(myset)
		myset = myset[1::2]
		
		strand = crispr_strand()
		con_rep_seq = consensus_repeat()
		consensus = con_rep_seq.get_Consensus_Repeat(path1)
		
		for sequence in consensus: 
			tmp_val.append(strand.getOrientation(sequence))
			
		len_of_list = len(tmp_val)	
		rev = get_reverse_comp()	

		for pos, x in enumerate(result):
			for i in x:
				if 'POSITION' in i:										
					pos = pos+2							
					num_of_crispers = num_of_crispers+1
					fo1.write('>'+cp_ID+'-'+str(r_tmp)+'\n')																
					
					if s<len_of_list and tmp_val[s]>0:																
						for num in range(pos,myset[index1]):									
							fo1.write(result[num][1]+'\t')									
						fo1.write('\n')
						index1 = index1+1	
						
					elif s<len_of_list and tmp_val[s]<0:								
						for num in range(myset[index1]-1,pos-1,-1):									
							seq_item = result[num][1]
							seq_item = str(seq_item)
							rev.reverse_complementary(seq_item)
							fo5 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data/reverse_complementary/INPUT_R.SEQUENCE", "r")
							seq_item = fo5.readline()
							fo1.write(seq_item+'\t')	
							fo5.close()								
						fo1.write('\n')
						index1 = index1+1
														
					s = s+1		
										
		crispr_file.close()
		fo1.close()

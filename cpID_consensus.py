import os.path

class cp_id_consensus(object):

	 def write_cpID_consensus(self, source_path="", dest_path=""):	

		fo2 = open(dest_path, 'a')
		fo2.write('{a:^10}{b:^70}'.format(a='CP_CRISPR', b='Consensus_Repeat'))
		fo2.write('\n\n')	

		if os.path.exists(source_path):
			
			fo1 = open(source_path, "r")
			result = []
			tmp_list1 = []
			tmp_str = ""
			tmp_list2 = []
			consensus = []

			for line in fo1:
				result.append(line.split())

			length = len(result)

			for i in range(1,length,2):
				tmp_list1 = result[i]
				DominantRepeat = {}
				for j in range(0,len(tmp_list1)):
					eachRepeat = tmp_list1[j]
					DominantRepeat[eachRepeat] = DominantRepeat.get(eachRepeat, 0) + 1
				consensus_seq = max(DominantRepeat, key = DominantRepeat.get)
				consensus.append(consensus_seq)

			for i in range(0,length,2):	
				tmp_str = ','.join(result[i])
				tmp_list2.append(tmp_str)

			id_len = len(tmp_list2)
			
			for i in range(0,id_len):
				fo2.write('{:>10}'.format(tmp_list2[i]))
				fo2.write('{:>50}'.format(consensus[i]))
				fo2.write('\n')

			fo1.close()
			fo2.close()
		
		else:
			print "There is no file for processing, kindly enter the required file"

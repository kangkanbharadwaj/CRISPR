class consensus_repeat(object):
	
	def get_Consensus_Repeat(self, path=""):		
		
		#path = '/scratch/0/bharadwk/CRISPR/CRISPR/fasta_files/CRISPRs_Repeats_Spacers_'+tmp_name+".out"
		#print path
		crispr_file = open(path, 'r')
		result = []

		for line in crispr_file:
			result.append(line.split())

		num = 0
		pos = 0
		ind_space = []
		num_of_crispers = 0
		index1 = 0
		consensus = []

		for ind, z in enumerate(result):
			for y in z:
				if '--------' in y:
					ind_space.append(ind)
				
		myset = set(ind_space)
		myset = sorted(myset)
		myset = myset[1::2]

		for pos, x in enumerate(result):
			for i in x:
				if 'POSITION' in i:
					DominantRepeat = {}			
					pos = pos+2		
					for num in range(pos,myset[index1]):
						eachRepeat = result[num][1]
						DominantRepeat[eachRepeat] = DominantRepeat.get(eachRepeat, 0) + 1				
					consensus_seq = max(DominantRepeat, key = DominantRepeat.get)
					consensus.append(consensus_seq)					
					index1 = index1+1														
		
		return consensus
		crispr_file.close()
		

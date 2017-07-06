class new_features(object):	

	def motif_presence(self, repeat=None):			
				
		req_motif = 'ATTGAAA'	
		
		if req_motif in repeat:
			return 1
		else:
			return 0
			
	def nucleotide_percentage(self, repeat=None):
		
		len_of_repeat = len(repeat)
		
		count_a = repeat.count('A')
		count_g = repeat.count('G')
		count_t = repeat.count('T')
		count_c = repeat.count('C')
		
		per_a = (count_a/len_of_repeat)*100
		per_g = (count_g/len_of_repeat)*100
		per_t = (count_t/len_of_repeat)*100
		per_c = (count_c/len_of_repeat)*100

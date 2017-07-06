import os

class get_reverse_comp(object):
	
	def reverse_complementary(self, sequence):		
		
		Repeat = sequence
		tmp_val = 0
		sequence.replace('U','T') # repalce if there exists a nucleotide 'U' with nucleotide 'T' in the retrieved repeat

		#write the repeat to file "INPUT_F.SEQUENCE"
		f = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/reverse_complementary/INPUT_F.SEQUENCE","w")
		f.write(Repeat) 
		f.close()

		# write reverse complementary of the repeat to file "INPUT_R.SEQUENCE"
		cmd = "tr ATGC TACG < /scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/reverse_complementary/INPUT_F.SEQUENCE | rev > /scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/reverse_complementary/INPUT_R.SEQUENCE"
		os.popen(cmd)
		

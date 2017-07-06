################################################################################################################################
#### This function decides the Strand of a CRISPR.
#### Here, 'Repeat' of a CRISPR is written to a file and "EDeN" tool has been used on this file, which results a numeric value1.
#### "EDeN" tool is also used on reverese complementary of the sequence 'Repeat' resulting another numeric value2.
#### If (value1-value2)/2 greater than zero, then the 'Repeat' is in Forward Strand.
#### If not, then it is in Reverse Strand.
################################################################################################################################
import os

class crispr_strand(object):
	

	def getOrientation(self, sequence=''):
		'''
		:param lowRange: CRISPR low range
		:param highRange: CRISPT high range. Both these parameters  are used to get the repeat sequence from the genome file to figure out the strand
		: return - 1 if the crispr is in forward strand
				 - 0 if the crispr is in reverese strand
		'''

		# select the repeat sequence using the lowRange and highRange parameters
		#cmd="awk 'NR==2' temp_folder/sequence.fasta | cut -c"+str(lowRange)+"-"+str(highRange) #+" > INPUT_F.SEQUENCE"
		#Repeat = subprocess.check_output(cmd,shell=True)    # save the obtained repeat in a variable 

		Repeat = sequence
		tmp_val = 0
		sequence.replace('U','T') # repalce if there exists a nucleotide 'U' with nucleotide 'T' in the retrieved repeat

		#write the repeat to file "INPUT_F.SEQUENCE" and execute the Eden tool to compute the score in forward strand
		f = open("/scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/INPUT_F.SEQUENCE","w")
		f.write(Repeat) 
		f.close()
		cmd = "/scratch/0/bharadwk/CRISPR/bin/EDeN -a TEST -i /scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/INPUT_F.SEQUENCE -M 1 -r 3 -d 3 -f SEQUENCE -g DIRECTED -m /scratch/0/bharadwk/CRISPR/bin/DR_Repeat_model -y /scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/For >/dev/null"
		os.popen(cmd) # execute the eden tool on the file "INPUT_F.SEQUENCE" and save the output file in "For" folder

		#Repeat = re.sub('.', lambda m: {'A':'T', 'G':'C','T':'A', 'C':'G'}.get(m.group(), m.group()), Repeat)  ## complementary sequence
		#Repeat = Repeat[::-1]  ## Reverse the sequence

		# write reverse complementary of the repeat to file "INPUT_R.SEQUENCE"
		cmd = "tr ATGC TACG < /scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/INPUT_F.SEQUENCE | rev > /scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/INPUT_R.SEQUENCE"
		os.popen(cmd)
		# compute the Eden score on the reverse complementary repeat and store in "Rev" folder
		cmd = "/scratch/0/bharadwk/CRISPR/bin/EDeN -a TEST -i /scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/INPUT_R.SEQUENCE -M 1 -r 3 -d 3 -f SEQUENCE -g DIRECTED -m /scratch/0/bharadwk/CRISPR/bin/DR_Repeat_model -y /scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/Rev >/dev/null"
		os.popen(cmd)

		#cmd = "chmod -r 777 /scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/For" # give the access permissions to the folder "For" and the file "prediction" inside the folder
		#os.popen(cmd)

		#cmd = "chmod -r 777 /scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/Rev" # give the access permissions to the folder "Rev" and the file "prediction" inside the folder
		#os.popen(cmd)

		#cmd = "chmod 777 temp_folder/For/prediction"
		#os.popen(cmd)

		#cmd = "chmod 777 temp_folder/Rev/prediction"
		#os.popen(cmd)

		f= open("/scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/For/prediction","r") 
		val_in_plus = float((f.readline().split())[1])  # read the score of forward strand from "prediction" file from "For" folder
		f.close()

		f= open("/scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/Rev/prediction","r")
		val_in_minus = float((f.readline().split())[1]) # read the score of reverse strand from "prediction" file from "Rev" folder
		f.close()

		#print val_in_plus, val_in_minus
		val_in_minus = val_in_minus  * -1   # the score from reverse strand is multiplied with -1, as the score obtained after performing reverse complementary
		#print val_in_plus, val_in_minus

		# if the sum of the scores from forward and reverse strand is greater than zero, then the repeat is in forward strand or else it is in reverse strand
		val = (val_in_plus + val_in_minus)/2 
		#print val
		
		if val > 0:
			#print "Repeat sequence in forward strand\n"
			tmp_val = 1
			
		else:
			#print "Repeat sequence in reverse strand\n"
			tmp_val = -1
		
		return tmp_val



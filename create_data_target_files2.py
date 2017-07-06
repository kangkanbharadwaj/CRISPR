class create_files(object):

	def create_files(self):

		#N = 250
		fo11_contents = []
		fo11 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_encoded_files/enclode_true.txt", "r")		
		for line in fo11:
			line = line.strip()			
			fo11_contents.append(line)			
		
		#fo11_contents = fo11.read()
		fo12_contents = []
		fo12 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_encoded_files/encode_false.txt", "r")
		for line in fo12:
			line = line.strip()
			fo12_contents.append(line)
		
		#fo12_contents = fo12.read()
		fo13_contents = []
		fo13 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/target_true_file/target_true.txt", "r")
		for line in fo13:
			line = line.strip()			
			fo13_contents.append(line)			
		
		#fo13_contents = fo13.read()
		fo14_contents = []
		fo14 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/target_false_file/target_false.txt", "r")
		for line in fo14:
			line = line.strip()			
			fo14_contents.append(line)		
		#fo14_contents = fo14.read()
		
		fo_train_fo11 = fo11_contents[0:249]		
		fo_test_fo11 = fo11_contents[249::]
		
		fo_train_fo12 = fo12_contents[0:249]
		fo_test_fo12 = fo12_contents[249::]
		
		fo_train_fo13 = fo13_contents[0:249]
		fo_test_fo13 = fo13_contents[249::]
		
		fo_train_fo14 = fo14_contents[0:249]
		fo_test_fo14 = fo14_contents[249::]
		
		fo11trainfo12 = fo_train_fo11 + fo_train_fo12
		fo15 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/data_train.seq", "w")
		for line in fo11trainfo12:
			fo15.write(line)
			fo15.write('\n')
		
		fo13trainfo14 = fo_train_fo13 + fo_train_fo14
		fo16 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/data_train.target", "w")		
		for line in fo13trainfo14:
			fo16.write(line)
			fo16.write('\n')
		
		fo11testfo12 = fo_test_fo11 + fo_test_fo12
		fo17 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/data_test.seq", "w")
		for line in fo11testfo12:
			fo17.write(line)
			fo17.write('\n')
		
		fo13testfo14 = fo_test_fo13 + fo_test_fo14
		fo18 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/data_test.target", "w")
		for line in fo13testfo14:
			fo18.write(line)
			fo18.write('\n')

		fo11.close()
		fo12.close()
		fo13.close()
		fo14.close()
		fo15.close()
		fo16.close()

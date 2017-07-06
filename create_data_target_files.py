class create_files(object):

	def create_files(self):
		
		fo11_contents = []
		fo11 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_encoded_files/enclode_true.txt", "r")
		fo12 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_encoded_files/encode_false.txt", "r")
		fo13 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/target_true_file/target_true.txt", "r")
		fo14 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/target_false_file/target_false.txt", "r")		
		
		fo15 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/data.seq", "w")
		fo16 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/data.target", "w")		

		
		fo11_contents = fo11.read()
		fo12_contents = fo12.read()
		fo13_contents = fo13.read()
		fo14_contents = fo14.read()
		
		fo15.write(fo11_contents + fo12_contents)
		fo16.write(fo13_contents + fo14_contents)
		

		fo11.close()
		fo12.close()
		fo13.close()
		fo14.close()
		fo15.close()
		fo16.close()

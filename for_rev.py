from itertools import izip
from new_features import new_features

class for_rev(object):

	def encode_to_org(self):	

		def deduce_org(string=None):
			encode_str = string
			encode_str = ''.join([i for i in encode_str if not i.isdigit()])
			encode_str = encode_str.replace("Y","")
			encode_str = encode_str.replace("N","")
			encode_str = encode_str.replace("X","")
			encode_str = encode_str.replace("-","")
			return encode_str
			

		fo1 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_encoded_files/enclode_true.txt", "r")
		fo2 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/bio_encoded_files/encode_false.txt", "r")
		fo3 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/for_rev/for_rev.txt", "a")
		fo5 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/modified_encoding/enclode_true.txt", "a")
		fo6 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/modified_encoding/encode_false.txt", "a")
		
		feature_obj = new_features()

		with fo1, fo2:
			str_x = ''
			str_y = ''
			for_str_x = ''
			for_str_y = ''
			for x, y in izip(fo1, fo2):
				for_str_x = x
				for_str_y = y
				for_str_x = for_str_x.rstrip()
				for_str_y = for_str_y.rstrip()
				
				str_x = x.strip()
				str_y = y.strip()
				str_x = deduce_org(str_x)
				str_y = deduce_org(str_y)
												
				fo3.write('{:>10}'.format(str_x))
				fo3.write('{:>40}'.format(str_y))
				fo3.write("\n")
				
				ret_val1 = feature_obj.motif_presence(str_x)
				ret_val2 = feature_obj.motif_presence(str_y)
				
				if ret_val1 == 1:					
					for_str_x = ''.join((for_str_x, 'M'))
					print for_str_x
					fo5.write(for_str_x)
					fo5.write('\n')
				else:
					for_str_x = ''.join((for_str_x, 'N'))
					fo5.write(for_str_x)
					fo5.write('\n')
				
				if ret_val2 == 1:
					for_str_y = ''.join((for_str_y, 'M'))
					fo6.write(for_str_y)
					fo6.write('\n')
				else:
					for_str_y = ''.join((for_str_y, 'N'))
					fo6.write(for_str_y)
					fo6.write('\n')
				
		
		fo1.close()
		fo2.close()
		fo3.close()
		fo5.close()
		fo6.close()

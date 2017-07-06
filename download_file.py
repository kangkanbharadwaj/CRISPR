from Bio import Entrez
from urllib2 import HTTPError

class download_fasta_file(object):
	def download_file(self, crispr_id=None, count=None):

		#FastaFile = "CP003098"
		FastaFile = crispr_id
		'''
		:param FastaFile : The parameter contains the accession number to be downloaded from ncbi website.
		:return - 0 for error in downloading the fasta file
				  1 for successful download
		'''
		# ref.: http://wilke.openwetware.org/Parsing_Genbank_files_with_Biopython.html

		# replace with your real email (optional):

		Entrez.email = 'whatever@mail.com'

		# accession id works, returns genome in fasta format, looks in the 'nucleotide' database:
		try:
			handle=Entrez.efetch(db='nucleotide',id=FastaFile,rettype='fasta')  # The genome with the accession number is fetched from ncbi server and saved in 'handle' variable
		except HTTPError:
			print "Error received in retrieving the fasta file with the given Accession Number.\nPlease check the Accession Number, or\nPlease check your internet connection or The 'NCBI' web server is down.\n"
			
		# store locally:
		local_file=open('/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/fasta_files/%s__%s.fa' %(FastaFile,count), 'w') 
		local_file.write(handle.read()) # write the genome to a file
		handle.close()
		local_file.close()


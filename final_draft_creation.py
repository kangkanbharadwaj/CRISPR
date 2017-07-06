class final_draft_create(object):
	
	def file_create(self, path=""):
		fo1 = open(path, 'w')				
		fo1.write('{a:^10}{b:^50}{c:^40}{d:^15}{e:^15}{f:^25}'.format(a='CP_CRISPR', b='Consensus_Repeat', c='Start', d='End', e='Repeat_Average_length', f='Spacer_Average_length'))		
		fo1.write('\n\n')
		fo1.close()


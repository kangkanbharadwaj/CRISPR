import re
import glob
from create_m_r_d_behaviour_file import m_r_d_variations

#folder_lists = ['Test_dir_with_negative_positioning', 'Test_dir_with_positive_positioning', 'Test_dir_X_pos_negative-positioning', 'Test_dir_X_pos_positive_positioning']
folder_lists = ['validation']

for x_names in folder_lists:
	
	#fo1 = open("/scratch/0/bharadwk/CRISPR/CRISPR/m_r_d_specifications/%s.txt" %(x_names), "w")
	fo1 = open("/scratch/0/bharadwk/CRISPR/CRISPR/biological_data/m_r_d_specifications/%s.txt" %(x_names), "w")
	fo1.write('{a:^0}{b:^0}{c:^0}{d:^10}{e:^10}{f:^10}{g:^10}{h:^10}{i:^10}{j:^10}{k:^15}{l:^15}{m:^15}{n:^15}{o:^15}{p:^15}{q:^15}{r:^15}{s:^10}'.format(a='m', 
				b='r', c='d', d='SIZE', e='CORRECT', f='ERROR', g='TP', h='FP', i='FN', j='TN', k='+PRECISION', l='+RECALL', 
				m='+F-MEASURE', n='-PRECISION', o='-RECALL', p='-F-MEASURE', q='bPRECISION', r='bRECALL', s='bF-MEASURE'))

	fo1.write('\n\n')
	fo1.close()
	
	path_name = "/scratch/0/bharadwk/CRISPR/CRISPR/biological_data/%s/*.txt" %(x_names)
	filenames = glob.glob(path_name)
	mrd_obj = m_r_d_variations()

	for fname in filenames:
		fname = fname.split('/')[8]
		mrd_obj.create_m_r_d_files(x_names,fname)





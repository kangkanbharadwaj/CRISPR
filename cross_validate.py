import os

from create_data_target_files import create_files
create_obj = create_files()
create_obj.create_files()
'''
list_of_paths = ['/scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/']

for items in list_of_paths:
	for m in range(1,2):
		for r in range(1,6):
			for d in range(1,6):
				print m, r, d
				#cmd2 = "/scratch/0/bharadwk/CRISPR/bin/EDeN -y %s -i %sdata.seq -M %d -f SEQUENCE -r %d -d %d  -g DIRECTED -t %sdata.target -a CROSS_VALIDATION > %soutput_file_m%d_r%d_d%d.txt" %(items, items, m, r, d, items, items, m, r, d)
				cmd1 = "/scratch/0/bharadwk/CRISPR/bin/EDeN -a TRAIN -i %sdata_train.seq -t %sdata_train.target -M %d -r %d -d %d -f SEQUENCE -g DIRECTED >/dev/null" %(items, items, m, r, d)
				os.popen(cmd1)
				cmd2 = "/scratch/0/bharadwk/CRISPR/bin/EDeN -a TEST -i %sdata_test.seq -M 3 -f SEQUENCE -g DIRECTED -r $r -d $d -m model>/dev/null" %(items)
				os.popen(cmd2)
				cmd3 = "paste %sdata_test.target %sprediction | awk '{print $1,$3}' | /scratch/0/bharadwk/CRISPR/bin/perf -t 0 2>/dev/null| grep ROC" %(items, items)
				os.popen(cmd3)
'''

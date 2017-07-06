for d in 0 2 4 6; do for r in 0 1 2 3 4 5; do echo -n "r=$r d=$d  ">/dev/null;
/scratch/0/bharadwk/CRISPR/bin/EDeN -a TRAIN -i /scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/data_train.seq -t /scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/data_train.target -M 3 -r $r -d $d -f SEQUENCE -g DIRECTED >/dev/null; 
/scratch/0/bharadwk/CRISPR/bin/EDeN -a TEST -i /scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/data_test.seq -M 3 -f SEQUENCE -g DIRECTED -r $r -d $d -m model>/dev/null; 
paste /scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/data_test.target /scratch/0/bharadwk/CRISPR/CRISPR/biological_data2/validation/prediction | awk '{print $1,$3}' | /scratch/0/bharadwk/CRISPR/bin/perf -t 0 2>/dev/null| grep ROC; done; done


#/scratch/0/bharadwk/CRISPR/bin/EDeN -a TEST -i /scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/INPUT_R.SEQUENCE -M 1 -r 3 -d 3 -f SEQUENCE -g DIRECTED -m /scratch/0/bharadwk/CRISPR/bin/DR_Repeat_model -y /scratch/0/bharadwk/CRISPR/CRISPR/for_rev_crispr_seq/Rev >/dev/null

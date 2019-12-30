scp -P 50032 -r $1 root@64.185.231.154:/var/share/dbl/get_data/auto
ssh -p 50032 root@64.185.231.154 /var/share/dbl/get_data/auto/get_data_n.sh $1 

<<COMMNETOUT
gcloud beta compute tpus create shin-tpu \
	      --zone=us-central1-a \
	      --range='10.0.101.0' \
	      --accelerator-type='v3-8' \
              --network=default \
	      --version='1.6'\
              --async \
	      --description='My TF Node' \
	      --preemptible



bash jp_ft_fine_tune_sample.sh

bash jp_ft_fine_tune_sample_eval.sh





gcloud beta compute tpus delete shin-tpu\
	     --zone=us-central1-a\
	     --async

COMMENTOUT

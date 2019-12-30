scp -P 50032 -r $1 root@64.185.231.154:/var/share/dbl/get_data/auto
echo "ファイルアップロード完了" >> on_process_m.csv
ssh -p 50032 root@64.185.231.154 /var/share/dbl/get_data/auto/get_data.sh $1

echo ruby -v
echo 'something'


scp -p 50032 -r root@64.185.231.154:/var/share/dbl/get_data/auto/$1_output .
<< COMMENTOUT

echo "転移学習開始" >> on_process_m.csv
gcloud beta compute tpus create shin-tpu \
	      --zone=us-central1-a \
	      --range='10.0.101.0' \
	      --accelerator-type='v3-8' \
              --network=default \
	      --version='1.15'\
	      --description='My TF Node' \
	      --preemptible



bash jp_ft_fine_tune_sample.sh

bash jp_ft_fine_tune_sample_eval.sh





gcloud beta compute tpus delete shin-tpu\
	     --zone=us-central1-a\
			 --async\



COMMENTOUT

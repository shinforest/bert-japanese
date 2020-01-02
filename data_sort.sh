ON_PROCESS_PATH = on_process.csv


retry() {
   MAX_RETRY=5
   n=0
   until [ $n -ge $MAX_RETRY ]
   do
      "$@" && break
      n=$[$n+1]
      sleep $[ ( $RANDOM % 15 )  + 1 ]s
   done
   if [ $n -ge $MAX_RETRY ]; then
     echo "$message失敗,-" >> $ON_PROCESS_PATH
     echo "Sorry.Please try uploading file again,-" >> $ON_PROCESS_PATH
     rm -r project_name/$1
     exit 1
   fi
}


<< COMMENTOUT
message = "データ転送"
echo "$message開始,-" >> $ON_PROCESS_PATH
retry scp -P 50032 -r project_name/$1 root@64.185.231.154:/var/share/dbl/get_data/auto
echo "$message完了,-" >> $ON_PROCESS_PATH

message = "データ前処理"
echo "$message開始,-" >> $ON_PROCESS_PATH
retry ssh -p 50032 root@64.185.231.154 /var/share/dbl/get_data/auto/get_data.sh $1
echo "$message終了,-" >> $ON_PROCESS_PATH


scp -P 50032 -r root@64.185.231.154:/var/share/dbl/get_data/auto/$1_output .

COMMENTOUT

echo "TPU立ち上げ開始,-" >> $ON_PROCESS_PATH
for location in us-cenntral1-a us-central1-b us-central1-c asia-east1-c europe-west4-a; do
	gcloud beta compute tpus create shin-tpu \
	      --zone=$location \
	      --range='10.0.101.0' \
	      --accelerator-type='v3-8' \
              --network=default \
	      --version='1.15'\
	      --description='My TF Node' \
	      --preemptible > tpu.log 2>&1


	if  grep -q ERROR "tpu.log" && echo "$locationでTPU立ち上げ失敗しました">> $ON_PROCESS_PATH; then
		continue
	else echo "$locationでTPUが立ち上がりました,-" >> $ON_PROCESS_PATH && break
  fi
done

start_time=`date +%s`


<< COMMENTOUT
message = "転移学習"
echo "$message開始,-"　>> $ON_PROCESS_PATH
retry bash jp_ft_fine_tune_sample.sh
echo "$message終了,-"　>> $ON_PROCESS_PATH

echo "予測開始,-" $ON_PROCESS_PATH
retry bash jp_ft_fine_tune_sample_eval.sh
echo "予測終了,-"　>> $ON_PROCESS_PATH





gcloud beta compute tpus delete shin-tpu\
	     --zone=$location\
       --async
			 -q

echo "TPU終了,-"　>> $ON_PROCESS_PATH
end_time=`date +%s`
time=$((end_time - start_time))
price = 2.4*$time
echo "TPU費用：$price米ドル,-"　>> $ON_PROCESS_PATH


COMMENTOUT

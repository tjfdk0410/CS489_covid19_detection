export TASK_NAME=sst2

python run_covid.py \
  --model_name_or_path bert-base-cased \
  --tokenizer_name bert-base-cased \
  --do_train \
  --do_eval \
  --do_predict \
  --train_file=./txt_augment.csv \
  --validation_file=val.csv \
  --test_file=./test.csv \
  --max_seq_length 140 \
  --per_device_train_batch_size 128 \
  --learning_rate 2e-5 \
  --num_train_epochs 12 \
  --output_dir ./result/maxseq140_batch64_ep12_aug


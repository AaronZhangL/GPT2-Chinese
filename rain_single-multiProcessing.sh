python train_single-multiProcessing.py \
--model_config config/model_config_kehuan.json \
--tokenized_data_path data/tokenized/ \
--tokenizer_path cache/vocab_kehuan.txt \
--raw_data_path data/train-kehuan-utf8.json \
--epochs 30 \
--log_step 200 \
--stride 512 \
--output_dir model/ \
--device 0 \
--num_pieces 32 \
--batch_size 4 \
--raw

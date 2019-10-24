python generate_texts.py \
  --device 0 \
  --length 900 \
  --tokenizer_path cache/vocab_kehuan-from.txt \
  --model_path model/model_epoch1 \
  --titles "在距离地球100万光年的地方，有一个与地球文明相似的星球。" \
  --topp 1 \
  --temperature 1.0

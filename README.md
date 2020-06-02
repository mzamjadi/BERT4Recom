# Run BERT4Rec as benchmark on amazon-book dataset.


**Requirements**

* python 2.7+
* Tensorflow 1.12 (GPU version)
* CUDA compatible with TF 1.12

**Run**

Please make sure to unzip files. We run amazon as an example:

``` bash
./run_amazon.sh
```
include two part command:
Make sure to change the directory (the first sentence in the run file) to your environment. The first part of the run file generates masked training, and test data. 
``` bash
python -u gen_data_fin.py \
    --dataset_name=${dataset_name} \
    --max_seq_length=${max_seq_length} \
    --max_predictions_per_seq=${max_predictions_per_seq} \
    --mask_prob=${mask_prob} \
    --dupe_factor=${dupe_factor} \
    --masked_lm_prob=${masked_lm_prob} \
    --prop_sliding_window=${prop_sliding_window} \
    --signature=${signature} \
    --pool_size=${pool_size} \
```

The second part train the model. The modeling part exists in the function model_fn_builder in the run.py file which uses some of the functions in the modeling.py. In the run file, we also have input_fn_builder function which reads data from the train.tfrecord and test.tfrecord files created before. Optimization file maily models a convoluted version of the Adam optimizer for training the NN. bert_train file includes different configurations for the datasets used in Bert4Rec (not necessary for us). Modeling.py incorporates the structure of the transformers.
``` bash
CUDA_VISIBLE_DEVICES=0 python -u run.py \
    --train_input_file=./data/${dataset_name}${signature}.train.tfrecord \
    --test_input_file=./data/${dataset_name}${signature}.test.tfrecord \
    --vocab_filename=./data/${dataset_name}${signature}.vocab \
    --user_history_filename=./data/${dataset_name}${signature}.his \
    --checkpointDir=${CKPT_DIR}/${dataset_name} \
    --signature=${signature}-${dim} \
    --do_train=True \
    --do_eval=True \
    --bert_config_file=./bert_train/bert_config_${dataset_name}_${dim}.json \
    --batch_size=${batch_size} \
    --max_seq_length=${max_seq_length} \
    --max_predictions_per_seq=${max_predictions_per_seq} \
    --num_train_steps=${num_train_steps} \
    --num_warmup_steps=100 \
    --learning_rate=1e-4
```

### hyper-parameter settings
json in `bert_train` like `bert_config_ml-1m_64.json`

```json
{
  "attention_probs_dropout_prob": 0.2,
  "hidden_act": "gelu",
  "hidden_dropout_prob": 0.2,
  "hidden_size": 64,
  "initializer_range": 0.02,
  "intermediate_size": 256,
  "max_position_embeddings": 200,
  "num_attention_heads": 2,
  "num_hidden_layers": 2,
  "type_vocab_size": 2,
  "vocab_size": 24919
}
```


=======
# BERT4Recom
BERT for sequential recommendation system in Tensor Flow.


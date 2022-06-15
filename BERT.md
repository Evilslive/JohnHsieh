
## 開啟 BERT 的正確方法

### transformers

> extract dims based on tensorflow

```python
from transformers import BertTokenizer, TFBertModel
# 包含有tf_model.h5的路徑 
MODEL_PATH = 'bert-base-chinese\\' 
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
tokenizer('今天天氣真好', return_tensor='tf')
```
```
>>> {'input_ids': <tf.Tensor: shape=(1, 8), dtype=int32, numpy=array([[ 101,  791, 1921, 1921, 3706, 2523, 1962,  102]])>, 
'token_type_ids': <tf.Tensor: shape=(1, 8), dtype=int32, numpy=array([[0, 0, 0, 0, 0, 0, 0, 0]])>, 
'attention_mask': <tf.Tensor: shape=(1, 8), dtype=int32, numpy=array([[1, 1, 1, 1, 1, 1, 1, 1]])>}
```
藉由 tokenizer 將輸入代碼化, 預設dict key為 input_ids、token_type_ids、attention_mask
* 中文長度為字數+2, '今'對應 791、'天' 對應 1921
* 英文則看細粒度 words -> wordpieces

特殊token(預設編號)
*   0 `[PAD]` 固定不同序列的輸入長度
* 100 `[UNK]` 代表不存在 *vocab.txt* 收錄的key
* 101 `[CLS]` 等於 pooler output (? 還是 last hidden state), 用來代表整句話
* 102 `[SEP]` 當一個輸入序列有兩句話時作為切分
* 103 `[MASK]` MLL 的核心, 透過隨機遮罩15%, 來訓練模型


> 預設參數




> 模型選擇

```python
model = TFBertModel.from_pretrained(MODEL_PATH)
```


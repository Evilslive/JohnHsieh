
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

chinese模型只有一種, 12*12*768



> 模型啟用

```python
model = TFBertModel.from_pretrained(MODEL_PATH)
model('下雨天', output_hidden_states=True, output_attentions=True)
```
模型輸出預設以numpy()輸出
* `last_hidden_state`: 預設輸出, 隱藏層的最後一層
* `pooler_output`: 預設輸出, 平均句向量 (同過attention後的CLS ?)
* `hidden_states`: 透過output_hidde_states輸出, 有0-12共13層 (0可能是初始隨機層 ?), 每層都會包在list內,跟輸入字數有關 (13 x 1 x input_length)
* `attentions`: 透過output_attentions輸出, 12個頭 x 12層, 共144個, 包兩層:第一層tuple、第二層list (12 x 1 x 12), 與輸入長度無關
* `logits`: 透過執行分類任務模型取得, 各類的分類可能邏輯值
* `loss`: 透過執行分類任務模型取得

> 四大下游任務

* `TFBertModel`
* `TFBertForTokenClassification`
* `TFBertForSequenceClassification`
* `TFBertForQuestionAnswering`




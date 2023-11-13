## _Natural Language Processing_
期待看到可以持續增加token與合併簡化token的模型 (Piaget: assimilation & accommodation)

斷詞 Word segmentation, WS 
詞類標註 Part-of-speech tagging, POS 
實體命名識別 Name entity recognition, NER 
關係抽取 Relationship extraction 
抽取式摘要
生成式摘要 

### 分類任務
#### 分類器參數, Activation Function
        linear: f(x) = x, -inf to inf 
        sigmoid: f(x) = 1/(1+e^x), 0 to 1 
        tanh: , -1 to 1 
        relu: max(0, x), 0 to inf 
        leaky relu:
---

* sigmoid: 0 to 1, 特性 
1.單側抑制 
2.相對寬闊的邊界(-6 to -6) 
3.稀疏激活性 函式 f(x) = 1 / (1+exp(-x)) 導數 f'(x) = f(x)(1-f(x)) 
* tanh(TanHyperbolic): -1 to 1 函式 f(x) = (e^x - e^(-x)) / (e^x + e^(-x)) 導數 f'(x) = 1 - (f(x))^2 
* ReLU(Rectifield Linear Units): 0 to inf, 特性 1.無梯度消失的問題 2.歸0時cell死亡 函式 f(x) = max(0, x) 導數 f'(x) = {1, x>0; 0, x<=0} 
* softmax: 0 to 1 特性 逼進0與1 函式 f(x)i = e^x_i / sigma(k=1 to K) e^x_k 導數

### 配對任務


---
### 作用於NLP的偉大發明

+ *1847* &emsp; Cauchy &emsp; **gradient descent**: 梯度下降
+ *1953* &emsp; Taylor &emsp; **cloze procedure**: Masked Language Model的先驅
+ *1986* &emsp; Rumelhart et al. &emsp; **back-propagation**: 後向傳遞
+ *2013* &emsp; Mikolov &emsp; **word embedding**: Word2Vec 詞嵌入
+ *2018* &emsp; Google &emsp; **BERT**: MLM模型的實現
+ *2020* &emsp; Google &emsp; **mT5**: 跨語言模型(縮寫跟金融領域的某個產品撞名常google不到, 你看!命名多重要!)


### **for SOTA**

+ [Papper with Code](https://paperswithcode.com/sota) 蒐集趨勢研究與程式碼
+ [SOTA Ai](https://www.stateoftheart.ai/) 組織重點任務、開放資料與模型
+ [spaCy](https://spacy.io/) 先別說NLTK了, 你有沒有聽過spaCy ? 滿足客製化需求的NLP套件

### 巨人的肩膀

***Google***
> [Research Publications](https://research.google/research-areas/)<br>&emsp;&emsp;各項領域的研究成果<br>
> [Natural Language](https://cloud.google.com/natural-language?hl=zh-tw)<br>
> &emsp;&emsp;兩項NLP產品:<br>
> &emsp;&emsp;&emsp;&emsp;1. 線上訓練模型/AutoML<br>
> &emsp;&emsp;&emsp;&emsp;2. 透過google的模型進行分析/API<br>
> [Ai Blog](https://ai.googleblog.com/)<br>&emsp;&emsp;意圖將Ai科普化<br>

***Facebook***
> [Research Publications](https://research.fb.com/publications/)<br>&emsp;&emsp;各項領域的研究成果<br>
> [Natural Language](https://wit.ai/)<br>&emsp;&emsp;wit.ai提供APP教學, 也可透過http APi<br>
> [for Developers](https://developers.facebook.com/?no_redirect=1)<br>&emsp;&emsp;開發人員專區<br>
> [Meta Ai](https://ai.facebook.com/)<br>臉書的人工智慧實驗室

***Microsoft***
> [OpenAi api](https://openai.com/) Musk創辦, 以 GPT-3, DALL.E 2 知名 (雖然open 但卻是很慢很慢的 開放試用... ) 

***IBM***
> [Research Publications](https://mitibmwatsonailab.mit.edu/research/papers-code/)

***nViDiA***
> [Blog](https://developer.nvidia.com/blog/)

***Stanford University***
> [Ai Index](https://aiindex.stanford.edu/)

***中研院***
> [CKIP Lab](https://ckip.iis.sinica.edu.tw/resource)<br>&emsp;&emsp;Traditional Chinese models & NLP tools !!




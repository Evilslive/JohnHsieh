


"""
    進行輸入輸出分析, 自動化產生命題
    導入輸入頁面, 直接進行分析
"""

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

def sql(date:str="sql0518.txt"):
    with open(date, 'r', encoding="utf-16") as f:
        database = f.readlines()
    return [i[:-1].split(",") for i in database][1:] # 去掉標題列

def pickup(data:list, text:str, strict:int=0):
    rigorous, loose = [], []
    for item in data:
        kw = item[2].split("/")
        if "" in kw: kw.remove("")
        if strict: # 嚴格標準, 關鍵詞都有才算
            if kw == [i for i in kw if i in text]:
                rigorous.append(item)
        else: # 寬鬆標準, 關鍵詞有一個就算
            for k in kw:
                if k in text:
                    loose.append(item)
                    break
    if strict: return rigorous
    else: return loose

@app.route('/',methods=['POST','GET'])
def index():
    database = sql()
    if request.method =='POST':
        if request.values['send']=='出 題':
            text = request.values.get('user') # 抓取要分析的文本
            result = pickup(database, text)
            return render_template('index.html', **locals())
    return render_template('index.html',result="")

if __name__ == "__main__":
    app.run(
        debug=True
    )


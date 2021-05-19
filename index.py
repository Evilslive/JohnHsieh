


"""
    進行輸入輸出分析, 自動化產生命題
    導入輸入頁面, 直接進行分析
"""

from flask import Flask
from flask import render_template, request

app = Flask(__name__)

def sql(date:str="sql0518.txt"):
    with open("D:\\CCU\\codes\\Python\\NLP\\exam\\"+date, 'r', encoding="utf-16") as f:
        database = f.readlines()
    return [i[:-1].split(",") for i in database]


@app.route('/',methods=['POST','GET'])
def index():
    database = sql()
    if request.method =='POST':
        if request.values['send']=='出 題':
            result = request.values.get('user')

            

            return render_template('index.html',result=result)
    return render_template('index.html',result="")

if __name__ == "__main__":
    app.run(
        debug=True
    )


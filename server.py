from flask import Flask
from flask import request
from flask import jsonify  
from newspaper import Article
import numpy as np
import inference

model = inference.detect_fake_news('gpu')

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
@app.route('/infer', methods=['GET', 'POST'])
def inference():
    url = request.data.decode("utf-8")
    article = Article(url)
    article.download()

    article.parse()
    print(" __      CONTENT DATA  __ \n")
    print(article.text)
    print(" __          END       __ \n")
    
    texts  = article.text
    output =model.inference(texts) 
    

    result = [{"out" : o[1] , "attention" : o[0]} for  o in output]
    print("Result:")
    print(result)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
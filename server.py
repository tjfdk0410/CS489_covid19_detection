from flask import Flask, request, jsonify
from newspaper import Article
import random

app = Flask(__name__)

@app.route('/detect/', methods=['POST'])
def _get_data():
    print(request.data)
    url = request.data.decode("utf-8")
    article = Article(url)
    article.download()
    # print("\n\n******** HTML ******** \n\n")
    # print(article.html)
    article.parse()
    print("\n\n******** text ******** \n\n")
    print(article.text)

    # out = random.choice(["true", "fake"])
    result = {
        "out": False,
        "attention": [
            ("Vaccines generally work by introducing a piece of a virus or bacteria into your body so you can develop long-lasting immunity to the pathogen.", 0.95),
            ("When it encounters the virus or bacteria in the real world it mounts a strong immune response preventing or decreasing the severity of infection.", 0.73),
            ("The spike protein is located on the outside of a coronavirus and is how SARS-CoV-2 (the coronavirus) enters human cells.", 0.68),
            ("From brain fog to migraines to even stroke-like symptoms,", 0.75)
        ]
    };
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8123, debug=True)

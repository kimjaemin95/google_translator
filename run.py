# -*- coding:utf-8 -*-

from flask import Flask, render_template, request
from googletrans import Translator, LANGCODES


app = Flask(__name__)


@app.route("/")
def index():
    print('index 페이지 입니다.')
    return render_template('index.html')

@app.route("/translate", methods=["POST"])
def translate():
    text = request.form["text"]
    input_lang = request.form["input_lang"]
    output_lang = request.form["output_lang"]
    translator = Translator()
    trans_res = translator.translate(text=text, src=input_lang, dest=output_lang)
    trans_text = trans_res.text

    return trans_text




if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')















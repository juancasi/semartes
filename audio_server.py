#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:37:21 2018

@author: juancastro
"""

from flask import Flask, Response

app = Flask(__name__)

@app.route("/mp3")
def streammp3():
    def generate():
        with open("saludo.mp3", "rb") as fogg:
            data = fogg.read(1024)
            while data:
                yield data
                data = fogg.read(1024)
    return Response(generate(), mimetype="audio/mp3")

if __name__ == "__main__":
    app.run(debug=True)
    
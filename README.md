## About this app
Autor: Leonardo Tada

Simple crawler function that walk to all pages in the same domain and
search for assets useds. Return JSON string. This version has a default timeout of 5 minutes to not remain running indefinitely.
Written in Python 3.

This repository contains a webservice version of the crawler made by me at:
https://github.com/leotada/gecko-web-crawler

## Install requirements

```sh
pip3 install -r requirements.txt -U --user
```

## How to run

```sh
python3 app.py
```

## Make get request passing the url
```sh
http://0.0.0.0:8000/crawler/https://translate.google.com.br
```

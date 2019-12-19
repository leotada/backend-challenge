## The challenge

The idea is simple: create a *web crawler* from ground up, using any language you are confortable with.

## Suggested workflow

This crawler should only navigate in one domain, for example: pointing it to https://elixir-lang.org, it should walk for all pages on the domaing, but it shouldn`t go to Twitter, or the Language Forum.

Your crawler must print, as a result, a map, with a list of all the pages, and all the static assets (css, js, img) of every page.

You can choose how the result is gonna look like.

You get extra points for a faster crawler.

Fork this repo and send it back to us with your implementation.

## Bonus

You need to provide instructions on buildin and running your code.

**Have fun building!** 🚀


-------------

## About this app
Autor: Leonardo Tada

Simple crawler function that walk to all pages in the same domain and
search for assets useds. Return JSON string. This version has a default timeout of 5 minutes to not remain running indefinitely.

This repository contains a webservice version of the crawler made by me at:
https://github.com/leotada/gecko-web-crawler

## How to run

```sh
python app.py
```

## Make get request passing the url
```sh
http://0.0.0.0:8000/crawler/https://translate.google.com.br
```

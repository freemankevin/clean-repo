#! /usr/bin/python3

# -*- coding: utf-8 -*-


from time import sleep
import requests

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "X-OAuth-Scopes": "repo"
}

with open('./repos.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

url = "https://api.github.com/repos/{}/{}"
urls = []

for line in data:
    name, repo = line.strip().split("/")
    urls.append(url.format(name, repo))

for l in urls:
    requests.delete(url=l, headers=headers)
    sleep(2)

import json
import requests


def process_text(text):
    headers = {'Content-Type': 'text/plain;charset=utf-8'}
    params = {
        "task": "nakdan",
        "genre": "modern",
        "data": text,
        "addmorph": True,
        "matchpartial": True,
        "keepmetagim": False,
        "keepqq": False,
    }
    r = requests.post("https://nakdan-4-0.loadbalancer.dicta.org.il/addnikud", headers=headers, json=params)
    r.encoding = "UTF-8"
    x = json.loads(r.text)
    ds = []
    for item in x:
        y = {}
        if ('word' in item) and item['sep'] is False:
            y['word'] = item['word']
        for inner in item['options']:
            y['morph'] = '0x{0:0{1}X}'.format(int(inner['morph']), 16)
        if len(y) > 0:
            ds.append(y)
    return filter_words(ds)


def is_female(item):
    return item['morph'][12] == '4' or item['morph'][12] == '5'


def is_adj(item):
    return item['morph'][13] == '1'


def is_talking_about_noun(items, start, end):
    for i in range(start, end):
        if items[i]['morph'][13] == '6':
            return True
    return False


def filter_words(items):
    out = set()
    for i in range(len(items)):
        j = i
        # checking if the adjective is talking about female or noun
        if j <= 3:
            j = 0
        else:
            j = j - 3
        if is_adj(items[i]) and is_female(items[i]) and (not is_talking_about_noun(items, j, i)):
            out.add(items[i]['word'])
    return out


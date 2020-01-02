from django.shortcuts import render
import json
import pandas as pd
import csv


# csvファイル3つ結合スクリプトかく

def on_process(request):
    json_list = []
    with open('on_process.csv', 'r') as f:
        for row in csv.DictReader(f):
            json_list.append(row)


    with open('./on_process/templates/on_process/output.json', 'w') as f:
        json.dump(json_list, f)

    return render(request, 'on_process/output.json', {})

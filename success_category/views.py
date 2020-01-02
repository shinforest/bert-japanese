from django.shortcuts import render
import json
import pandas as pd
import csv
import os
from django.http import HttpResponse
import zipfile
from django.http import FileResponse

# csvファイル3つ結合スクリプトかく
from django.db import models
from django.views import generic



def success_category(request)

    path = "media"
    files_names = os.listdir(path)
    print(files_names)



    zip_path = 'media/new_comp.zip'
    file_paths = []
    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
        for file in files_names:
            file_path = os.path.join("media", file)
            new_zip.write(file_path)
            # file_paths.append(file_path)


    if os.path.exists(zip_path):
        zip_file = open(zip_path, 'rb')
        return FileResponse(zip_file)
        # response = HttpResponse(zip_file, content_type='application/force-download')
        # response['Content-Disposition'] = 'attachment; filename="%s"' % 'foo.zip'
        # return response
        # with open(zip_path, 'rb') as fh:
        #     response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        #     response['Content-Disposition'] = 'inline; filename=' + os.path.basename(zip_path)
        #     return response


    # content = 'body1'
    # response = HttpResponse(content, content_type='text/plain')
    # # response['Content-Disposition'] = 'attachment; filename="output.json"'
    # response['Content-Disposition'] = 'attachment; filename=\"'+ file +'\"'
    # return response
    # print ('カテゴリーが認識されたよ')
    # os.getcwd()
    # path = "./success_category/templates/success_category/media"
    # print(path)
    # files_names = os.listdir(path)
    # print(files_names)
    # file_paths = []
    # for file in files_names:
    #     file_path = os.path.join("media", file)
    #     file_paths.append(file_path)
    #
    # #
    # # else:
    #
    # return render(request, 'success_category/success_category.html', {"file_paths":file_paths})
    #


from django.http import HttpResponse
def download(file):
    content = 'body1'
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=\"'+ file +'\"'
    return response

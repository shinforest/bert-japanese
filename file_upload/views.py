from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
import os
import sys
import shutil
import pandas as pd


from django.db import models






# ------------------------------------------------------------------
def file_upload(request):
    shutil.rmtree("./on_process.csv")
    cols = ['Task', 'Remaining Time']
    df = pd.DataFrame(index=[], columns=cols)
    df.to_csv("on_process.csv",header=True, index=False)
    shutil.rmtree("./media")
    os.makedirs('./media',exist_ok=True)

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            folder_path = "./project_name/"+request.POST['project']+'/input/input_data'
            os.makedirs(folder_path)
            sys.stderr.write("*** file_upload *** aaa ***\n")
            handle_uploaded_file(request.FILES['file'], request.POST['project'])
            file_obj = request.FILES['file']
            handle_uploaded_post(request.POST['column'], request.POST['project'])
            column_obj = request.POST['column']
            sys.stderr.write(file_obj.name + "\n")
            handle_uploaded_project(request.POST['project'])
            project_obj = request.POST['project']
            # handle_uploaded_datatype(request.POST.get('data_type'))
            if request.POST.get('data_type') == "category":
                os.system('bash data_sort.sh '+project_obj)
                return HttpResponseRedirect('/success_category')

            else:
                os.system('bash data_sort_n.sh '+project_obj)
                return HttpResponseRedirect('/success_numeric/url/')
            # data_type = request.POST['data_type']
            # print(data_type)
            #
            # return HttpResponseRedirect('/success_category/url/')

    else:
        form = UploadFileForm()
    return render(request, 'file_upload/upload.html', {'form': form})
#
#
# ------------------------------------------------------------------
# def download_list():
#     path = "./media"
#     files_names = os.listdir(path)
#     files = []
#     for file in files_names:
#         file_path = os.path.join(path, file)
#         files.append(file_path)


def handle_uploaded_file(file_obj, project_name):
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    sys.stderr.write(file_obj.name + "\n")
    file_path = "./project_name/"+project_name+'/input/input_data/' + file_obj.name
    sys.stderr.write(file_path + "\n")
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            sys.stderr.write("*** handle_uploaded_file *** ccc ***\n")
            destination.write(chunk)
            sys.stderr.write("*** handle_uploaded_file *** eee ***\n")

def handle_uploaded_post(column_obj, project_name):
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    file_path = "./project_name/"+project_name+'/input/column_names.txt'
    sys.stderr.write(file_path + "\n")
    with open(file_path, mode='w') as destination:
        sys.stderr.write("*** handle_uploaded_post *** ccc ***\n")
        destination.write(column_obj)
        sys.stderr.write("*** handle_uploaded_post *** eee ***\n")


def handle_uploaded_project(project_obj):
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    file_path = "./project_name/"+project_obj+'/input/project_name.txt'
    sys.stderr.write(file_path + "\n")
    with open(file_path, mode='w') as destination:
        sys.stderr.write("*** handle_uploaded_post *** ccc ***\n")
        destination.write(project_obj)
        sys.stderr.write("*** handle_uploaded_post *** eee ***\n")

def handle_analysis_mode(analysis_obj):
    print(something)
# ------------------------------------------------------------------
def success_category(request):
    print ('カテゴリーが認識されたよ')
    os.getcwd()
    path = "./media"
    print(path)
    files_names = os.listdir(path)
    str_out = "Data Uploaded!!!!!!<p />"
    str_out += "データアップロード成功!!!!<p />"
    print(files_names)
    for file in files_names:
        file_path = os.path.join(path, file)
        print(file_path)
        str_out += '<li><a href="'+ file_path + '">' + file + "</a></li>"

    #
    # else:
    print(str_out)
    return HttpResponse(str_out)
    # ------------------------------------------------------------------




def success_numeric(request):
    project_obj = request.POST['project']
    print ('数値が認識されたよ')


    #     str_out = "カテゴリー"
    #
    # else:
    str_out = "Data Uploaded!!!!!!<p />"
    str_out += "データアップロード成功!!!!<p />"
    return HttpResponse(str_out)

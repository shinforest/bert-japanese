from django import forms
import os
from django.contrib import messages



# DATA_CHOICES =(('category':'カテゴリー'),('numeric':'数値'))

ANALYSIS_CHOICES = (
      ('classification', 'クラス分け'),
      ('named_entity', '固有表現抽出'),


)

DATA_CHOICES = (
    ('category', 'カテゴリー型'),
    ('num', '数値型')
)

class UploadFileForm(forms.Form):
    analysis_type = forms.ChoiceField(
        label='分析手法',
        widget=forms.RadioSelect,
        choices=ANALYSIS_CHOICES,
        required=True,

    )
    project = forms.CharField(label='プロジェクト')
    file = forms.FileField(label='解析したいファイル')
    column = forms.CharField(label='解析したい列名',max_length=50)
    data_type = forms.ChoiceField(
        label='データのタイプ',
        widget=forms.RadioSelect,
        choices=DATA_CHOICES,
        required=True,

    )
    def clean_project(self):
        list = os.listdir("./project_name")
        project = self.cleaned_data['project']
        if project in list:
            del project
            raise forms.ValidationError("・・・ERROR:すでに存在するプロジェクト名です:ERROR・・・・")
        else:
            return project

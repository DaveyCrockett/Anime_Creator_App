from django import forms


class UploadedFileForm(forms.Form):
    video = forms.FileField()
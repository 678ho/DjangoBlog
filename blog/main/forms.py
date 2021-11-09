from django import forms
from .models import Write
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class WriteForm(forms.ModelForm) :
    class Meta :
        model = Write
        fields = ['title', 'contents']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'content': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '내용을을 입력하세요.'}
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }
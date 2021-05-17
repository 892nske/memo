from django.forms import ModelForm
from .models import Memo, Tags


class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'text']


class NewTagForm(ModelForm):
    class Meta:
        model = Tags
        fields = ['tag']
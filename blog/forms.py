from django import forms
from .models import Comment
from mptt.forms import TreeNodeChoiceField

class NewCommentForm(forms.ModelForm):
    parent=TreeNodeChoiceField(queryset=Comment.objects.all())

    #TODO we have to remove required parent field

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['parent'].required=False

    class Meta:
        model = Comment
        fields = ('name', 'parent' ,'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'email': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


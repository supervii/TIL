from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10, 
#         label = '제목',
#         widget = forms.TextInput(attrs={
#             'class':'my-title',
#             'placeholder': 'Enter the Title'
#             }
#         )
#     )
#     content = forms.CharField(
#         label= '내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class':'my-content',
#                 'placeholder': 'Enter the Content',
#                 'rows': 5,
#                 'cols': 50
#             }
#         )
#     )


class ArticleForm(forms.ModelForm):
    title= forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'Enter the Title',
            }
        )
    )
    content = forms.CharField(
        label= '내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder': 'Enter the Content',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    
    class Meta:
        model = Article
        fields = ('title','content',)
        # fields = '__all__'
        # exclude = ('title',)  제외해주기 
        # widgets ={
        #     'title' : forms.TextInput(attrs={}

        #     )
        # }

class CommentForm(forms.ModelForm):
        
    class Meta:
        model = Comment
        fields = ('content',)

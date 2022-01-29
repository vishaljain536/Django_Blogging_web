from django import forms
from .models import Post
from  ckeditor.fields import RichTextFormField

class BlogsForm(forms.ModelForm):
    '''
      Forms for Blogs
    '''
    class Meta:
         model=Post
         fields='__all__'
         widgets={
             'blog_title':forms.TextInput(attrs={'class':'form-control','placeholder':'Blog Title'}),
             # 'blog_description':forms.Textarea(attrs={'class':'form-control','placeholder':'Blog Description'}),
             'blog_description':RichTextFormField(),
             # 'categories':forms.Select(choices={'class':'form-control','placeholder':'Categories'}),

         }
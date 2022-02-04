from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from.Forms import BlogsForm,SignUpForm
from.models import Post
from django.contrib import messages


# Create your views here.
def Login(request):
    '''
    Login page
    '''
    url="Login.html"
    if request.method=="POST":
          username=request.POST.get('username')
          password=request.POST.get('password')
          user=auth.authenticate(username=username,password=password)
          if user is not None:
              auth.login(request,user)
              return redirect('blogapp:blog')
          else:
              messages.warning(request,"Not a valid user Pls singup")
              return redirect('blogapp:login')

    return render(request,url)


def Logout(request):
    '''
    Logout
    '''
    auth.logout(request)
    return redirect('blogapp:login')

def Signup(request):
    '''
         Signup page
    '''
    url="Sign_Up.html"
    form=SignUpForm()
    if request.method=='POST':
        form=form=SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('blogapp:login')
        else:
            return redirect('blogapp:signup')

    return render(request,url,{'form':form})




def Index(request):
   print(request.user)
   return render(request,"Index.html")

@login_required(login_url='blogapp:login')
def Blog(request):
   '''
     Blog Regitartion
   '''
   form=BlogsForm()
   if request.method=='POST':
      form=BlogsForm(request.POST)
      if form.is_valid:
           form.save()
           messages.success(request,"Succesfully new blog Created")
           return render(request,"Blog.html")
      else:
          messages.warning(request,"Error Blog Creating")
          return render(request, "Blog.html")
   return render(request,"Blog.html",{'form':form})

@login_required(login_url='blogapp:login')
def Blog_List(request):
    blogs=Post.objects.all()
    return render(request,"Blog_List.html",{'blogs':blogs})

# def Blog_Submit(request):
#    try:
#     picture =request.POST['picture']
#     filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]
#     F = open("D:/Blog/media/" + filename, "wb")
#     for chunk in picture.chunks():
#         F.write(chunk)
#     F.close()
#     return render(request, "Blog.html")
#    except Exception as e:
#        print("Error:", e)
#        return render(request, "Blog.html")

@login_required(login_url='blogapp:login')
def Blog_Page(request,id):
    blogs=Post.objects.get(id=int(id))
    return render(request,"Blog_Page.html",{'blogs':blogs})

@login_required(login_url='blogapp:login')
def Blog_Delete(request,id):
    blogs=Post.objects.get(id=int(id))
    blogs.delete()
    blogs = Post.objects.all()
    return render(request, "Blog_List.html", {'blogs': blogs})

@login_required(login_url='blogapp:login')
def Blog_Update(request,id):
   '''
     Blog  Update
   '''
   Posts=Post.objects.get(id=int(id))
   data={
       'blog_title':Posts.blog_title,
       'blog_description':Posts.blog_description,
       'author':Posts.author,
       'published':Posts.published,

   }
   form=BlogsForm(initial=data)
   if request.method=='POST':
      form=BlogsForm(request.POST,instance=Posts)
      if form.is_valid:
           form.save()
           messages.success(request,"Succesfully Updated Blog Deatils")
           return render(request,"Blog_Update.html")
      else:
          messages.warning(request,"Submission update failed")
          return render(request, "Blog_Update.html")
   return render(request,"Blog_Update.html",{'form':form})

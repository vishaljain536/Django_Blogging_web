
from django.urls import path,include
from. import views
app_name='blogapp'
urlpatterns = [
    path('',views.Index,name='home'),
    path('blog/', views.Blog, name='blog'),
    path('blog_list/', views.Blog_List, name='blog_list'),
    path('blog_page/<int:id>', views.Blog_Page, name='blog_page'),
    path('blog_update/<int:id>', views.Blog_Update, name='blog_update'),
    path('blog_delete/<int:id>', views.Blog_Delete, name='blog_delete'),
]

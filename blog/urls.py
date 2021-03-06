from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.Indexview.as_view(), name='home'),
    path('blog/<int:id>/<slug:slug>/', views.detailview, name='detail'),
    path('likes/', views.PostLike, name='Like'),
    path('<int:id>/DeleteComment/', views.CommentDelete, name='DeleteComment'),
    path('<int:id>/<str:category>/', views.Category_List, name='category'),
    path('Contact/', views.Contact, name="Contact"),
    path('About/CollegeBlog/', views.AboutPage, name="About"),
]

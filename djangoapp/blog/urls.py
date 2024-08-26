from django.urls import path
from blog.views import index, page, post, category, created_by, tag, search

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('category/<slug:slug>/', category, name='category'),
    path('created_by/<int:author_pk>/', created_by, name='created_by'),
    path('page/<slug:slug>/', page, name='page'),
    path('tag/<slug:slug>/', tag, name='tag'),
    path('search/<slug:slug>/', search, name='search'),
]

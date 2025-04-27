from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),  # Home page view with random blogs and documentation links
    path('about', views.about, name='about'),  # About page
    path('contact', views.contact, name='contact'),  # Contact page
    path('blog', views.blog, name='blog'),  # Blog page with pagination
    path('projects', views.projects, name='projects'),  # Projects page
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),  # Single blog post
    path('category/<str:category>', views.category, name='category'),  # Category page
    path('categories/', views.categories, name='categories'),  # List of all categories
    path('search/', views.search, name='search'),  # Search page
    path('thanks', views.thanks, name='thanks'),  # Thank you page after successful contact
]

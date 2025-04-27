from django.shortcuts import render
from django.core.paginator import Paginator
from home.models import Blog
import random
import re
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Q


# Home page view with random blogs and pagination for Data Engineering documentation
def index(request):
    # Example documentation links (Data Engineering tools)
    documentation_links = [
        {"title": "Django Documentation", "url": "https://docs.djangoproject.com/en/stable/"},
        {"title": "AWS Documentation", "url": "https://docs.aws.amazon.com/"},
        {"title": "Snowflake Documentation", "url": "https://docs.snowflake.com/en/"},
        {"title": "Apache Spark Documentation", "url": "https://spark.apache.org/docs/latest/"},
        {"title": "Databricks Documentation", "url": "https://docs.databricks.com/"},
        {"title": "Kafka Documentation", "url": "https://kafka.apache.org/documentation/"},
        {"title": "Airflow Documentation", "url": "https://airflow.apache.org/docs/"},
        {"title": "Google Cloud Documentation", "url": "https://cloud.google.com/docs"},
        {"title": "Azure Data Engineering Documentation",
         "url": "https://learn.microsoft.com/en-us/azure/data-engineering/"},
        {"title": "PostgreSQL Documentation", "url": "https://www.postgresql.org/docs/"},
        # Add more links here...
    ]

    # Pagination for documentation links
    paginator = Paginator(documentation_links, 3)  # Show 3 links per page
    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the paginated documentation links

    # Fetch random 3 blogs for the homepage
    blogs = Blog.objects.all()
    random_blogs = random.sample(list(blogs), 3)

    # Pass the data to the template for rendering
    context = {'random_blogs': random_blogs, 'page_obj': page_obj}
    return render(request, 'index.html', context)


# About page view
def about(request):
    return render(request, 'about.html')


# Thank you page view (redirected after successful contact)
def thanks(request):
    return render(request, 'thanks.html')


# Contact page view (form submission)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        invalid_input = ['', ' ']

        # Check if fields are empty
        if name in invalid_input or email in invalid_input or phone in invalid_input or message in invalid_input:
            messages.error(request, 'One or more fields are empty!')
        else:
            # Regex patterns for email and phone validation
            email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            phone_pattern = re.compile(r'^[0-9]{10}$')

            if email_pattern.match(email) and phone_pattern.match(phone):
                form_data = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'message': message,
                }
                # Prepare the email message
                email_message = '''
                From:\n\t\t{}\n
                Message:\n\t\t{}\n
                Email:\n\t\t{}\n
                Phone:\n\t\t{}\n
                '''.format(form_data['name'], form_data['message'], form_data['email'], form_data['phone'])
                send_mail('You got a mail!', email_message, '', ['dev.ash.py@gmail.com'])
                messages.success(request, 'Your message was sent.')
            else:
                messages.error(request, 'Email or Phone is Invalid!')
    return render(request, 'contact.html', {})


# Projects page view
def projects(request):
    return render(request, 'projects.html')


# Blog page view (list of all blog posts with pagination)
def blog(request):
    blogs = Blog.objects.all().order_by('-time')
    paginator = Paginator(blogs, 3)  # 3 blogs per page
    page = request.GET.get('page')  # Get the current page number from the URL
    blogs = paginator.get_page(page)  # Get the paginated blog posts
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)


# Category page view (display blogs of specific category with pagination)
def category(request, category):
    category_posts = Blog.objects.filter(category=category).order_by('-time')
    if not category_posts:
        message = f"No posts found in category: '{category}'"
        return render(request, "category.html", {"message": message})

    paginator = Paginator(category_posts, 3)  # 3 blogs per page
    page = request.GET.get('page')
    category_posts = paginator.get_page(page)
    return render(request, "category.html", {"category": category, 'category_posts': category_posts})


# Categories page view (list of all categories)
def categories(request):
    all_categories = Blog.objects.values('category').distinct().order_by('category')
    return render(request, "categories.html", {'all_categories': all_categories})


# Search page view (search blog posts based on query)
def search(request):
    query = request.GET.get('q')  # Get the search query
    query_list = query.split()  # Split query into words
    results = Blog.objects.none()  # Start with an empty result set
    for word in query_list:
        results = results | Blog.objects.filter(Q(title__contains=word) | Q(content__contains=word)).order_by('-time')
    paginator = Paginator(results, 3)  # 3 results per page
    page = request.GET.get('page')
    results = paginator.get_page(page)
    message = "Sorry, no results found for your search query." if len(results) == 0 else ""
    return render(request, 'search.html', {'results': results, 'query': query, 'message': message})


# Single blog post view (displays a specific blog post)
def blogpost(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)  # Get the blog post by slug
        context = {'blog': blog}
        return render(request, 'blogpost.html', context)
    except Blog.DoesNotExist:
        context = {'message': 'Blog post not found'}
        return render(request, '404.html', context, status=404)

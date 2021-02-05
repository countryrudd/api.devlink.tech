from django.shortcuts import render

from blog.views import get_blog_querylist
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

BLOG_POSTS_PER_PAGE = 5

def home_screen_view(request):
    # context = {
    #   'some_string': "This is some string that i m passing to the view",
    #  'some_number': 3273537
    # }
    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q', "")
        context['query'] = str(query)
    #   list_of_values = ['first entry', 'second entry', 'third entry', 'fourth entry']
    #  context['list_of_values'] = list_of_values
    blog_posts = sorted(get_blog_querylist(query), key=attrgetter('date_updated'), reverse=True)

    # pagination
    page = request.GET.get("page", 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger :
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

    return render(request, "personal/home.html", context)

from django.shortcuts import render


def blog(request):
    return render(request, 'blog.html')

def index(request):
    return render(request, 'index.html')

def index_2(request):
    return render(request, 'index-2.html')

def index_3(request):
    return render(request, 'index-3.html')

def index_4(request):
    return render(request, 'index-4.html')

def inner_page(request):
    return render(request, 'inner-page.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def blog_details(request):
    return render(request, 'blog-details.html')
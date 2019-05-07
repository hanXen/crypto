from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, 'blog/index.html')

def about_page(request):
    return render(request, 'blog/about.html')

def research_page(request):
    return render(request, 'blog/research.html')

def member_page(request):
    return render(request, 'blog/member.html')

def notice_page(request):
    return render(request, 'blog/notice.html')

def contact_page(request):
    return render(request, 'blog/contact.html')

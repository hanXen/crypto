from django.shortcuts import render
from .models import Announce, Member

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
    announces = Announce.objects.all().order_by('published_date')

    return render(request, 'blog/notice.html', {'announces': announces})

def contact_page(request):
    return render(request, 'blog/contact.html')

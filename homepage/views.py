from django.shortcuts import render, get_object_or_404
from .models import Logo, Blog


def home_page_view(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})


def engagements_view(request):
    return render(request, 'engagements.html')


def logo_view(request):
    logos = Logo.objects.all()
    return render(request, 'index.html', {'logos': logos})


def detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'detail.html', {'blog': blog})

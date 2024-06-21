from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Blog, UserComment
from .forms import UserCommentForm


def home_page_view(request):
    blogs = Blog.objects.all()
    form = UserCommentForm()
    if request.method == 'POST':
        form = UserCommentForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            user_comment = UserComment(
                first_name=cleaned['first_name'],
                last_name=cleaned['last_name'],
                email=cleaned['email'],
                website=cleaned['website'],
                message=cleaned['message'],
            )
            user_comment.save()
            return JsonResponse({
                'message': 'success'
            })
    else:

        context = {'blogs': blogs,
                   'form': form}
        return render(request, 'homepage.html', context)


def engagements_view(request):
    return render(request, 'engagements.html')


def detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {'blog': blog}
    return render(request, 'detail.html', context)

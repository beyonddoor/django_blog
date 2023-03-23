from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.
def index(request):
    latest_question_list = Post.objects.order_by('-date_posted')[:5]
    
    context = {
        'posts': latest_question_list,
    }
    return render(request, 'posts/index.html', context)


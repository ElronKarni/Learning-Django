from multiprocessing import context
from django.shortcuts import render
from .forms import ArticleForm
from .models import Article
# Create your views here.


def create_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()

    context = {
        "form": form,
    }
    return render(request, 'blog/article_create.html', context)



def article_list(request):
    queryset = Article.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'blog/article_list.html', context)
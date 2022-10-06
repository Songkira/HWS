# views.py
def detail(request, __(a)__):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context_data = {
        'article': article,
        __(b)__,
        'comments':comments,
    }
    return render(request, 'eithers/detail.html', __(c)__)

a => article_pk
b => 'comment_form':comment_form,
c => context_data

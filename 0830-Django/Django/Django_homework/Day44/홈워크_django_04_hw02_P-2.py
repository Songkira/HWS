def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    # return render(request,'articles/index.html')
    return redirect('articles:index')
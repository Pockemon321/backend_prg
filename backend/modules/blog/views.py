class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/articles_detail.html'
    context_object_name = 'article'
    queryset = model.objects.detail()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['form'] = CommentCreateForm
        return context
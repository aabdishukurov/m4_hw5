from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic



class WatchShopView(generic.ListView):
    template_name = 'watches/shop.html'
    queryset = models.Shop.objects.all()

    def get_queryset(self):
        return models.Shop.objects.all()

class WatchShopDetailView(generic.DetailView):
    template_name = 'watches/watch_detail.html'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Shop, id=show_id)

class AddTvShowView(generic.CreateView):
    template_name = 'watches/crud/create_watch.html'
    form_class = forms.WatchShopForm
    queryset = models.Shop.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(AddTvShowView, self).form_valid(form=form)


class DeleteWatchShopView(generic.DeleteView):
    template_name = 'watches/crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Shop, id=show_id)


class UpdateWatchShopView(generic.UpdateView):
    template_name = 'watches/crud/update_watch.html'
    form_class = forms.WatchShopForm
    success_url = '/'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Shop, id=show_id)

    def form_valid(self, form):
        return super(UpdateWatchShopView, self).form_valid(form=form)

def Comment_View(request):
    comment = models.Comment.objects.all()
    return render(request, 'watch_detail.html', {'comment_key': comment})

class Search(generic.ListView):
    template_name = 'watches/shop.html'
    context_object_name = 'watch'
    paginate_by = 5

    def get_queryset(self):
        return models.Shop.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context




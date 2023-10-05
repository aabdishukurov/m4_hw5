from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from . import forms

class RegistrationView(CreateView):
    form_class = forms.RegistraionNewForm
    #form_class = UserCreationForm
    success_url = '/users/'
    template_name = 'registration/registration.html'

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('users:user_list')

class UserListView(ListView):
    queryset = User.objects.all()
    template_name = 'registration/user_list.html'

    def get_queryset(self):
        return User.objects.all()



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


class Search(generic.ListView):
    template_name = 'watches/shop.html'
    context_object_name = ('watches')
    paginate_by = 5

    def get_queryset(self):
        return models.Shop.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context




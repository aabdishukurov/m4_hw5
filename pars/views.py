from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView
from . import models, parser, forms


class ParserFilmListView(ListView):
    model = models.Cinema
    template_name = 'parser/film_list.html'

    def get_queryset(self):
        return models.Cinema.objects.all()



class ParserFormView(FormView):
    template_name = 'parser/start_parse.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Данные успешно взяты.......')
        else:
            return super(ParserFormView).post(request, *args, *kwargs)
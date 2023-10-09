from django.urls import path
from . import views

urlpatterns = [
    path('film-list/', views.ParserFilmListView.as_view(), name='film_list'),
    path('start_parsing/', views.ParserFormView.as_view(), name='start_pars'),
]
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index),
    # ex: /polls/5/
    path('<int:poll_id>', views.detail),
    # ex: /polls/5/results/
    path('<int:poll_id>/results/', views.results),
    # ex: /polls/5/vote/
    path('<int:poll_id>/vote/', views.vote),
]

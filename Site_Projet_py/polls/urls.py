from django.urls import path
from .views import LobbyView
from . import views

app_name = "polls"
urlpatterns = [
    path("", LobbyView.as_view(), name='lobby'),
    path("test",views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),



    path("knn", views.index_p, name="knn"),
    path("page1", views.index_1, name="page1"),
    path("apply_Model", views.index_2, name="apply_Model"),


    path("proj",views.index_proj, name="proj"),
    path("code",views.code, name="code" )
]
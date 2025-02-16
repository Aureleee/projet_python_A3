from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

from django.views.generic import TemplateView

class IndexView(generic.ListView):
    template_name = "template0.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]

class LobbyView(TemplateView):
    template_name = "lobby.html"
    



class DetailView(generic.DetailView):
    model = Question
    template_name = "template1.html"
    def get_queryset(self):
       """
       Excludes any questions that aren't published yet.
       """
       return Question.objects.filter(pub_date__lte=timezone.now())



class ResultsView(generic.DetailView):
    model = Question
    template_name = "template2.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "template1.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



# PARTIE KNN ( de Safwan CHENDEB)
    

from django.http import HttpResponse
import pandas as pd

from django.template import loader

from django.shortcuts import render


import plotly.express as px

from  sklearn.neighbors import KNeighborsClassifier
from  sklearn.model_selection import train_test_split

#
from sklearn.cluster import KMeans




def index_p(request):
    data = pd.read_csv(r"C:\Users\aurel\Desktop\DATA_IRIS.txt", names=['sl','sw','pl','pw','label'])
    iris_classes=data.label.unique()
    #template = loader.get_template("template0.html")
    
    fig = px.scatter(data, x='pw',y='pl',color = 'label',size='sl',hover_data=['pw'])

    plot_html=fig.to_html(full_html=False,default_height=500,default_width=700 )

    context ={
        'les_labels_iris':iris_classes,
        'plot_html':plot_html
        }
    return render(request, "KNN/template0KNN.html", context)

def index_1(request):
    data = pd.read_csv(r"C:\Users\aurel\Desktop\DATA_IRIS.txt", names=['sl','sw','pl','pw','label'])
    iris_classes=data.label.unique()
    #template = loader.get_template("template0.html")
    
    fig = px.scatter(data, x='pw',y='pl',color = 'label',size='sl',hover_data=['pw'])

    plot_html=fig.to_html(full_html=False,default_height=500,default_width=700 )

    context ={
        'les_labels_iris':iris_classes,
        'plot_html':plot_html
        }
    return render(request, "KNN/template1KNN.html", context)

def KnnOnIris():
    data = pd.read_csv(r"C:\Users\aurel\Desktop\DATA_IRIS.txt", names=['sl', 'sw', 'pl', 'pw', 'label'])
    iris_classes = data.label.unique()
    data['label'].replace(
        iris_classes,
        [0, 1, 2],
        inplace=True
    )
    X = data.drop(columns=['label']).values
    y = data['label'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = KNeighborsClassifier(n_neighbors=3) # création d'un modèle paramétré
    model.fit(X_train, y_train) # entraîner le modèle avec le dataset du training
    y_pred = model.predict(X_test)

    dataknn = pd.DataFrame(X_test, columns=['sl', 'sw', 'pl', 'pw'])
    dataknn['label'] = y_test
    dataknn['pred_label'] = y_pred
    fig = px.scatter(dataknn, x="pw", y="pl", color="label", size="pl", hover_data=['pw'], facet_col="pred_label")
    
    fig.update_layout(title="KNN Applied", xaxis_title="Petal Length", yaxis_title="Petal Width")
    plot_html = fig.to_html(full_html=False, default_height=500, default_width=700)
    return plot_html

def KMeansOnIris():
    data = pd.read_csv(r"C:\Users\aurel\Desktop\DATA_IRIS.txt", names=['sl', 'sw', 'pl', 'pw', 'label'])
    iris_classes = data.label.unique()
    data['label'].replace(
        iris_classes,
        [0, 1, 2],
        inplace=True
    )
    X = data.drop(columns=['label']).values
    y = data['label'].values
    model = KMeans(3, random_state=223)
    model.fit(X)
    pred_label = model.predict(X)
    data['pred_label'] = pred_label
    fig = px.scatter(data, x="pw", y="pl", color="label", 
                     size="pl", hover_data=['pw'], facet_col="pred_label")
    fig.update_layout(title="KMeans Applied", xaxis_title="Petal Length", yaxis_title="Petal Width")
    plot_html = fig.to_html(full_html=False, default_height=500, default_width=700)
    return plot_html




def index_2(request):
    template = loader.get_template('KNN/template1KNN.html')
    if(request.GET['model']=="KNN"):
        plot_html=KnnOnIris()
    if(request.GET['model']=="KMeans"):
        plot_html=KMeansOnIris




    context ={
        'plot_html':plot_html
        }
    return HttpResponse(template.render(context,request))




#Projet python


def index_proj(request):
    
    return render(request, "PROJ/temp_Projet.html")

def code(request):

    return render(request, "PROJ/temp_code.html")

def extraction_data():
    

    return 








































from django.urls import path
from . import views

urlpatterns = [
    path('', views.startQuiz),
    path('quiz',views.actualQuiz, name='quiz'),
    path('quiz2',views.actualQuiz2),
    path('quiz3',views.actualQuiz3),
    path('quiz4',views.actualQuiz4),
    path('fetchValue', views.fetch_value, name='fetch_value'),
    path('fetchValue2', views.fetch_value2, name='fetch_value2'),
    path('fetchValue3', views.fetch_value3, name='fetch_value3'),
    path('fetchValue4', views.fetch_value4, name='fetch_value4'),
    path('analyzeResult',views.analyzeResult,name='analyzing')
]

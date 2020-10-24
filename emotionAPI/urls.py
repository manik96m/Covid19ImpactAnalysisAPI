from django.urls import path
from . import views
from . import EmotionController

urlpatterns = [

    path('',views.getScore,name='home'),
    path('start',EmotionController.start,name='start')

]
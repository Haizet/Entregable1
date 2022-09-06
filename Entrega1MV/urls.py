from unicodedata import name
from django.urls import path
from Entrega1MV.views import home, user_create, user_info,topics,create_topics

urlpatterns = [
   path('', home),
   path('user_create/', user_create, name='Entrega1MVUserCreate'),
   path('user_info/', user_info, name='Entrega1MVUserInfo'),
   path('topics/', topics, name='Entrega1MVTopics'),
   path('topics_create/', create_topics, name='Entrega1MVCreateTopics')
]
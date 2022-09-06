from unicodedata import name
from django.urls import path
from Entrega1MV.views import home, userCreate, user_info,topics,create_topics,posts,create_posts,busqueda_usuario

urlpatterns = [
   path('', home, name = 'Entrega1MVInicio'),
   path('userCreate/', userCreate, name='Entrega1MVUserCreate'),
   path('user_info/', user_info, name='Entrega1MVUserInfo'),
   path('topics/', topics, name='Entrega1MVTopics'),
   path('topics_create/', create_topics, name='Entrega1MVCreateTopics'),
   path('posts/', posts, name='Entrega1MVPost'),
   path('topics_create/', create_posts, name='Entrega1MVCreateTopics'),
   path('busqueda_usuario/', busqueda_usuario, name='Entrega1MVUserSearch')
]
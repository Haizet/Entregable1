from unicodedata import name
from django.urls import path
from Entrega1MV.views import UserList, about, home, userCreate,topics,create_topics,posts,create_posts,busqueda_usuario,busqueda_usuario_get,busqueda_tema,busqueda_tema_get,busqueda_post,busqueda_post_get


urlpatterns = [
   path('', home, name = 'Entrega1MVInicio'),
   path('userCreate/', userCreate, name='Entrega1MVUserCreate'),
   path('user_info/', UserList.as_view(), name='Entrega1MVUserInfo'),
   path('topics/', topics, name='Entrega1MVTopics'),
   path('topics_create/', create_topics, name='Entrega1MVCreateTopics'),
   path('posts/', posts, name='Entrega1MVPost'),
   path('post_create/', create_posts, name='Entrega1MVCreateTopics'),
   path('busqueda_usuario/', busqueda_usuario, name='Entrega1MVUserSearch'),
   path('busqueda_usuario_get/', busqueda_usuario_get, name='Entrega1MVUserSearchGet'),
   path('busqueda_tema/', busqueda_tema, name='Entrega1MVSubjectSearch'),
   path('busqueda_tema_get/', busqueda_tema_get, name='Entrega1MVSubjectSearchGET'),
   path('busqueda_post/', busqueda_post, name='Entrega1MVPostSearch'),
   path('busqueda_post_get/', busqueda_post_get, name='Entrega1MVPostSearchGET'),
   path('about/', about, name = 'About'),

   # path('user_delete/<str:user_name>', user_delete, name = 'Entrega1MVUserDelete' ),
   # path('user_edit/ <str:user_name>', user_edit, name =  'Entrega1MVUserEdit')
]
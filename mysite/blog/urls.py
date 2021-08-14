from django.urls import path
from .views import *

urlpatterns = [
    path('create_category/', CategoryCreateView.as_view()),
    path('update_category/<int:pk>', CategoryUpdateView.as_view()),
    path('list_category/', CategoryListView.as_view()),
    path('destroy_category/<int:pk>', CategoryDestroyView.as_view()),
    path('create_tovary/', TovaryCreateView.as_view()),
    path('update_tovary/<int:pk>', TovaryUpdateView.as_view()),
    path('list_tovary/', TovaryListView.as_view()),
    path('destroy_tovary/<int:pk>', TovaryDestroyView.as_view()),
    path('create_coment/', ComentCreateView.as_view()),
    path('update_coment/<int:pk>', ComentUpdateView.as_view()),
    path('list_coment/', ComentListView.as_view()),
    path('destroy_coment/<int:pk>', ComentDestroyView.as_view()),   
]
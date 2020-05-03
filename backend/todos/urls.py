from django.urls import path
from .views import TodoList, TodoDetail
urlpatterns = [
    path('todos/<int:pk>', TodoDetail.as_view()),
    path('todos/', TodoList.as_view())
]
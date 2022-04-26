from django.urls import path
from todoapp import views


urlpatterns=[
    path("todos",views.TodoCreateView.as_view()),
    path("todos/<int:id>",views.TodoDetail.as_view()),
    path("mtodos",views.TodoMixinList.as_view()),
    path("mtodos/<int:id>",views.TodoMixinDetails.as_view()),
]
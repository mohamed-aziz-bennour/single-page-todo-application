"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^register$', csrf_exempt(views.RegisterView.as_view()), name='register'),
    url(r'^login$', csrf_exempt(views.LoginView.as_view()), name='login'),
    url(r'^(?P<token>[0-9a-zA-Z]+)/create$', csrf_exempt(views.CreateTodo.as_view()), name='create-todo'),
    url(r'^(?P<token>[0-9a-zA-Z]+)/all$', csrf_exempt(views.ViewAllTodos.as_view()), name='all-todos'),
    url(r'^(?P<token>[0-9a-zA-Z]+)/incompleted$', csrf_exempt(views.ViewIncompletedTodos.as_view()), name='incompleted-todos'),
    url(r'^(?P<token>[0-9a-zA-Z]+)/completed$', csrf_exempt(views.ViewCompletedTodos.as_view()), name='completed-todos'),
    url(r'^(?P<token>[0-9a-zA-Z]+)/complete_todo$', csrf_exempt(views.CompleteTodo.as_view()), name='complete-todo'),
    url(r'^(?P<token>[0-9a-zA-Z]+)/incomplete_todo$', csrf_exempt(views.InCompleteTodo.as_view()), name='incomplete-todo'),
    url(r'^(?P<token>[0-9a-zA-Z]+)/Update_todo$', csrf_exempt(views.UpdateTodo.as_view()), name='update-todo'),
    url(r'^(?P<token>[0-9a-zA-Z]+)/Todos_ByDate$', csrf_exempt(views.ViewCompletedTodos_ByDate.as_view()), name='date-todos'),

]
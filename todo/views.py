import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Todo, Profile
import datetime
from todo.login_form import UserForm
from todo.task_form import  PostForm

# Create your views here.

class Index(View):

    def get(self,request):
        return render(request, "todo/index.html", {'form':{'user':UserForm(),'todo':PostForm()}})

class RegisterView(View):

    def post(self,request):
        content = str(request.body,'utf8')
        data = json.loads(content)
        user = User.objects.create_user(data.get('username'),password=data.get('password'))
        profile = Profile.objects.create(user = user)
        print(profile)
        return JsonResponse({'user':profile.token.hex})


class LoginView(View):

    def post(self,request):    
        data = request.POST
        user = authenticate(username=data.get('username'), password=data.get('password'))
        if not user:
            return JsonResponse({'status':'failure', 'message':'invalid username'})
        profile = Profile.objects.get(user = user)
        return JsonResponse({'user':profile.token.hex})

class CreateTodo(View):

    def post(self,request,token):
        # content = str(request.body,'utf8')
        # data = json.loads(content)
        data = request.POST
        profile = Profile.objects.filter(token=token)
        if not profile or not data.get('task'):
            return JsonResponse({'status':'failure', 'message':'invalid username'})

        user = profile[0].user
        todo = Todo.objects.create(user=user, task=data.get('task'))
        return JsonResponse({'todo':todo.to_json()})

class ViewAllTodos(View):

    def get(self,request,token):
        profile = Profile.objects.get(token=token)
        todo_objects = profile.user.todo_set.all()
        todos = [todo.to_json() for todo in todo_objects]
        return JsonResponse({'todos':todos})

class ViewIncompletedTodos(View):

    def get(self,request,token):
        profile = Profile.objects.get(token=token)
        todo_objects = profile.user.todo_set.filter(completed=False)
        todos = [todo.to_json() for todo in todo_objects]
        return JsonResponse({'todos':todos})

class ViewCompletedTodos(View):

    def get(self,request,token):
        profile = Profile.objects.get(token=token)
        todo_objects = profile.user.todo_set.filter(completed=True)
        todos = [todo.to_json() for todo in todo_objects]
        return JsonResponse({'todos':todos})

# change complete to True 
class CompleteTodo(View):

    def post(self,request,token):
        # content = str(request.body,'utf8')
        # data = json.loads(content)
        data = request.POST
        profile = Profile.objects.get(token=token)
        if not profile or not data.get('id_post'):
            return JsonResponse({'status':'failure', 'message':'invalid username'})
        id_post = data.get('id_post')
        todo_object = profile.user.todo_set.get(id=id_post)
        todo_object.completed = True 
        todo_object.save()
        return JsonResponse({'todo':todo_object.to_json()})

# incomplete a todo , put it back to False
class InCompleteTodo(View):

    def put(self,request,token):
        content = str(request.body,'utf8')
        data = json.loads(content)
        profile = Profile.objects.get(token=token)
        if not profile or not data.get('id_post'):
            return JsonResponse({'status':'failure', 'message':'invalid username'})
        id_post = data.get('id_post')
        todo_object = profile.user.todo_set.get(id=id_post)
        todo_object.completed = False 
        todo_object.save()
        return JsonResponse({'todo':todo_object.to_json()})


# update a task in a todo
class UpdateTodo(View):

    def post(self,request,token):
        # content = str(request.body,'utf8')
        # data = json.loads(content)
        print("inside update*******")
        data = request.POST
        profile = Profile.objects.get(token=token)
        if not profile or not data.get('id_post'):
            return JsonResponse({'status':'failure', 'message':'invalid username'})
        id_post = data.get('id_post')
        task = data.get('task')
        todo_object = profile.user.todo_set.get(id=id_post)
        todo_object.task = task
        todo_object.save()
        return JsonResponse({'todo':todo_object.to_json()})

# show todos by date 

class ViewCompletedTodos_ByDate(View):

    def post(self,request,token):
        content = str(request.body,'utf8')
        data = json.loads(content)
        profile = Profile.objects.get(token=token)
        if not profile or not data.get('year') or not data.get('month') or not data.get('day'):
            return JsonResponse({'status':'failure', 'message':'invalid username'})
        year = data.get('year')
        month = data.get('month')
        day = data.get('day')
        todo_objects = profile.user.todo_set.filter(updated_at__date=datetime.date(year,month,day))
        todos = [todo.to_json() for todo in todo_objects]
        return JsonResponse({'todos':todos})
















        


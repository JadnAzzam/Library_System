from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import RegisterUserForm, RegisterLibrarianForm, UserForm, LibrarianForm, CreateBookForm, BookForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from .models import Book, Student, Librarian

@unauthenticated_user
def login_user_view(request):
  if request.method == "POST":
    form = AuthenticationForm(request = request, data = request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,f"You are now logged in as {username}")
            return redirect('')
        else:
            messages.error(request, 'Invalid Username or Password.')
    else:
        messages.error(request, "Invalid username or password.")
  form = AuthenticationForm()
  #returns the login page
  context = {'form':form}
  return render(request,'library/user_login.html',context)


def logout_user_views(request):
  logout(request)
  list(messages.get_messages(request))
  return redirect('home')

  @unauthenticated_user
  def register_user_views(request):
    if request.method == 'POST' :
      form = RegisterUserForm(request.POST)
      if form.is_valid():
        username = form.cleaned_data.get('username')
        current_user = Student.objects.filter(name = username).count()
        email = form.cleaned_data.get('email')

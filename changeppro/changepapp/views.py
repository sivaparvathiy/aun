from django.shortcuts import render
from django.shortcuts import render
#from django.contrib.auth.forms import
UserCreationForm
from .forms import signupForm
from django.contrib import messages
from django.contrib.auth.forms import
AuthenticationForm,PasswordChangeForm,SetPasswordFo
rm
from django.contrib.auth import
authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponseRedirect
# Create your views here.
def sign_up(request):
 if request.method=='POST':
 fm=signupForm(request.POST)
 if fm.is_valid():
 messages.success(request,'user creation.successfully')
 fm.save()
 else:
 fm=signupForm()
 return
render(request,'signup.html',{'form':fm})
def user_login(request):
 if not request.user.is_authenticated:
 if request.method == 'POST':
 fm =
AuthenticationForm(request=request,
data=request.POST)
 if fm.is_valid():
 uname = fm.cleaned_data['username']
 pwd = fm.cleaned_data['password']
 user = authenticate(username=uname,
password=pwd)
 if user is not None:
 login(request, user)
 return
HttpResponseRedirect('/profile/')
 else:
 fm = AuthenticationForm()
 return render(request, 'login.html',
{'form': fm})
 else:
 return HttpResponseRedirect('/profile/')
def profile(request):
 if request.user.is_authenticated:
 messages.success(request,'Login successfull')
 return render(request,'profile.html',{'name':request.user}
)
 else:
 return HttpResponseRedirect('/login/')
 def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/login/')
#change password with old password
def user_changepassword(request):
 if request.method=='POST':

fm=PasswordChangeForm(user=request.user,data=request.POST)
 if fm.is_valid():
 fm.save()
 update_session_auth_hash(request,fm.user)
 messages.success(request,'Password changedsuccessfully')
 return HttpResponseRedirect('/profile/')
 else:
 fm=PasswordChangeForm(user=request.user)
 return render(request,'changepassword.html',{'form':fm})
#change password without old password
def user_changepassword1(request):
 if request.method=='POST':

fm=SetPasswordForm(user=request.user,data=request.POST)
 if fm.is_valid():
 fm.save()
 update_session_auth_hash(request,fm.user)
 messages.success(request,'Password changedsuccessfully')
 return HttpResponseRedirect('/profile/')
 else:
 fm=SetPasswordForm(user=request.user)
 return render(request,'changepassword1.html',{'form':fm})

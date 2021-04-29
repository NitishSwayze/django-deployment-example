from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from AppThree import forms
from AppThree.models import VisitorList

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    my_dict = {"insert_me" : "Sign Up To Continue!"}
    return render(request, "AppThree/index.html", context = my_dict)

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserProfileForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = forms.UserProfileForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'AppThree/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account is not active')
        else:
            print("Someone tried to login and failed!")
            print("username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details!")
    else:
        return render(request, 'AppThree/login.html', {})



def form_name_view(request):
    form = forms.NewUserForm()
    # above we are creating a new instance of NewUserForm and assigning it to variable form
    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            # form.save(commit=True)
            form.save()
            form = forms.NewUserForm()
# in above line we are initiating form again so that after submission, the for becomes blain again
            return index(request)


        #     print('validation successful!')
        #     print("Name: "+form.cleaned_data['name'])
        #     print("Email: "+form.cleaned_data['email'])
        #     print("Text: "+form.cleaned_data['text'])

    return render(request, "AppThree/form_page.html", {'form':form})

def visitor(request):
    visitor_list = VisitorList.objects.order_by('first_name')
    visitor_dict = {'visitorpage': visitor_list}
    return render(request, "AppThree/visitorlist.html", context=visitor_dict)

def relative(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request, 'AppThree/relative_url_templates.html',context_dict)

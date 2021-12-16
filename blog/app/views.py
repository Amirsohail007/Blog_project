from django.shortcuts import render,redirect
from app.models import *
from app.forms import LoginForm,RegistrationForm,BlogForm
import datetime

# Create your views here.
#home page view
def home(request):
    all_posts = Blog.objects.all()
    return render(request, 'app/home.html',{'posts':all_posts, 'name':request.session.get('username')})

#dashboard view
def dashboard(request):
    if not request.session.get('username'):
        return redirect("login") 
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            b = Blog(
                title=form.cleaned_data["title"],
                post=form.cleaned_data["post"],
                date=datetime.date.today(),
                username=Registration.objects.get(user_name=request.session.get("username"))
            )
            b.save()

            return redirect('home')
    form = BlogForm()
      
    return render(request,'app/dashboard.html',{'form':form})

#login view
def login(request):
    if request.session.get('username'):
        return redirect("dashboard")
    if request.POST:
        if request.session.get('username'):
            return redirect("dashboard")
        form = LoginForm(request.POST)
        if form.is_valid():
            form_username = form.cleaned_data["username"]
            username = Registration.objects.filter(user_name=form_username)
            if username and username[0].password == form.cleaned_data["password"]:
                request.session['username'] = form_username
                request.session.set_expiry(0)
                print("successfully login")
                return redirect("home")
            else:
                print("invalid credentilal")
    else:
        form = LoginForm()
    return render(request,'app/login.html',{'form':form})


#logout view
def logout(request):
    try:
        del request.session['username']
    finally:
        return redirect('home')


#signup view
def signup(request):
    if request.session.get('username'):
        return redirect("dashboard")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = RegistrationForm()
    return render(request,'app/register.html',{'form':form})


#about view
def about(request):
    return render(request, 'app/about.html')
    

#contact view
def contact(request):
    return render(request, 'app/contact.html')


#all my post
def mypost(request):
    identity = Registration.objects.get(user_name=request.session.get("username"))
    posts = Blog.objects.filter(username=identity)
    return render(request, 'app/mypost.html',context={"posts":posts,'name':request.session.get('username')})

# detail view
def detail_view(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.POST:
        post_id = request.POST["identity"]
        post_obj = Blog.objects.get(id=post_id)
        post_obj.post = request.POST["post"]
        post_obj.title = request.POST["title"]
        post_obj.save()
        return redirect("mypost")
    return render(request, 'app/details.html',context={"post":blog})


# delete view
def delete_view(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect("mypost")

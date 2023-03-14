from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False).order_by('-id')[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })

# @login_required
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, '')
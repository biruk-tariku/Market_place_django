from django.shortcuts import render,redirect

from item.models import Category,Item

from .forms import signupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    Categories = Category.objects.all()

    return render(request, 'core/index.html',{
        'categories': Categories,
        'items': items,
    })

def contact (request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)


        if form.is_valid():
            form.save()

            return redirect('/login/')
        else:
            form = signupForm()
    form = signupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
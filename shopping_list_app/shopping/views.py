from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ShoppingListForm
from .models import ShoppingList

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('shopping_list')
        
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shopping_list')
    else:
        return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def shopping_list(request):
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shopping_item = form.save(commit=False)
            shopping_item.user = request.user
            shopping_item.save()
            return redirect('shopping_list')
    else:
        form = ShoppingListForm()
        items = ShoppingList.objects.filter(user=request.user)
        return render(request, 'shopping_list.html', {'form':form, 'items': items})
    
@login_required
def edit_item(request, item_id):
    item = ShoppingList.objects.get(id=item_id)
    if request.method == 'POST':
        form = ShoppingListForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('shopping_list')
    else:
        form = ShoppingListForm(instance=item)
    return render(request, 'edit_item.html', {'form': form})

@login_required
def delete_item(request, item_id):
    item = ShoppingList.objects.get(id=item_id)
    item.delete()
    return redirect('shopping_list')

@login_required
def toggle_purchase_item(request, item_id):
    item = get_object_or_404(ShoppingList, id=item_id)
    item.purchased = not item.purchased
    item.save()
    return redirect('shopping_list')


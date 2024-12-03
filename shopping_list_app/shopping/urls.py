from django.urls import path
from .views import register, user_login, user_logout, shopping_list, edit_item, delete_item, home, toggle_purchase_item

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('shopping_list/', shopping_list, name='shopping_list'),
    path('edit_item/<int:item_id>/', edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('toggle_purchase_item/<int:item_id>/', toggle_purchase_item, name='toggle_purchase_item'),]

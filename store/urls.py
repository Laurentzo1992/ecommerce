from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
 
 	path('update_item/', views.updateItme, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('create_user/', views.createUser, name="create_user"),
    path('edit_user/', views.editUser, name="edit_user"),

]
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.perfectwalk_home, name='PWhome'),
    path('index', views.index, name='PWindex'),
    path('createUser', views.create_user, name='PWcreateUser'),
    path('PetRegister', views.create_pet, name='PWcreatePet'),
    path('Post', views.create_post, name='PWcreatePost'),
    path('<int:pk>/perfectwalk_details', views.perfectwalk_details, name='PWpostDetails'),
    path('<int:pk>/perfectwalk_edit', views.perfectwalk_edit, name='PWpostEdit'),
    path('<int:pk>/perfectwalk_delete', views.perfectwalk_delete, name='PWpostDelete'),
]
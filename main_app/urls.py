from django.urls import path
from . import views #controller

#CRUD restsful routes
# with .as_view() we're accessing the appropriate controller

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('frogs/', views.frogs_index, name='index'),
    path('frogs/<int:frog_id>/', views.frogs_detail, name='detail'),
    path('frogs/create/', views.FrogCreate.as_view(), name='frogs_create'),
    path('frogs/<int:pk>/update/', views.FrogUpdate.as_view(), name='frogs_update'),
    path('frogs/<int:pk>/delete/', views.FrogDelete.as_view(), name='frogs_delete'),
]
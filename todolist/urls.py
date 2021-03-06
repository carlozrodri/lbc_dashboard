from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index,name="index"),
    path("update/<int:pk>", views.update_task, name="update_task"),
    path("deleted/<int:pk>/", views.delete_task, name="delete_task"),
  #  path('multi',views.multiplication, name='multi'),
   # path('test', views.Create_view.as_view(), name='create')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


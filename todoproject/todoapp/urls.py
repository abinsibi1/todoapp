from . import views
from django.urls import path
app_name='todoapp'
urlpatterns = [

    path('',views.home,name='home'),
    # path('details/',views.details,name='details'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.TaskDetailview.as_view(), name='cbvdetails'),
    path('cbvedit/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvedit'),
    path('cbvdelete/<int:pk>',views.TaskDeleteview.as_view(),name='cbvdelete'),

]
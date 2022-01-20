from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, DeleteView, TheLoginView, RegisterPage, HomePage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', TheLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', HomePage.as_view(), name='index'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('delete/<int:pk>', DeleteView.as_view(), name='task-delete'),
]
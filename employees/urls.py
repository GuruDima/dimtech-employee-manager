from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'employees'

urlpatterns = [
    # Главная страница — список сотрудников
    path('', views.employee_list, name='employee_list'),

    # CRUD сотрудников
    path('create/', views.employee_create, name='employee_create'),
    path('update/<int:pk>/', views.employee_update, name='employee_update'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),

    # Аутентификация
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='employees:login'), name='logout'),

    # Регистрация
    path('signup/', views.signup_view, name='signup'),

    # Доп. функционал
    path('export/excel/', views.export_employees_excel, name='export_excel'),
    path('stats/', views.employee_stats, name='employee_stats'),
]

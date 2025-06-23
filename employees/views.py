from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q, Avg, Count
from django.contrib.auth.forms import UserCreationForm

from .models import Employee
from .forms import EmployeeForm
import openpyxl

# Проверка: является ли пользователь staff
def is_staff_user(user):
    return user.is_staff


# 📋 Список сотрудников с фильтрацией, сортировкой и пагинацией
@login_required
def employee_list(request):
    query = request.GET.get("q")
    position = request.GET.get("position")
    level = request.GET.get("level")
    sort = request.GET.get("sort")

    employees = Employee.objects.all()

    if query:
        employees = employees.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    if position:
        employees = employees.filter(position=position)
    if level:
        employees = employees.filter(level=level)

    # Сортировка
    sort_options = {
        "name_asc": "first_name",
        "name_desc": "-first_name",
        "salary_asc": "salary",
        "salary_desc": "-salary",
        "level_asc": "level",
        "level_desc": "-level",
        "date_asc": "date_hired",
        "date_desc": "-date_hired"
    }
    if sort in sort_options:
        employees = employees.order_by(sort_options[sort])

    paginator = Paginator(employees, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    positions = Employee.objects.values_list("position", flat=True).distinct()
    levels = Employee.LEVEL_CHOICES

    return render(request, "employees/employee_list.html", {
        "employees": page_obj,
        "positions": positions,
        "levels": levels
    })


# ➕ Добавление сотрудника
@login_required
@user_passes_test(is_staff_user)
def employee_create(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Сотрудник успешно добавлен.")
        return redirect("employees:employee_list")
    return render(request, "employees/employee_form.html", {"form": form})


# ✏️ Редактирование сотрудника
@login_required
@user_passes_test(is_staff_user)
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, request.FILES or None, instance=employee)
    if form.is_valid():
        form.save()
        messages.success(request, "Информация о сотруднике обновлена.")
        return redirect("employees:employee_list")
    return render(request, "employees/employee_form.html", {"form": form})


@login_required
@user_passes_test(is_staff_user)
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        employee.delete()
        messages.success(request, "Сотрудник удалён.")
        return redirect("employees:employee_list")

    return render(request, "employees/employee_delete.html", {"employee": employee})



# 👁️ Просмотр профиля сотрудника
@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, "employees/employee_detail.html", {"employee": employee})


# 🔐 Регистрация
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Аккаунт успешно создан. Войдите в систему.")
            return redirect("employees:login")
    else:
        form = UserCreationForm()
    return render(request, "employees/signup.html", {"form": form})


# 📤 Экспорт в Excel
@login_required
@user_passes_test(is_staff_user)
def export_employees_excel(request):
    employees = Employee.objects.all()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["ID", "Имя", "Фамилия", "Должность", "Оклад", "Уровень", "Email", "Телефон", "Дата приёма"])

    for emp in employees:
        ws.append([
            emp.id, emp.first_name, emp.last_name, emp.position,
            emp.salary, emp.get_level_display(), emp.email,
            emp.phone, emp.date_hired.strftime("%Y-%m-%d") if emp.date_hired else ""

        ])

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = "attachment; filename=employees.xlsx"
    wb.save(response)
    return response


# 📊 Статистика сотрудников
@login_required
def employee_stats(request):
    total = Employee.objects.count()
    avg_salary = Employee.objects.aggregate(avg=Avg("salary"))["avg"]
    levels = (
        Employee.objects
        .values("level")
        .annotate(count=Count("id"))
        .order_by("level")
    )

    level_display = dict(Employee.LEVEL_CHOICES)
    for level in levels:
        level["label"] = level_display.get(level["level"], level["level"])

    return render(request, "employees/employee_stats.html", {
        "total": total,
        "avg_salary": avg_salary,
        "levels": levels
    })


# 🧱 Кастомные страницы ошибок
def custom_403(request, exception=None):
    return render(request, "403.html", status=403)

def custom_404(request, exception=None):
    return render(request, "404.html", status=404)

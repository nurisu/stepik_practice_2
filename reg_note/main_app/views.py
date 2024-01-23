from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse
from main_app.models import User, Notes

def reg(request):
    if request.method == "GET":
        return render(request, "reg.html")
    else:
        data = request.POST
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password1, password2 = data.get("password1"), data.get("password2")
        if username is None:
            return HttpResponse("<h3>Введите имя пользователя</h3>")
        elif email is None:
            return HttpResponse("<h3>Введите почту</h3>")
        elif first_name is None:
            return HttpResponse("<h3>Введите имя</h3>")
        elif last_name is None:
            return HttpResponse("<h3>Введите фамилию</h3>")
        elif password1 is None or password2 is None:
            return HttpResponse("<h3>Введите пароль</h3>")
        elif password1 != password2:
            return HttpResponse("<h3>Пароли должны совпадать</h3>")
        else:
            newuser = User()
            newuser.create_user(username, first_name, last_name, email, password1)
            return HttpResponse("<h3>Вы успешно зарегистрировались</h3>")

def login_page(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        data = request.POST
        try:
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is None:
                return HttpResponse("<h3>Пользователь с таким логином и паролем не найден</h3>")
            login(request, user)
            return HttpResponse("<h3>Вы успешно авторизованы</h3>")
        except KeyError:
            return HttpResponse("<h3>Заполните все поля</h3>")

def logout_page(request):
    logout(request)
    return HttpResponse("<h3>Вы успешно вышли из системы</h3>")

def notes(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h3>Войдите в профиль</h3>")
    else:
        username = request.user.username
        user_id = request.user.id
        context = {"notes": [a.note_text for a in Notes.objects.filter(username=user_id)], "username": username}
        return render(request, "notes.html", context)

def add_note(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h3>Войдите в профиль</h3>")
    else:
        if request.method == "GET":
            return render(request, "add_note.html")
        else:
            data = request.POST
            my_note = data.get("my-note")
            note = Notes(username=request.user, note_text=my_note)
            note.save()
            return render(request, "add_note.html")


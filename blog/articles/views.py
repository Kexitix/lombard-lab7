from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # проверка уникальности названия статьи
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = u"Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                # если поля заполнены без ошибок
                article = Article.objects.create(text=form["text"], title=form["title"],
                                                 author=request.user)
                return redirect('get_article', article_id=article.id)
                # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", "").strip(),
            'email': request.POST.get("email", "").strip(),
            'password': request.POST.get("password", ""),
        }
        if not (form['username'] and form['email'] and form['password']):
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'register.html', {'form': form})
        try:
            User.objects.get(username=form['username'])
            # если пользователь существует, то ошибки не произойдет
            form['errors'] = u"Пользователь с таким именем уже есть"
            return render(request, 'register.html', {'form': form})
        except User.DoesNotExist:
            # этот логин свободен - регистрируем
            User.objects.create_user(form['username'], form['email'], form['password'])
            return redirect('login')
    return render(request, 'register.html', {})


def login_view(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", "").strip(),
            'password': request.POST.get("password", ""),
        }
        if not (form['username'] and form['password']):
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'login.html', {'form': form})
        user = authenticate(username=form['username'], password=form['password'])
        if user is not None:
            login(request, user)
            return redirect('archive')
        form['errors'] = u"Такого аккаунта не существует или пароль неверный"
        return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('archive')

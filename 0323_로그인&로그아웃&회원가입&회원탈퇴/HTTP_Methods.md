# READ 1 (index page)
- index 페이지에서는 전체 게시글을 조회해서 출력

```django
1. articles/views.py

from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

2. templates/articles/index.html

{% extends 'base.html' %}

{%block content %}
    {% for article in articles %}
        <p>글 번호 : {{ article.pk }}</p>
        <p>글 제목 : {{ article.title }}</p>
        <p>글 내용 : {{ article.content }}</p>
    {% endfor %}
{% endblock content %}
```

# READ 2 (detail page)
- 개별 게시글 상세 페이지 제작
- 글의 번호(pk)을 활용해서 하나의 view 함수와 templates 파일로 대응
- Variable Routing 활용

```django
1. articles/urls.py
- URL로 특정 게시글을 조회할 수 있는 번호를 받음

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]

2. articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

3. templates/articles/detail.html

{% extends 'base.html' %}

{% block content %}
    <h3>{{ article.pk }} 번째 글</h3>
    <p>재목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <p>작성 시각 : {{ article.created_at }}</p>
    <p>수정 시각 : {{ article.updated_at }}</p>
{% endblock content %}
```

# CREATE

- 사용자의 입력을 받을 페이지를 렌더링 하는 함수 1개
    - "new" view function

- 사용자가 입력한 데이터를 전송 받아 DB에 저장하는 함수 1개
    - "create" view function

### New

```django
1. articles/urls.py

urlpatterns = [
    path('new/', views.new, name='new'),
]

2. articles/views.py

def new(request):
    return render(request, 'articles/new.html')

3. templates/article/new.html

{% extends 'base.html' %}

{% block content %}
    <form action="{% url 'articles:create' %}" method='GET'>
        <label for='title'>Title: </label>
        <input type='text' name='title'>

        <label for='content'>Content: </label>
        <textarea name='content'></textarea>

        <input type='submit'>
    </form>
{# endblock content %}
```

### create

```django
1. articles/urls.py

urlpatterns = [
    path('create/', views.create, name='create'),
]

2. articles/views.py

def create(request):
    # 입력한 데이터 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 데이터를 생성하는 3가지 방법 (1번 또는 2번 생성 방식을 많이 사용함)
    # 1.
    article = Article()
    article.title = title
    article.content = content
    article.save()

    # 2.
    article = Article(title=title, content=content)
    article.save()

    # 3.
    Article.objects.create(title=title, content=content)

    # "redirect()"은 인자에 작성된 곳으로 다시 요청을 보냄
    return redirect('articles:detail', article.pk)
```

# GET

- 특정 리소스를 가져오도록 요청할 대 사용
- 반드시 데이터를 가져올 때만 사용해야 함
- DB에 변화를 주지 않음
- CRUD에서 R 역할을 담당

# POST

- 서버로 데이터를 전송할 때 사용
- 서버에 변경사항을 만듦
- 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
- GET의 query string parameter와 다르게 URL로 데이터를 보내지 않음
- CRUD에서 C/U/D 역할을 담당

```django
POST method 적용하기

1. templates/articles/new.html

{% extends 'base.html' %}

{% block content %}
    <form action="{% url 'articles:create' %}" method="POST">
    ...
    </form>

2. articles/views.py

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
```

# 403 Forbidden

- 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
- 서버에 요청은 도달했으나 서버가 접근을 거부할 때 반환됨
- 즉, 게시글을 작성할 권한이 없다
    - Django 입장에서는 작성자가 누구인지 모르기 때문에 함부로 작성할 수 없다라는 의미
- 모델(DB)을 조작하는 것은 단순 조회와 달리 최소한의 신원 확인이 필요

# CSRF

- Cross-Site-Request-Forgery
- 사이트 간 요청 위조
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
- Security Token 사용 방식 - (CSRF Token)
- 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용

- {% csrf_token %}
    - 해당 태그가 없다면 Django 서버는 요청에 대해 403 forbidden으로 응답
    - 템플릿에서 내부 URL로 향하는 POST form을 사용하는 경우에 사용 (외부 URL로 향하는 POST form에 대해서는 사용 금지)

# DELETE

```django
1. articles/urls.py

urlpatterns = [
    path('<int:pk>/delete/', views.delete, name='delete'),
]

2. articles/views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

3. articles/detial.html
# Detail 페이지에 작성하여 DB에 영향을 미치기 때문에 POST method를 사용

{% extends 'base.html' %}

{% block content %}
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
    </form>
{% endblock content %}
```

# UPDATE

- 사용자의 입력을 받을 페이지를 렌더링 하는 함수 1개
    - "edit" view function

- 사용자가 입력한 데이터를 전송 받아 DB에 저장하는 함수 1개
    - "update" view function

### Edit

```django
1. articles/urls.py

urlpatterns = [
    path('<int:pk>/edit/', views.edit, name='edit'),
]

2. articles/views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

3. articles/edit.html

{% extends 'base.html' %}

{% block content %}
    <form action="#" method="POST">
        {% csrf_token %}
        <label for="title">Title: </label>
        <input type="text" name="title" value="{{ article.title }}>

        <label for="content">Content: </label>
        <textarea name="content">{{ article.content }}</textarea>

        <input type="submit">
    </form>
{% endblock content %}

4. articles/detail.html

# Edit 페이지로 이동하기 위한 하이퍼 링크를 detail.html에 작성
<a href="{% url 'articles:edit' article.pk %}">EDIT</a>
```

### Update

```django
1. articles/urls.py

urlpatterns = [
    path('<int:pk>/update/', views.update, name='update'),
]

2. articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)

3. articles/edit.html
<form action="#" method="POST">
-> <form action="{% url 'articles:update' article.pk %}" method="POST">
```

# Handling HTTP requests

- 공통점
    - new-create는 모두 CREATE 로직을 구현하기 위한 공통 목적
    - edit-update는 모두 UPDATE 로직을 구현하기 위한 공통 목적

- 차이점
    - new와 edit는 GET 요청에 대한 처리만을
    - create와 update는 POST 요청에 대한 처리만을 진행

### Create

- new와 create view 함수를 합침
- 각각의 역할은 request.method 값을 기준으로 나뉨

```django
1. articles/view.py

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:detail', pk=article.pk #(or article.pk))
    else:
        return rendeR(request, 'articles/create.html') 

2. new의 view 함수와 new의 url path 삭제
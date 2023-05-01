# Django Form


## Form에 대한 Django의 역할

- Form은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단

- Django는 Form과 관련한 유효성 검사를 **단순화하고 자동화** 할 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있다.
  - 개발자가 필요한 핵심 부분만 집중할 수 있도록 돕는 프레임워크의 특성


## Django는 Form에 관련된 작업의 세 부분을 처리

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리


## Form과 ModelForm

- ModelForm이 Form보다 더 좋은 것이 아니라 각자 역할이 다른 것

- Form

  - 사용자의 입력을 필요로 하며 직접 입력 데이터가 DB 저장에 사용되지 않거나 일부 데이터만 사용될 때 (ex - 로그인, 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않음)

- ModelForm

  - 사용자의 입력을 필요로 하며 입력을 받은 것을 그대로 DB 필드에 맞춰 저장할 때
  
  - 데이터의 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할지 이미 알고 있기 때문에 곧바로 save() 호출이 가능


# Static File

- 응답할 대 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
  - 사용자의 요청에 따라 내용이 바뀌는 것이 아니라 요청한 것을 그대로 보여주는 파일

- **파일 자체가 고정**되어 있고 서비스 중에도 추가되거나 **변경되지 않고 고정** 되어있음
  - 예를 들어, 웹 사이트는 일반적으로 이미지, 자바 스크립트 또는 CSS와 같은 미리 준비된 추가 파일(움직이지 않는)을 제공해야 함

- Django에서는 이러한 파일들을 "static file"이라 함
  - Django는 staticfiles 앱을 통해 정적 파일과 관련된 기능을 제공


## Media File

- 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)
- 유저가 업로드 한 모든 정적 파일


## Django에서 정적파일을 구성하고 사용하기 위한 몇가지 단계

1. INSTALLED_APPS에 django.contrib.staticfiles가 포함되어 있는지 확인하기
2. settings.py에서 STATIC_URL을 정의하기
3. 앱의 static 폴더에 정적 파일을 위치하기
4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기
```django
{% load static %}
<img src = "{% static 'sample_img.jpg' %}" alt="sample image">
```


## Django template tag

- {% load %}
  - 특정 라이브러리, 패키지에 등록된 모든 템플릭 태그와 필터를 로드

- {% static ' ' %}
  - STATIC_ROOT에 저장된 정적 파일에 연결


## Static files 관련 Settings

1. STATIC_ROOT
- Default : None
- Django 프로젝트에서 사용하는 모든 정적 파일을 한곳에 모아 넣는 경로
- **collectstatic**이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
- **개발 과정에서 settings.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음**

```django
# settings.py

 STATIC_ROOT = BASE_DIR / 'staticfiles'
```

2. STATICFILES_DIRS
- Default : [] (Empty list)
- **app/static/** 디렉토리 경로를 사용하는 것 (기본 경로)외에 추가적인 정적 파일 경로 목록을 정의하는 리스트
- 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함
```django
# settings.py

STATICFILES_DIR = [
  BASE_DIR / 'static',
]
```

3. STATIC_URL
- Default : None
- STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL
- 개발 단계에서는 실제 정적 파일들이 저장되어 있는 **app/static/** 경로 (기본 경로) 및 **STATICFILES_DIRS**에 정의된 추가 경로들을 참색
- **실제 파일이나 디렉토리가 아니며, URL로만 존재**
- 비어 있지 않은 값으로 설정 한다면 반드시 /(slash)로 끝나야 함
```django
# settings.py

STATIC_URL = '/static/'
```

## ImageField()
- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능
- 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
- IageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경 할 수 있음


## FileField()
- FileField(upload_to = '', storage=None, max_length=100, **options)
- 파일 업로드에 사용하는 모델 필드
- 2개의 선택 인자를 가지고 있음
  - 1. upload_to
  - 2. storage


## FileField / ImageField를 사용하기 위한 단계
1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
2. upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정 (선택사항)


## MEDAI_ROOT
- Default : '' (Empty string)
- 사용자가 업로드 한 파일 (미디어 파일)들을 보관할 디렉토리의 절대 경로
- Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
  - 데이터베이스에 저장되는 것은 **파일 경로**
- **MEDAI_ROOT는 STATIC_ROOT**와 반드시 다른 경로로 지정해야 함
```django
# settings.py

MEDIA_ROOT = BASE_DIR / 'media'
```

## MEDIA_URL
- Default: '' (Empty string)
- MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL
- 업로드 된 파일의 주소(URL)를 만들어 주는 역할
  - 웹 서버 사용자가 사용하는 public URL
- 비어 있지 않은 값으로 설정 한다면 반드시 /(slash)로 끝나야 함
- **MEDAI_URL은 STATIC_URL**과 반드시 다른 경로로 지정해야 함
```django
# settings.py

MEDIA_URL = '/media/'
```

## 개발 단계에서 사용자가 업로드한 미디어 파일 제공하기
```django
# 프로젝트/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
- 사용자로부터 업로드 된 파일이 프로젝트에 업로드 되고나서, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요함
  - 업로드 된 파일의 URL == settings.MEDIA_URL
  - 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT



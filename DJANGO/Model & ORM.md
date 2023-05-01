# Sending form data (Client)

## HTML < form > element

- 데이터가 전송되는 방법을 정의
  
- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당
  
- 데이터를 어디(action)로 어떤 방식(method)으로 보낼지
  
- 핵심 속성
  
  - action
    
  - method
    

## HTML form's attributes

1. action
  

- 입력 데이터가 전송될 URL을 지정
  
- 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야 함
  
- 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
  

2. method
  

- 데이터를 어떻게 보낼 것인지 정의
  
- 입력 데이터의 HTTP request methods를 지정
  
- HTML form 데이터는 오직 2가지 방법으로만 전송 할 수 있는데 바로 GET 방식과 POST 방식
  

## HTML < input > element

- 사용자로부터 데이터를 입력 받기 위해 사용
  
- "type" 속성에 따라 동작 방식이 달라짐
  
  - input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 각각의 type은 별도로 MDN 문서에서 참고하여 사용하도록 함
    
  - type을 지정하지 않은 경우, 기본값은 "text"
    
- 핵심 속성
  
  - name
    

## HTML input's attribute

- name
  
  - form을 통해 데이터를 제출(submit) 했을 때 name 속성에 설정된 값을 서버로 전송하고, 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
    
  - 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것
    

## HTML request methods

- HTTP
  
  - HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜
    
- 웹에서 이루어지는 모든 데이터 교환의 기초
  
- HTTP는 주어진 리소스가 수행 할 원하는 작업을 나타내는 request methods를 정의
  
- 자원에 대한 행위(수행하고자 하는 동작)를 정의
  
- 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
  
- HTTP Method 예시
  
  - GET, POST, PUT, DELETE
    

## GET

- 서버로부터 정보를 조회하는데 사용
  
  - 즉, 서버에게 리소스를 요청하기 위해 사용
    
- 데이터를 가져올 때만 사용해야 함
  
- 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
  
  - 데이터는 URL에 포함되어 서버로 보내짐
    
- GET과 get 모두 대소문자 관계없이 동일하게 동작하지만 명시적 표현을 위해 대문자 사용을 권장
  

## Method = GET vs POST

- GET
  
  - GET 메소드는 주로 데이터를 읽거나 검색
    
  - GET 메소드를 사용하면 모든 form date는 URL로 인코딩되어 action URL에 Query String Parameters로 전달됨
    
- POST
  
  - POST 메소드는 주로 새로운 리소스를 생성(create)시 사용
    

## Query String Parameters

- 사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 데이터를 파라미터를 통해 넘기는 것
  
- 이러한 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성되며 기본 URL과 물음표(?)로 구분됨
  
- Query String이라고도 함
  
- 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
  
- "key=value"로 필요한 파라미터의 값을 적음
  
  - "="로 key와 value가 구분됨
    
- 파라미터가 여러 개일 경우 "&"를 붙여 여러 개의 파라미터를 넘길 수 있음
  

# Retrieving the data (Server)

- 데이터 가져오기(검색하기)
  
- 서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게 됨
  
- 이러한 목록에 접근하는 방법은 사용하는 특정 프레임워크에 따라 다름
  

## Request and Response objects

- 요청과 응답 객체 흐름
  

1. 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성
  
2. 그리고 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달
  
3. 마지막으로 view 함수는 HttpResponse object를 반환
  

## Request.get() vs Request.GET.get('message')

- request라는 이름의 객체에 대해 get 메소드를 실행 (파이썬 딕셔너리에서의 get 개념)
  
- request.GET은 Django에서 사용
  
- "request"는 HttpRequest가 보내졌을 때에 Django가 만든 객체이며, "request.GET"을 실행하는 것으로 request의 정보를 딕셔너리로 얻을 수 있게 하는 것
  
- request.GET.get('message') 뜻은 request.GET한 딕셔너리 형태의 정보에서 get() 메소드를 실행하여 데이터 얻기
  

## DATABASE 기본 구조

- 스키마 - DB 기본구조 (뼈대)
  
- 필드 - DB 테이블에서 열
  
- 레코드 - DB 테이블에서 행
  
- PK - id 중복 불가, Django가 생성
  

# Django Model

- Django는 Model을 통해 데이터에 접근하고 조작
  
- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
  
- 저장된 데이터베이스의 구조 (layout)
  
- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
  
  - 모델 클래스 1개 == 데이터베이스 테이블 1개
    

## Django Model Field

1. CharField (max_length = None)
  

- 길이의 제한 있는 문자열, 실제로 제한이 있음
  

2. TextField (max_length = )
  

- 입력 단계에서 글자수 제한이 있음. 단, 실제로 저장될 때 길이에 대한 제한을 두지 않음
  

3. DatetimeField (auto_now_add)
  

- 최초 생성일자 자동 생성 (게시판 글 작성 날짜)
  

4. DatetimeField (auto_now)
  

- 최초 수정일자 자동 생성 (게시판 글 작성 날짜)
  

5. EmailField (auto_now)
  

- 이메일 형식에 맞게 작성하는 필드
  

## Migrate

- makemigrations
  
  - 테이블 생성 및 수정시 반드시 migration 해야함
    
  - 프로젝트 설계도의 청사진만 그림
    
  - DB에는 테이블이 아직 생성되지는 않음 (청사진만 그림)
    
- migrate
  
  - 동기화 - 모델 변경사항과 데이터 동기화
    
- models.py에서 새로 스키마를 만들거나 수정을 했다면 반드시 migrate를 통해서 DB와 동기화를 해야 함
  
- 1. python manage.py makemigrations
    
  2. python manage.py migrate
    

# ORM

- Object-Relational-Mapping
  
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 (Django <-> DB) 데이터를 변환하는 프로그래밍 기술
  
- 객체 지향 프로그래밍에서 데이터베이스를 연동할 때, 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
  
- Django는 내장 Django ORM을 사용
  
- 한 마디로 SQL을 사용하지 않고 데이터베이스를 조작할 수 있게 만들어주는 매개체
  

## ORM 장단점

- 장점
  
  - SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능
    
  - 객체 지향적 접근으로 인한 높은 생산성
    
- 단점
  
  - ORM 만으로 세밀한 데이터베이스 조작을 구현하기 어려운 경우가 있음
    

## ORM을 사용하는 이유

- 우리는 DB를 객체(object)로 조작하기 위해 ORM을 사용할 것
  

# QuerySet API

## Query

- 데이터베이스에 특정한 데이터를 보여 달라는 요청
  
  - "쿼리문을 작성한다" 라는 것은 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성
    
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달
  
- 데이터베이스에게서 전달 받은 객체 목록 (데이터 모음)
  
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
    
- Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음
  
- objects manager를 사용하여 복수의 데이터를 가져오는 queryset method를 사용할 때 반환되는 객체
  
- 단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨
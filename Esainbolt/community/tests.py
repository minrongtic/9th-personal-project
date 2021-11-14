from django.test import TestCase

# Create your tests here.
# <navbar>
#         {% if user.is_authenticated %}
#             <a href="{% url 'account_logout' %}">로그아웃</a>
#             <a href="{% url 'account_change_password' %}">비밀번호 변경</a>
#             <a href="{% url 'community:communityBoard' %}">커뮤니티</a>
#         {% else %}
#             <a href="{% url 'account_login' %}">로그인</a>
#             <a href="{% url 'account_signup' %}">회원가입</a>
#         {% endif %}
#     </navbar>


# <!DOCTYPE html>
# <html lang="kr">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link rel="stylesheet" type="text/css" href={% static 'route/css/main.css' %}>
#     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
#     <title>Esainbolt | Main</title>
# </head>
# <body>
#     <nav class="navbar navbar-expand-lg navbar-light bg-light">
#         <div class="container">
#             <div class="collapse navbar-collapse" id="navbarSupportedContent">
#                 <ul class="navbar-nav ms-auto">
#                     <li class="nav-home">
#                         <a class="nav-link active" aria-current="page" href="{% url 'route:main' %}">Home</a>
#                     </li>
#                     {% if user.is_authenticated %}
#                         <li class="nav-community">
#                             <a class="nav-link active" aria-current="page" href="{% url 'community:communityBoard' %}">Community</a>
#                         </li>
#                         <li class="nav-login">
#                             <a class="nav-link active" aria-current="page" href="{% url 'account_logout' %}">Logout</a>
#                         </li>
#                         <li class="nav-login">
#                             <a class="nav-link active" aria-current="page" href="{% url 'account_change_password' %}">Change_Password</a>
#                         </li>
#                     {% else %}
#                         <li class="nav-login">
#                             <a class="nav-link active" aria-current="page" href="{% url 'account_login' %}">Login</a>
#                         </li>
#                         <li class="nav-login">
#                             <a class="nav-link active" aria-current="page" href="{% url 'account_signup' %}">SignUp</a>
#                         </li>
#                     {% endif %}
#                 </ul>
#             </div>
#         </div>
#     </nav>


# communityBoard

    {% for community in communities.all % }
    <div class = "title" >
        <a href = "{% url 'community:communityDetail' community.id %}" > {{community.title}} < /a >
    </div >
    {% endfor % }
    <br >
    <br >
    <a href = "{% url 'community:communityNew' %}" > 글 쓰기 < /a >
{% endblock body-content % }

# community Detail
<div class = "title" >
        <h2 > {{community.title}} < /h2 >
    </div>
    <div class="date-time">
        <h5>{{community.date.date}}</h5>
        <h5>{{community.date.time}}</h5>
    </div>
    <div class="body">
        <p>{{community.body}}</p>
    </div>
    <br>
    <br>
    <a href="{% url 'community:communityEdit' community.id %}">수정하기</a>
    <a href="{% url 'community:communityDelete' community.id %}">삭제하기</a>

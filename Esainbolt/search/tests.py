from django.test import TestCase

# Create your tests here.

<div class = "search_bar" >
        <h3 > 검색어: < strong > {{query}} < /strong > </h3 >
    </div>
    {% if routes_list %}
    {% for route in routes_list %}
    <div class="search_result">
        <a href="/route/{{route.id}}">{{route.via}}</a>
    </div>
    {% endfor %}
    {% elif query %}
        <h5>검색 결과가 없습니다</h5>
    {% endif %}
{% endblock body-content %}

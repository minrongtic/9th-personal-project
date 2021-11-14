from django.test import TestCase

# Create your tests here.
# route Board 원래
 <!-- < div class = "fin" >
        <h2 > 도착지: {{route.fin}} < /h2 >
    </div>
    <div class="via">
        <p>가는 방법: {{route.via}}</p>
    </div>
    <div class="more">
        <a href="{% url 'route:routeDetail' route.id %}">more</a>
    </div>
    <br><br>
    {% endfor %}
{% endblock body-content %} -->

# route detail 원래
<div class="fin">
        <h2>도착지: {{route.fin}}</h2>
    </div>
    <div class="via">
        <p>가는 방법: {{route.via}}</p>
    </div>
    <div class="etc">
        <p>비고: {{route.etc|linebreaks}}</p>
    </div>

<a href="{% url 'route:routeDetail' route.id %}" class="stretched-link">자세히 보기</a>

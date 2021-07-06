from django.contrib import admin
from django.urls import path

from django.views.decorators.csrf import csrf_exempt


from .views import RiskCalculator

urlpatterns = [
    path(
        "calculate/",
        csrf_exempt(RiskCalculator.as_view()),
        name="risk calculator route",
    )
]

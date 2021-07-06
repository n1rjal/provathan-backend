from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


from .utils import get_risk_label
from .serializers import RiskFormSerializer
from django.utils.decorators import method_decorator
from rest_framework import routers, serializers, viewsets


import json

# Create your views here.
class RiskCalculator(View):
    def post(self, request):
        # data sent to the server by the client
        data = json.loads(request.body)
        # lets make a serilizer object
        SerializerResponse = RiskFormSerializer(data=data)
        if not SerializerResponse.is_valid():
            return JsonResponse({"errors": SerializerResponse.errors})

        else:
            risk_prediction = SerializerResponse.calculate_risk(**data)
            return JsonResponse(
                {
                    "prediction": risk_prediction,
                    "label": get_risk_label(risk_prediction),
                }
            )

    def get(self, request):
        return JsonResponse({"hello": "GET"})

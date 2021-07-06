from rest_framework import routers, serializers, viewsets
from .utils import ProvathanModelInstance

# serializers for easy validation
class RiskFormSerializer(serializers.Serializer):
    gender = serializers.CharField(max_length=1)
    age = serializers.FloatField()
    CCP = serializers.BooleanField()
    RF = serializers.BooleanField()
    CRP = serializers.FloatField()
    HAD = serializers.BooleanField()
    UA = serializers.FloatField()
    ESR = serializers.FloatField()
    RBC = serializers.FloatField()
    WBC = serializers.FloatField()
    HMC = serializers.FloatField()
    HMG = serializers.FloatField()
    PLT = serializers.FloatField()

    def calculate_risk(self, **kwargs):
        return ProvathanModelInstance.predict(**kwargs)

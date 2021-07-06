from rest_framework import routers, serializers, viewsets
from .utils import ProvathanModelInstance

# serializers for easy validation
class RiskFormSerializer(serializers.Serializer):
    sp02 = serializers.FloatField(label="Oxygen Level", required=True)
    temperature = serializers.FloatField(label="Temperature", required=True)
    CRP = serializers.FloatField(
        label="C reactive protein",
    )
    HMG = serializers.FloatField(
        label="Haemoglobin",
    )
    WBC = serializers.FloatField(
        label="WBC COUNT",
    )
    PC = serializers.FloatField(
        label="platelet count",
    )
    KD = serializers.BooleanField(label="Kidney Disease")
    AD = serializers.BooleanField(label="Auto Immunity Disease")
    RD = serializers.BooleanField(label="Respiratory Disease")

    def calculate_risk(self, **kwargs):
        return ProvathanModelInstance.predict(**kwargs)

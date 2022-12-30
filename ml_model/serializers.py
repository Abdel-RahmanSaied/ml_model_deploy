from rest_framework import serializers , fields
from rest_framework.response import Response

class ModelSerializer(serializers.Serializer):
    class Meta :
        id = serializers.IntegerField(required=True)
        ATF = serializers.IntegerField(required=True)
        TKF = serializers.IntegerField(required=True)
        CMT = serializers.IntegerField(required=True)
        DEF = serializers.IntegerField(required=True)
        SMF = serializers.IntegerField(required=True)
        ERF = serializers.IntegerField(required=True)
        DAF = serializers.IntegerField(required=True)
        HR = serializers.IntegerField(required=True)
        SW = serializers.IntegerField(required=True)
        TR = serializers.IntegerField(required=True)
        BR = serializers.IntegerField(required=True)
        NS = serializers.IntegerField(required=True)
        DZ = serializers.IntegerField(required=True)
        UB = serializers.IntegerField(required=True)
        hasSAD = serializers.IntegerField(required=True)
        Suicidal = serializers.IntegerField(required=True)
        DpD = serializers.IntegerField(required=True)
        DpT = serializers.IntegerField(required=True)

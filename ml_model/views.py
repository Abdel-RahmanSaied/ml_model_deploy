import os

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status, filters
from .serializers import ModelSerializer
import joblib
import pickle
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

@permission_classes([])
class ModelResult(viewsets.ModelViewSet):
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        id = request.data["id"]
        ATF = request.data["ATF"]
        TKF = request.data["TKF"]
        CMT = request.data["CMT"]
        DEF = request.data["DEF"]
        SMF = request.data["SMF"]
        ERF = request.data["ERF"]
        DAF = request.data["DAF"]
        HR = request.data["HR"]
        SW = request.data["SW"]
        TR = request.data["TR"]
        BR = request.data["BR"]
        NS = request.data["NS"]
        DZ = request.data["DZ"]
        UB = request.data["UB"]
        hasSAD = request.data["hasSAD"]
        Suicidal = request.data["Suicidal"]
        DpD = request.data["DpD"]
        DpT = request.data["DpT"]
        serialer = ModelSerializer(data= request.data)
        if serialer.is_valid(raise_exception=True):
            model_path = "models/anxiety_severity.pkl"
            model = joblib.load(model_path)
            mapp = {0: "Mild", 1: "Minimal", 2: "Moderate ", 3: "Severe "}
            data = [id,ATF,TKF,CMT,DEF, SMF, ERF, DAF, HR, SW, TR, BR, NS, DZ, UB, hasSAD, Suicidal, DpD, DpT]

            model_result =mapp.get(int(model.predict([data])))
            return Response({"detail": model_result}, status=status.HTTP_200_OK)
        else:
            return Response( {"detail": serialer.errors}, status=status.HTTP_400_BAD_REQUEST)



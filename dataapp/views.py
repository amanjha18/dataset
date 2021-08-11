from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


class SetPharma(APIView):
    def post(self, request):
        year = request.data['year']
        datum = request.data['datum']
        m01ab = request.data['m01ab']
        m01ae = request.data['m01ae']
        n02ba = request.data['n02be']
        n02be = request.data['n02be']
        n05b= request.data['n05b']
        n05c = request.data['n05c']
        r03 = request.data['r03']
        r06 = request.data['r06']
        pharma_table=PharmaSales.objects.create(year=year, datum=datum, m01ab=m01ab, m01ae=m01ae, n02ba=n02ba, n02be=n02be, n05c=n05c, r03=r03, r06=r06)
        pharma_table.save()
        return Response({"status": "ok", "message": "pharmasales data save successfully"})



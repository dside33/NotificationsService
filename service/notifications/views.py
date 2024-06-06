from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.views import View

from users.models import CustomUser
from .serializers import CustomUserSerializer

from .utils import send_email, check_json_file
from .permissions import HasAPIKeyAndIsAuthenticated

import json
import csv
import codecs


class MainPageView(View):
    def get(self, request):
        return render(request, 'main_page.html')
    

class JSONSendAPIView(APIView):

    permission_classes = [HasAPIKeyAndIsAuthenticated]
    
    def post(self, request, format=None):
        file_obj = request.FILES.get('file')
        
        is_correct, message_status = check_json_file(file_obj)

        if not is_correct:
            return Response({"error": message_status}, status=400)
        
        return Response({"status": "Success"}, status=200)
    

class CSVSendAPIView(APIView):
    
    def post(self, request, format=None):
        file_obj = request.FILES.get('file')  
        
        if not file_obj:
            return Response({"error": "No file provided."}, status=400)
        
        users_data = []
        try:
            # Читаем файл с указанием кодировки utf-8
            reader = csv.DictReader(codecs.iterdecode(file_obj, 'utf-8'))
            for row in reader:
                users_data.append(row)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
        
        
        # for user in users_data:
        #     if user.get('notification_method') == CustomUser.EMAIL:
        #         send_email.delay(user.get('notification_address'))
        
        return Response({"message": users_data}, status=200)



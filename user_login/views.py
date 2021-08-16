from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST',])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

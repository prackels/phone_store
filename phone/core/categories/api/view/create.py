from ...models import phone
from ..serializers import phoneserializer
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["POST"])
def create_phone(request):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer= phoneserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= HTTP_201_CREATED)
    if not serializer.is_valid:
        return Response(status= HTTP_400_BAD_REQUEST)
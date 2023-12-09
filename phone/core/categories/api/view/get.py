from ...models import phone
from ..serializers import phoneserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

@api_view(["GET"])
def ViewPhones(request):
    quary= phone.objects.all()
    serializer= phoneserializer(quary, many=True)
    
    return Response(serializer.data)
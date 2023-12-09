from rest_framework.decorators import api_view
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from rest_framework.response import Response
from ...models import phone

@api_view(["DELETE"])
def delete_phone(request, pk):
    try:
        phone_instance = phone.objects.get(pk=pk)
    except phone.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    phone_instance.delete()
    return Response(status=HTTP_204_NO_CONTENT)

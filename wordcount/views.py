from rest_framework.views import APIView
from .serializers import WordCountSerializer
from django.http.response import JsonResponse
from .models import DataStore
from rest_framework.response import Response


class TableDataView(APIView):

    def get_table(self, pk):
        try:
            response = DataStore.objects.get(id=pk)
            return response
        except:
            return JsonResponse("Url Does Not Exist", safe=False)

    def get(self, request, pk=None):
        try:
            if pk:
                data = self.get_table(pk)
                serializer = WordCountSerializer(data)
            else:
                data = DataStore.objects.all()
                serializer = WordCountSerializer(data, many=True)
            return Response(serializer.data)
        except:
            return JsonResponse("Item Does Not Exist", safe=False)

    def post(self, request):
        data = request.data
        serializer = WordCountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            data = DataStore.objects.all()
            serializer = WordCountSerializer(data, many=True)
            return Response(serializer.data)
        return JsonResponse("Failed to Add Data", safe=False)

    def put(self, request, pk=None):
        try:
            row_to_update = DataStore.objects.get(id=pk)
            serializer = WordCountSerializer(instance=row_to_update, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = DataStore.objects.all()
                serializer = WordCountSerializer(data, many=True)
                return Response(serializer.data)
            return JsonResponse("Failed to Update Student")
        except:
            return JsonResponse("Failed to Update Student", safe=False)

    def delete(self, request, pk=None):
        try:
            row_to_delete = DataStore.objects.get(id=pk)
            row_to_delete.delete()
            return JsonResponse("Row Deleted Successfully", safe=False)
        except:
            return JsonResponse("Failed to Delete Data", safe=False)
from rest_framework.response import Response
from rest_framework.views import APIView

from survey.serializers import SurveySerializer
from survey.models import Survey

class ListView(APIView):
    def get(self, request):
        data = SurveySerializer(Survey.objects.get(id=1)).data
        return Response(data)

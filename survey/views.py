from rest_framework.response import Response
from rest_framework.views    import APIView

from survey.serializers import SurveySerializer
from survey.models      import Survey


class ListView(APIView):
    def get(self, request):
        survey = Survey.objects.all()
        serializer = SurveySerializer(survey, many=True)
        return Response(serializer.data)

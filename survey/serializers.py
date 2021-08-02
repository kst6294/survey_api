from rest_framework import serializers

from survey.models import Survey, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(source='user.username', read_only=True)

    class Meta:
        model = Answer
        fields = ["content", "user"]

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("title", "answers")


class SurveySerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Survey
        fields = ("title", "question")

    def get_question(self, obj):
        questions = [question.title for question in Question.objects.filter(survey_id=obj.id)]
        return questions

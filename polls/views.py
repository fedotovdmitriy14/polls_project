from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from polls.models import Poll, Question, Choice, Answer
from polls.permissions import AdminOrReadOnly
from polls.serializers import PollSerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer


class PollViewset(viewsets.ModelViewSet):
    """Возвращат список опросов, позволяет их создавать/редактировать
        и удалять админам. Остальным польователям разрешен просмотр.
    """

    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    permission_classes = [AdminOrReadOnly]


class QuestionViewSet(viewsets.ModelViewSet):
    """Возвращат список вопросов, позволяет их создавать/редактировать
            и удалять админам. Остальным польователям разрешен просмотр.
        """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AdminOrReadOnly]


class ChoicesViewSet(viewsets.ModelViewSet):
    """Возвращат список выборов, позволяет их создавать/редактировать
            и удалять админам. Остальным польователям разрешен просмотр.
        """

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [AdminOrReadOnly]


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_relevant_polls(request):
    """Зарегистрированный пользователь может получить список актуальный
        опросов. Текущая дата сравниватеся с start_date и end_date опроса
    """

    polls= Poll.objects.filter(start_date__lte=timezone.now()).filter(end_date__gte=timezone.now())
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def answer_create(request):
    """Зарегестрированный пользователь может оставить отзыв"""

    serializer = AnswerSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        answer = serializer.save()
        return Response(AnswerSerializer(answer).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def answer_show(request, user_id):
    """Возвращает ответы конкретного пользователя

    Аргументы:
    user_id - числовой идентификатор пользователя
    """

    answers = Answer.objects.filter(user_id=user_id)
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)

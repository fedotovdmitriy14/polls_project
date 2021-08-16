from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'polls', views.PollViewset, basename='polls')
router.register(r'questions', views.QuestionViewSet, basename='questions')
router.register(r'choices', views.ChoicesViewSet, basename='choices')

urlpatterns = [
    path('', include(router.urls)),
    path('activepolls/', views.get_relevant_polls, name='relevant_poles'),
    path('answer/', views.answer_create, name='answer-create'),
    path('show/<int:user_id>', views.answer_show, name='answer_show'),
]
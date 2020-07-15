from django.urls import path

from .views import (
    home_view,
    question_detail_view,
    # question_create_view, 
)

urlpatterns = [
    path('', home_view, name='home'),
    path('question/<int:pk>/', question_detail_view, name='question-detail'),
    # path('question/create/', question_create_view, name='question-create'),
]

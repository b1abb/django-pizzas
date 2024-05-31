from django.urls import path

from .views import feedback, feedback_thank_you, goodLinks

urlpatterns = [
    path('', feedback, name='feedback'),
    path('feedback/thank_you/<int:feedback_id>/', feedback_thank_you, name='feedback_thank_you'),
    path('goodLinks', goodLinks, name='goodLinks'),
]

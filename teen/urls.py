from django.urls import path

from .views import TestView, ResultView
from .forms import PassTestForm

urlpatterns = [
    path('test_pass/', TestView.as_view([PassTestForm])),
    path('result/', ResultView.as_view())
]

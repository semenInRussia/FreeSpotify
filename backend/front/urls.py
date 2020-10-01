from django.urls import path

from front.views import TopView

urlpatterns = [
    path("", TopView.as_view(), name="view_top"),
]


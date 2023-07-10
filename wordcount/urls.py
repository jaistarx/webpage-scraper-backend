from django.urls import path
from .views import TableDataView, baseView

urlpatterns = [
    path("", baseView),
    path("tableview/", TableDataView.as_view()),
    path("tableview/<int:pk>/", TableDataView.as_view()),
]
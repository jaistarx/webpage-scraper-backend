from django.urls import path
from .views import TableDataView

urlpatterns = [
    path("tableview/", TableDataView.as_view()),
    path("tableview/<int:pk>/", TableDataView.as_view()),
]
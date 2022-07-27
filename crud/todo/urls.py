from django.urls import path

# importing views from views.py
from .views import TodoAppCreateView, TodoAppListView, TodoAppDetailView,TodoAppUpdateView

urlpatterns = [
    path("", TodoAppCreateView.as_view(), name='home'),
    path("list/", TodoAppListView.as_view(), name='list'),
    path("detail/<pk>/", TodoAppDetailView.as_view(), name='detail'),
    path("<pk>/update/", TodoAppUpdateView.as_view(), name='update'),
]
from django.urls import path
from .views import ListBoardView, BoardDetailView

urlpatterns = [
    path('all_announcements_list/', ListBoardView.as_view(), name='all_announcements_list'),
    path('announcement_id/<int:pk>', BoardDetailView.as_view(), name='announcement_detail'),
]
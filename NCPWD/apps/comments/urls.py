from rest_framework import routers
from django.urls import path
from .views import CommentViewSet, TopicCommentAPIView


router = routers.SimpleRouter()

router.register(r"comments", CommentViewSet)


urlpatterns = router.urls
urlpatterns.append(
    path('topics/<int:topic>/comments', TopicCommentAPIView.as_view(), name="topic_comments")
)

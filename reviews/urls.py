
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, LawyerReviewsAPIView, LawyerDetailWithReviewsAPIView

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('api/', include(router.urls)), 
    path('api/lawyers/<int:lawyer_id>/reviews/', LawyerReviewsAPIView.as_view(), name='lawyer-reviews'),
    path('api/lawyers/<int:lawyer_id>/', LawyerDetailWithReviewsAPIView.as_view(), name='lawyer-detail-with-reviews'),
]

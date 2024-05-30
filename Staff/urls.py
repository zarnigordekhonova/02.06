from .views import WorkersViewSet, JobsViewSet, CompanyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'workers', WorkersViewSet, basename='workers')
router.register(r'jobs', JobsViewSet, basename='jobs')
router.register(r'company', CompanyViewSet, basename='company')

urlpatterns = router.urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, StudentViewSet, add_student, student_list, random_student, random_student_result

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('api', include(router.urls)),
    path('add', add_student, name='add_student'),
    path('', student_list, name='student_list'),
    path('random', random_student, name='random_student'),
    path('random/result', random_student_result, name='random_student_result'),
]
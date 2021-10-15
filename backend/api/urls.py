
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import PersonList, PersonDetails



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/persons/', PersonList.as_view()),
    path('api/persons/<int:id>/', PersonDetails.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

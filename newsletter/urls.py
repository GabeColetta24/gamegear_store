from django.urls import path
from .views import newsletter_signup


# Newsletter app URL patterns
urlpatterns = [
    path('', newsletter_signup, name='newsletter_signup'),
]
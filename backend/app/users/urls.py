from django.urls import path

from app.users.views import MeInformation

app_label='users'

urlpatterns = [
    path('me/', MeInformation.as_view()),

]




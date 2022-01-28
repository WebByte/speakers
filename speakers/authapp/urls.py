from django.urls import path

import authapp
from .views import *
app_name = 'authapp'

urlpatterns = [
    # path('signup/', UserProfileCreationView.as_view()),  # POST
    # path('login/', UserProfileLoginView.as_view()),  # POST
    # path('logout/', UserProfileLogoutView.as_view()),  # POST
    #
    #
    # path('test/', TestView.as_view()),  # POST
    # path('delete/', UserProfileDeleteView.as_view()),  # POST

    path('login/', authapp.login, name='login'),
    # path('logout/', authapp.logout, name='logout'),
    # path('register/', authapp.register, name='register'),
    path('test/', test, name='test'),
    # path('edit/', authapp.edit, name='edit'),
    path('verify/<email>/<activationKey>/', authapp.veryfy, name='verify'),
]

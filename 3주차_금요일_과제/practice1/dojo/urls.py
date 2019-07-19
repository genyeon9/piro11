from django.urls import path
from . import views

urlpatterns = [
    path('sum/<int:x>', views.mysum, name='mysum'),
    path('sum/<int:x>/<int:y>', views.mysum, name='mysum'),
    path('sum/<int:x>/<int:y>/<int:z>', views.mysum, name='mysum'),

]
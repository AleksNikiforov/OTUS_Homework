from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('design/', design, name='design'),
    path('examination/', examination, name='examination'),
    path('poc/', poc, name='poc'),
    path('install/', install, name='install'),
    path('comissioning/', comissioning, name='comissioning'),
    path('accept/', accept, name='accept'),
    path('migration/', migration, name='migration'),
    path('other_jobs/', other_jobs, name='other_jobs'),
    path('subcontractor/', subcontractor, name='subcontractor'),
    path('other/', other, name='other'),
    path('unenxpected/', unenxpected, name='unenxpected'),
    path('business_trip/', business_trip, name='business_trip'),
    path('rates/', rates, name='rates'),
]
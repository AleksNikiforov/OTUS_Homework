from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),

    

    path('design-list/', DesignListView.as_view(), name='Design'),
    path('design-detail/<int:pk>/', DesignListView.as_view(), name='Design_detail'),
    path('poc-list/', PocListView.as_view(), name='Poc'),
    path('poc-detail/<int:pk>/', PocListView.as_view(), name='Poc_detail'),
    path('install-list/', InstallListView.as_view(), name='Install'),
    path('install-detail/<int:pk>/', InstallListView.as_view(), name='Install_detail'),
    path('comissioning-list/', ComissioningListView.as_view(), name='Comissioning'),
    path('comissioning-detail/<int:pk>/', InstallListView.as_view(), name='Comissioning_detail'),
    path('accept-list/', AcceptListView.as_view(), name='Accept'),
    path('accept-detail/<int:pk>/', AcceptListView.as_view(), name='Accept_detail'),
    path('migration-list/', MigrationListView.as_view(), name='Migration'),
    path('migration-detail/<int:pk>/', MigrationListView.as_view(), name='Migration_detail'),
    path('other_jobs-list/', Other_jobstionListView.as_view(), name='Other_jobs'),
    path('other_jobs-detail/<int:pk>/', Other_jobstionListView.as_view(), name='Other_jobs_detail'),
    path('subcontractor-list/', SubcontractorListView.as_view(), name='Subcontractor'),
    path('subcontractor-detail/<int:pk>/', SubcontractorListView.as_view(), name='Subcontractor_detail'),
    path('other-list/', OtherListView.as_view(), name='Other'),
    path('other-detail/<int:pk>/', OtherListView.as_view(), name='Other_detail'),
    path('unenxpected-list/', UnenxpectedListView.as_view(), name='Unenxpected'),
    path('unenxpected-detail/<int:pk>/', UnenxpectedListView.as_view(), name='Unenxpected_detail'),
    path('business_trip-list/', Business_tripListView.as_view(), name='Business_trip'),
    path('business_trip-detail/<int:pk>/', Business_tripListView.as_view(), name='Business_trip_detail'),
    path('rates-list/', RatesListView.as_view(), name='Rates'),
    path('rates-detail/<int:pk>/', RatesListView.as_view(), name='Rates_detail'),
]

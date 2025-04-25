from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountByMonth, MultilineIncidentTop3Country, multipleBarbySeverity
from fire import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    # Chart URLs
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountByMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multipleBarChart/', multipleBarbySeverity, name='chart'),

    # Map URLs
    path('stations-map/', views.map_station, name='map-station'),
    path('incidents-map/', views.map_incident, name='map-incident'),

    # Locations URLs
    path('locations/', views.LocationListView.as_view(), name='locations_list'),
    path('locations/create', views.LocationsCreateView.as_view(), name='locations_create'),
    path('locations/update/<pk>/', views.LocationsUpdateView.as_view(), name='locations_update'),
    path('locations/delete/<pk>/', views.LocationsDeleteView.as_view(), name='locations_delete'),

    # Incident URLs
    path('incidents/', views.IncidentListView.as_view(), name='incidents_list'),
    path('incidents/create', views.IncidentCreateView.as_view(), name='incidents_create'),
    path('incidents/update/<pk>/', views.IncidentUpdateView.as_view(), name='incidents_update'),
    path('incidents/delete/<pk>/', views.IncidentDeleteView.as_view(), name='incidents_delete'),
]
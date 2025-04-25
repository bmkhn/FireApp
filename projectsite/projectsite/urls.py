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

    # Fire Station URLs
    path('firestations/', views.FireStationListView.as_view(), name='firestations_list'),
    path('firestations/create', views.FireStationCreateView.as_view(), name='firestations_create'),
    path('firestations/update/<pk>/', views.FireStationUpdateView.as_view(), name='firestations_update'),
    path('firestations/delete/<pk>/', views.FireStationDeleteView.as_view(), name='firestations_delete'),

    # Firefighters URLs
    path('firefighters/', views.FirefighterListView.as_view(), name='firefighters_list'),
    path('firefighters/create', views.FirefighterCreateView.as_view(), name='firefighters_create'),
    path('firefighters/update/<pk>/', views.FirefighterUpdateView.as_view(), name='firefighters_update'),
    path('firefighters/delete/<pk>/', views.FirefighterDeleteView.as_view(), name='firefighters_delete'),

    # Fire Truck URLs
    path('firetrucks/', views.FireTruckListView.as_view(), name='firetrucks_list'),
    path('firetrucks/create', views.FireTruckCreateView.as_view(), name='firetrucks_create'),
    path('firetrucks/update/<pk>/', views.FireTruckUpdateView.as_view(), name='firetrucks_update'),
    path('firetrucks/delete/<pk>/', views.FireTruckDeleteView.as_view(), name='firetrucks_delete'),

    # Weather Conditions URLs
    path('weatherconditions/', views.WeatherConditionsListView.as_view(), name='weatherconditions_list'),
    path('weatherconditions/create', views.WeatherConditionsCreateView.as_view(), name='weatherconditions_create'),
    path('weatherconditions/update/<pk>/', views.WeatherConditionsUpdateView.as_view(), name='weatherconditions_update'),
    path('weatherconditions/delete/<pk>/', views.WeatherConditionsDeleteView.as_view(), name='weatherconditions_delete'),
]
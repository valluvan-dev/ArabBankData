from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('ccii/',instant_market_place,name="ccii"),
    path('sales/',sales_view,name="sales"),
    path('get_sample_data/', get_sample_data, name='get_sample_data'),
    # path('custom_query/', custom_query, name='custom_query'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_red),
    path('search', views.search_catalog_ru),
    path('search-uz', views.search_catalog_uz),

    path('search-star-ru', views.search_star_ru),
    path('search-star-uz', views.search_star_uz),

    path('search-lead-ru', views.search_leads_ru),
    path('search-lead-uz', views.search_leads_ru),

    path('search-duty-artist-ru', views.search_duty_artists_ru),
    path('search-duty-artist-uz', views.search_duty_artists_uz),

    path('ru/all-catalogs', views.get_all_catalog),
    path('uz/all-catalogs', views.get_all_catalog_uz),

    path('ru/star/<str:pk>', views.get_current_star_ru),
    path('uz/star/<str:pk>', views.get_current_star_uz),

    path('ru/lead/<str:pk>', views.get_current_lead_ru),
    path('uz/lead/<str:pk>', views.get_current_lead_uz),

    path('ru/duty-artist/<str:pk>', views.get_current_duty_artist_ru),
    path('uz/duty-artist/<str:pk>', views.get_current_duty_artist_uz),

    path('ru/card/<str:pk>', views.get_current_card_ru),
    path('uz/card/<str:pk>', views.get_current_card_uz),

    path('ru/catalog/all-stars', views.get_all_stars),
    path('uz/catalog/all-stars', views.get_all_stars_uz),

    path('ru/catalog/all-duty-artists', views.get_all_duty_artists_ru),
    path('uz/catalog/all-duty-artists', views.get_all_duty_artists_uz),

    path('ru/catalog/all-leads', views.get_all_leading_ru),
    path('uz/catalog/all-leads', views.get_all_leading_uz),

    path('ru/catalog/<str:pk>', views.catalog_page_ru),
    path('uz/catalog/<str:pk>', views.catalog_page_uz),

    path('count', views.count_ads),
    path('count_catalog', views.count_ads_catalog),

    path('<str:pk>', views.main_page),
]

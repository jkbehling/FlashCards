from django.urls import path
#from django.conf.urls import url
from flash_cards_app import views
from flash_cards_app.models import Card

# home_list_view = views.HomeListView.as_view(
#     queryset=Card.objects.order_by("front")[:5],
#     context_object_name="card_list",
#     template_name="flashcards/home.html",
# )
urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.deck, name="decks"),
    path("about/", views.about, name="about"),
    path('card_delete/<int:id>', views.card_delete, name='card_delete'),
    path('deck_delete/<int:id>', views.deck_delete, name='deck_delete'),
    path('view_deck/<int:id>', views.view_deck, name="view_deck"),
    path('card_list/<int:id>', views.card_list, name="card_list"),
    path('card_Edit/<int:id>', views.card_Edit, name="card_Edit"),
    path('card_New/<int:id>', views.card_New, name='card_New'),
    path('carousel', views.carousel, name='carousel'),
    path('deck_new/', views.deck_new, name="deck_new"),
    path('deck_edit/<int:id>', views.deck_edit, name='deck_edit'),
    path('deck_list/', views.deck_list, name="deck_list"),
    path('card_test/<int:id>', views.card_test, name="card_test"),
]
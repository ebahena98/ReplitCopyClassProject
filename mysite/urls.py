from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# Import views for personal app
from personal.views import (
    home_screen_view,
)
# Import views for landing pages app
from landing_pages.views import (
    about_view,
    help_view,
    safety_view,
    contact_view,
    buyers_view,
    sellers_view,
    starting_view,
    rules_view,
    your_account_view
)

# Importing views for URL routing
from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,
)

from chatbox.views import (
    lobby_screen_view,
    room_screen_view,
)

# URL configuration for mysite
urlpatterns = [
    # Admin interface URL
    path('admin/', admin.site.urls),

    path('lobby/', lobby_screen_view, name='lobby'),

    path('room/', room_screen_view, name='room'),

    path('post/', include('post.urls', 'post')),

    # Home page URL
    path('', home_screen_view, name = 'home'),

    # User registration URL
    path('register/', registration_view, name = 'register'),

    # User logout URL
    path('logout/', logout_view, name = 'logout'),

    # User login URL
    path('login/', login_view, name = 'login'),

    # User account URL
    path('account/', account_view, name = 'account'),

    path('must_authenticate/', must_authenticate_view, name = 'must_authenticate'),

    # Password change reset URLs
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'registration/password_change_done.html'), 
        name = 'password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'registration/password_change.html'), 
        name = 'password_change'),

    # Password reset URLs
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_done.html'),
        name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name = 'password_reset'),  
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'),
        name = 'password_reset_complete'),

    path('about/', about_view, name = 'about'),

    path('help/', help_view, name = 'help'),
    path('safety/', safety_view, name = 'safety'),
    path('contact/', contact_view, name = 'contact'),
    path('buyers/', buyers_view, name = 'buyers'),
    path('sellers/', sellers_view, name = 'sellers'),
    path('starting/', starting_view, name = 'starting'),
    path('rules/', rules_view, name = 'rules'),
    path('your-account/', your_account_view, name = 'your_account'),

]

# Static and media files served during development as DEBUG is set to TRUE
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

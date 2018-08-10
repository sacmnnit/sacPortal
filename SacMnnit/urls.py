"""sacMnnit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static  
from SacMnnit.views import ( home,president,contact,downloads,contactmail )
from Technical.views import ( avishkar,technological, )
from Cultural.views import ( classical,culrav,literary,eloquence,cultural  )
from Athletics.views import ( yoga,annual_athletics,josh,games,athletics )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

	path('avishkar', avishkar, name='avishkar'),
	path('technological', technological, name='technological'),

	path('culrav', culrav, name='culrav'),
	path('literary', literary, name='literary'),
	path('classical', classical, name='classical'), 
	path('eloquence', eloquence, name='eloquence'),
	path('cultural', cultural, name='cultural'),
	

	path('josh', josh, name='josh'),
	path('athletics', athletics, name='athletics'),
	path('annual_athletics', annual_athletics, name='annual_athletics'),
	path('games', games, name='games'),
	path('yoga', yoga, name='yoga'),

	path('downloads', downloads, name='downloads'),
	path('president', president, name='president'),
	path('contact', contact, name='contact'),
	path('contactmail', contactmail, name='contactmail'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)





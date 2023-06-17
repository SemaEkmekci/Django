# print(django.get_version()) -> sürüm öğrenmek için

# django-admin startproject catalog -> proje oluşturmak için

# cd catalog ->catalog klasörüne gidiyoruz.

# django-admin help -> komutlara ulaşabiliriz

# python manage.py help

# python manage.py runserver -> server ı çalıştırdık

# python manage.py startapp pages -> pages adında bir modüler proje oluşturur.

# Eklemek istediğimiz modüler proje root klasördeki (catalog) settings.py dosyasına;
# INSTALLED_APPS = ["pages.apps.PagesConfig",....] listesine bu şekilde eklenir.

# from django.http import HttpResponse views.py dosyasında request oluşturmak için bu kütüphane eklenir.
# views.py dosyasına fonksiyon yazılır.
# pages klasörünün içine urls.py dosyası eklenir.
# Oluşturulan urls.py dosyasının içine
# from django.urls import path
# from . import views


# # http://127.0.0.1:8000/

# urlpatterns = [
#     path("", views.index, name="index"),]

# views.py dosyasındaki fonksiyon çağırılmak için yazılır.

# HTML SAYFASINI DAHİL ETME
# 'templates' adında ayrı bir klasör oluşturup içine pages klasörü oluşturuyoruz.
# catalog klasörü altındaki settings.py dosyasına;
# "DIRS": [os.path.join(BASE_DIR), "templates"], ekliyoruz.

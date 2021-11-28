# Django-QuizApp-API
------------------------------------------------
env kurup active ediyoruz
$ python -m venv qenv2
$ source ./qenv2/Scripts/activate
------------------------------------------------
$ python -m pip install django
Django Framework kuruyoruz
------------------------------------------------
$ python -m pip install djangorestframework
django rest framework kuralim
Öncelikle RESTFull API Nedir? Bunu öğrenmemiz gerekiyor, Restfull API bir web servisi üzerinde connect olmuş ve birbiriyle haberleşme yapan iki makine arasında translator (çevirmen) görevi görmesini sağlar. Rest API sunucunun uygulamadan veri alabilmesini sağlamaktadır, bu nedenle bu veriyi çekip işlemek açısından günümüzde son derecede kullanışlıdır. Bunlar Masaüstü, iOS, Android gibi uygulamalar olabilir burada bir sınırlamamız bulunmamakta. Django Rest Framework (DRF) REST API kullanmamız için bize olanak sağlayan bir framework ve biz bunu kullanacağız. Pekala neden DRF kullanıyoruz?
1- Diğer framework’lere göre çok daha kullanışlı olması. (PHP Slim vs.)
2- Authentication (kimlik doğrulama) bulundurması.
3- ORM ve ORM haricicndeki veri depolama veri kaynaklarını bulundurabilmesi.
( Bir çok avantajını dökümantasyon üzerinden görebiliriz :)) Çünkü burada sözel olarak bahsettiğimden çok fazlasını dökümantasyonda ve internette araştırabileceğiniz uygulamalar üzerinden rahatlıkla görüntüleyebilirsiniz..
------------------------------------------------
$ python -m pip install python-decouple 
Tüm projelerde kimseyle paylaşmak istemediğiniz hassas verilere sahip olabilir. Veriler, e-posta ana bilgisayarı, e-posta parolaları, gizli anahtar, hata ayıklama ve diğer hassas veriler olabilir. Bunları saklamanın ve bunlara erişmenin en iyi yolu Python Decouple .
------------------------------------------------
$ pip freeze > requirements.txt
asgiref==3.4.1
Django==3.2.9
djangorestframework==3.12.4
python-decouple==3.5
pytz==2021.3
sqlparse==0.4.2
Bir projeyi başkalarıyla paylaşıyorsanız, bir yapı sistemi kullanıyorsanız veya projeyi bir ortamı geri yüklemeniz gereken başka bir konuma kopyalamayı planlıyorsanız, projenin gerektirdiği dış paketleri belirtmeniz gerekir. Önerilen yaklaşım, bağımlı paketlerin gerekli sürümlerini yükleyen pip için bir komut listesi içeren bir gereksinim.txt dosyası (readthedocs.org) kullanmaktır . En yaygın komut, pip freeze > requirements.txtbir ortamın mevcut paket listesini gereksinimler.txt dosyasına kaydeden komuttur 
------------------------------------------------
.gitignore dosyasini düzenle
------------------------------------------------
$ django-admin startproject quiz_prj .
projemizi olusturalim
------------------------------------------------
Ekle
INSTALLED_APPS = [
    'rest_framework',
]
------------------------------------------------
.env olusturalim
settings.py deki SECRET_KEY i tirnaklari kaldirarak kopyala 
.env dosyasina yapistir
settings.py a git from decouple import config 
SECRET_KEY = config('SECRET_KEY') yaz
------------------------------------------------
$ python manage.py startapp quiz
APP olusturalim
INSTALLED_APPS = [
    'rest_framework',
    'quiz',
]
Aslinda baska bir ulasma yolu daha var 
class QuizConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz'
app.py altinda QuisConfig araciligiyla da ulasilir.
INSTALLED_APPS = [
    'rest_framework',
    'quiz.apps.QuizConfig',
]
------------------------------------------------
$ python manage.py migrate
Admin paneline ulasmamiz gerekiyor. SuperUser olusturalim. Bunun icin de djangonun default olarak verdigi modelleri database lere kaydetmem gerekiyor. Bana hazir tablolar db ye kuruldu.
------------------------------------------------
$ python manage.py createsuperuser
$ python manage.py runserver
http://127.0.0.1:8000/admin/ 
sifreyi gir
------------------------------------------------
quiz>models.py
Simdi model olusturacagiz. Frontend ne istiyorsa ona uygun endpointler döndürmem gerekiyor. Kategori , Ders ve Sorular diye modeller olusturucaz. Sorulari olusturmak icin bir arayüz olusturmayacagiz.Cünkü admin icin hazir bir panelimiz var. Oturup da admin icin bir panel yazmamiza gerek yok.Admin yetkili bir kullanici olusturup admin panele girip sorulari olusturmasini saglayabiliriz.Bunu django admin panelinden yapacagiz. Djang admin panelinde customization yapacagiz. Admin paneli basli basina bir derya. Customization veya override yapilabilir.

class Update(models.Model):...
class Category(models.Model):...
class Quiz(models.Model):...
class Questions(Update):...
class Answer(Update):...

$ python manage.py makemigrations
$ python manage.py migrate
database e modelleri kaydetmek icin

quiz > admin.py DB olustuktan sonra ben bunlari admin paneline register etmem gerekiyor.
from .models import Category, Quiz, Question, Answer ... 
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------
------------------------------------------------


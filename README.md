# Django-QuizApp-API
models - admin - (urls) - serializers - views - urls
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

database e modellerim geldi. Simdi kategorileri veya sorulari manuel eklemem gerekiyor. Fakat tek tek hepsini eklemek zor. Ic ice gecmis veriler var. Bunlarin takibini ve girisini kolaylastirmak icin bir paket mevcut.(TabularInline). 
https://django-nested-admin.readthedocs.io/en/latest/quickstart.html
https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
TabularInline kullanarak 2 modeli ic ice gösterebiliriz. Girisler kolaylasmis olur. 
$ python -m pip install django-nested-admin
$ pip freeze > requirements.txt
INSTALLED_APPS = [
    'rest_framework',
    'quiz',
    'nested_admin',
]

quiz_prj > urls.py a path ekle
urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls'))
]

Geriye kalan islemler admin.py da düzenlendi.

------------------------------------------------

Geldik endpoint belirlemeye. Su an 3 tane endpoint belirleyecegim. Frontendde kategorileri koyacaklar. Kategoriyi sectigi zaman kullanici o kategorilerin icerisinde hangi quizler var onlari görecek. Quizi sectiginde de quiz icerisindeki sorulara ulasacak. Yapmak istedigimiz sey bu.Fakat öncelikle urls leri ayarlamam gerekiyor.

quiz icine urls.py olusturalim.

quiz_prj > urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    path('quiz' , include('quiz.urls')),
]

quiz>urls.py 
from django.urls import path
urlpatterns = [
    path('', , name = ''),
]

------------------------------------------------
quiz icerisine serializers.py olusturalim
Önce söyle bir sey yapacagiz. Category endpoint i icin, öncelikle bana category_name dönsün, id sini dönsün ve icinde kac tane kategori var onu söylesin. Genelde functionbased kullaniliyor fakat biz bu projede classedbased kullanacagiz. Bazi methodlari override edecegiz. GenericViews ler üzerinden gidecegiz endpointlerde. Biz projede update delete yazmayacagiz. Liste seklinde gönderecegiz frontende. Gercek projelerde de Rest-framework su sekilde kullanilir. Mesela bir API den veri cekiyorsunuz. O veri frontend ne istemisse onu listelemek icin gönderilir. Genelde create update cok yapilmiyor. API endpointleri Frontende List olarak gönderiyoruz. 
------------------------------------------------
#4lü
quiz > models.py a git
class Category altina sunu ekle
    @property
    def quiz_count(self):
        return self.quiz_set.count()
bu bana Cateroryi döndürürken Quiz icinde kac tane obje var onu gösterecek. 

quiz > serializers.py a git CategorySerializer yaz
from rest_framework import serializers
from .models import Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id' , 
            'name',
            'quiz_count'
        ) 

quiz > views.py a git CategorySerializersi import et CategoryList yaz
from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer 
# Create your views here.
class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

quiz > urls.py a git viewsteki Category i import et
from django.urls import path
from .views import CategoryList
urlpatterns = [
    path('', CategoryList.as_view(), name = 'category'),
]

------------------------------------------------
#4lü
quiz > models.py a git
class Quiz altina sunu yaz 
    @property
    def question_count(self):
        return self.question_set.count()
bu bana Quiz döndürürken kac tane question var onu dönecek.

quiz > serializers.py a git CategoryDetailSerializer yaz
class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = (
            'title',
            'question_count',
            )

quiz > views.py a git CategoryDetailSerializer import et CategoryDetail yaz
from .models import Category , Quiz
class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs['category'] #backend #frontend
        queryset = queryset.filter(category__name=category) # categiry modelindeki name ne ise url den aldigim isme esitle ve bunu filtrele. Benim Quiz imde categoryler benim numara olarak kayitli. Foreign_key iliskisinden dolayi oradaki id sini verir. Benim bu id leri bilmem gerekiyor filtreleme yapmam icin. Bunu quizin icindeki category fieldinden aliyorum. 
        return queryset   


quiz > urls.py a git viewsteki CategoryDetail i import et
path('<category>', CategoryDetail.as_view(), name = 'category-detail'),

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


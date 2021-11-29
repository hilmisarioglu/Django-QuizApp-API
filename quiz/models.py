from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Update(models.Model):
    updated = models.DateTimeField(auto_now_add=True) #update ettiginde tarih kaydeder
    class Meta:
        abstract = True # DB ye kaydetmez
    
class Category(models.Model):
    name = models.CharField(max_length=100 , verbose_name = 'Category Name' )
    #verbose_name yazarak admin panelini override ederek nasil gözükmesini istiyorsak onu gösterebiliriz.Hem verbose_name hem de verbose_name_plural, nesneleri insan tarafından okunabilir hale getirmenin veya onları insan tarafından okunabilir bir noktaya dönüştürmenin yollarıdır.
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    @property
    def quiz_count(self):
        return self.quiz_set.count()

class Quiz(models.Model):
    title = models.CharField(max_length=100 , verbose_name = 'Quiz Title')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # Bu, başvurulan nesne silindiğinde benimsenecek davranıştır . Django'ya özgü değildir; bu bir SQL standardıdır. Django'nun SQL'in üzerinde kendi uygulaması olmasına rağmen. Böyle bir olay meydana geldiğinde yapılması gereken yedi olası eylem vardır:
    # CASCADE: Başvurulan nesne silindiğinde, ona referansları olan nesneleri de silin (örneğin bir blog gönderisini kaldırdığınızda, yorumları da silmek isteyebilirsiniz). SQL eşdeğeri: CASCADE.
    # PROTECT: Başvurulan nesnenin silinmesini yasaklayın. Silmek için, ona manuel olarak başvuran tüm nesneleri silmeniz gerekir. SQL eşdeğeri: RESTRICT
    # RESTRICT: (Django 3.1'de tanıtıldı) SQL'inkiyle daha doğru bir şekilde PROTECTeşleşen benzer davranış RESTRICT. ( Django dokümantasyon örneğine bakın 
    # SET_NULL: Başvuruyu NULL olarak ayarlayın (alanın boş olmasını gerektirir). Örneğin, bir Kullanıcıyı sildiğinizde, blog gönderilerine yaptığı yorumları saklamak isteyebilirsiniz, ancak bunun anonim (veya silinmiş) bir kullanıcı tarafından gönderildiğini söyleyebilirsiniz. SQL eşdeğeri: SET NULL.SET_DEFAULT: Varsayılan değeri ayarlayın. SQL eşdeğeri: SET DEFAULT.SET(...): Belirli bir değeri ayarlayın. Bu, SQL standardının bir parçası değildir ve tamamen Django tarafından işlenir.DO_NOTHING: Muhtemelen çok kötü bir fikir çünkü bu, veritabanınızda bütünlük sorunları yaratacaktır (gerçekte var olmayan bir nesneye atıfta bulunur). SQL eşdeğeri: NO ACTION. (2)
    # Örneğin PostgreSQL belgelerine de bakın .
    # Çoğu durumda, CASCADEbeklenen davranıştır, ancak her ForeignKey için, bu durumda beklenen davranışın ne olduğunu her zaman kendinize sormalısınız. PROTECTve SET_NULLgenellikle yararlıdır. Olmaması CASCADEgereken yeri ayarlamak , yalnızca tek bir kullanıcıyı silerek tüm veritabanınızı kademeli olarak silebilir.
    date_created = models.DateTimeField(auto_now_add=True)
    #create edildiginde bir kere olusturuyor
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Quizzes'
        
    @property
    def question_count(self):
        return self.question_set.count()

class Question(Update):
    SCALE = (
        (0 , 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Advanced'),
    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, verbose_name= 'Question')
    # title icine blank=True , null=True yazabilirdik.blank=True Admin panelinde bos birakabilirsin demek. Stringlerde null=True otomatik geliyor tekrardan yazmaniza gerek yok. null=True DB ye null olarak kaydedilmesini saglar. DateTimeField veya IntegerField larda blank=True yazdiysak null=True da ister. 
    difficulty = models.IntegerField(choices = SCALE)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Answer(Update):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=250, verbose_name= 'Answer')
    is_right = models.BooleanField(default=False)

    #django-abstract-models inheritance diye bir kavram var. Örnegin iki farkli class ta updated isminde ayi sekilde kullandigim field im var. Bu daha büyük modeller icin daha fazla kullanilacak demektir.Tekrar tekrar yazmaya gerek yok.Ortak kullanilan fieldlari bir classta yazariz bu db ye kaydedilmez. Daha sinra bu classttan inherit edilir.
    def __str__(self):
        return self.answer_text
    
    
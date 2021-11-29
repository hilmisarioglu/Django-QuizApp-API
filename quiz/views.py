from django.shortcuts import render
from rest_framework import generics
from .models import Category , Quiz
from .serializers import CategorySerializer , CategoryDetailSerializer
# Create your views here.
class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    
    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs['category'] #backend #frontend
        queryset = queryset.filter(category__name=category) # categiry modelindeki name ne ise url den aldigim isme esitle ve bunu filtrele. Benim Quiz imde categoryler benim numara olarak kayitli. Foreign_key iliskisinden dolayi oradaki id sini verir. Benim bu id leri bilmem gerekiyor filtreleme yapmam icin. Bunu quizin icindeki category fieldinden aliyorum. 
        return queryset   
from .models import *
from .serializers import * 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
'''
READ = GET
CREATE = POST
DELETE = DELETE
UPDATE = PUT
'''
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        articles =  Article.objects.all() # article 객체 가져오기
        serializer = ArticleListSerializer(articles, many = True)
        # many = True 단일 데이터가 아니라 데이터 덩어리가 넘어온다(쿼리 셑으로 넘어옴)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # 유효하다면
            serializer.save() #저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article =  Article.objects.get(pk=article_pk) # article 객체 가져오기
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # many = True 단일 데이터가 아니라 데이터 덩어리가 넘어온다(쿼리 셑으로 넘어옴)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid(raise_exception=True): # 유효하다면
            serializer.save() #저장
            return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
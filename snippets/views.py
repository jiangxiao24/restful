from django.shortcuts import render

# Create your views here.

from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from django.shortcuts import render,HttpResponse,redirect


def index(request):
    user0 = User.objects.get(username='jiangqijun')
    print(user0)
    # user = User(username='root', password='root', email='root@163.com')
    # user.save()
    snippet = Snippet(owner=user0,code='foo = "bar"\n')
    snippet.save()
    user2 = User.objects.get(username='root')
    snippet2 = Snippet(owner=user2,code='print("hello, world")\n')
    snippet2.save()
    serializer_context = {
        'request': request,
    }
    serializer = SnippetSerializer(snippet, context=serializer_context)
    print('#######################')
    print(type(serializer.data))
    print(serializer.data)
    """
    <class 'rest_framework.utils.serializer_helpers.ReturnDict'>
    {'id': 34, 'title': '', 'code': 'foo = "bar"\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
    """
    content = JSONRenderer().render(serializer.data) #把字典类型转化为字节流
    print('#######################')
    print(type(content))
    print(content)
    """
    <class 'bytes'>
    b'{"id":31,"title":"","code":"foo = \\"bar\\"\\n","linenos":false,"language":"python","style":"friendly"}'
    """
    import io
    stream = io.BytesIO(content)
    data = JSONParser().parse(stream) #把字节流转换为字典类型
    print('#######################')
    print(type(data))
    print(data)
    """
    <class 'dict'>
    {'id': 31, 'title': '', 'code': 'foo = "bar"\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
    """
    serializer_context2 = {
        'request': request,
    }
    serializer2=SnippetSerializer(data=data,context=serializer_context2)
    if serializer2.is_valid():
        serializer2.save()
    serializer3=SnippetSerializer(Snippet.objects.all(), many=True)
    print('#######################')
    print(type(serializer3)) #<class 'rest_framework.serializers.ListSerializer'> 列出所有的值
    print(serializer3.data)
    #Snippet.objects.all().delete()
    return render(request, 'index.html')


# @csrf_exempt #不需要做csfr校验
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     # if request.method == 'GET':
#     #     snippets = Snippet.objects.all()
#     #     serializer = SnippetSerializer(snippets, many=True)
#     #     #return JsonResponse(serializer.data, safe=False)
#     #     return render(request, 'snippets_list.html')
#
#     # elif request.method == 'POST':
#     #     data = JSONParser().parse(request)
#     #     serializer = SnippetSerializer(data=data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return JsonResponse(serializer.data, status=201)
#     #     return JsonResponse(serializer.errors, status=400)
#     if request.method == 'POST':
#         title = request.POST.get('title', None)
#         code = request.POST.get('code', None)
#         return redirect('/index/')
#     return render(request, 'snippets_list.html')


# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer


@api_view(['GET','POST'])
def user_list(request, format=None):
    if request.method == 'GET':
        user = User.objects.all()
        print(user)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serilaizer = UserSerializer(user)
        return Response(serilaizer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serilaizer = UserSerializer(user, data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
        return Response(serilaizer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     if request.method == 'GET':
#         snippet = Snippet.objects.all()
#         serializer = SnippetSerializer(snippet, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format=None):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer,UserSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import json
# from collections import OrderedDict
#
#
# class UserList(APIView):
#     def get(self, request):
#         user = User.objects.all()
#         serializer = UserSerializer(user, many= True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserDetail(APIView):
#     def get_obj(self,pk):
#         try:
#             user = User.objects.get(pk=pk)
#             return user
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk):
#         serializer = UserSerializer(self.get_obj(pk))
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, pk):
#         user = self.get_obj(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         user = self.get_obj(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# # class JsonCustomEncoder(json.JSONEncoder):
# #     def default(self, field):
# #         if isinstance(field, OrderedDict):
# #             return {'code': field.code, 'messgae': field.message}
# #         else:
# #             return json.JSONEncoder.default(self, field)
#
#
# class Snippets_list(APIView):
#     def get(self, request, format=None):
#         snippet = Snippet.objects.all()
#         serializer = SnippetSerializer(snippet, many=True)
#         # d =serializer.data
#         # print(type(d)) #'rest_framework.utils.serializer_helpers.ReturnList'
#         # import json
#         # obj = d[0]
#         # print(type(json.dumps(obj, cls=JsonCustomEncoder)))
#         # obj1 = json.dumps(obj, cls=JsonCustomEncoder)
#         #return  render(request, 'snippets_list.html',{'obj':obj1})
#         #return HttpResponse(obj1)
#         return Response(serializer.data)
#
#     def post(self, request, fromat=None):
#         serializer = SnippetSerializer(data=request.data)
#         print(serializer.is_valid())
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class Snippet_detail(APIView):
#     def get_obj(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             return Http404
#
#     def get(self,request, pk, format=None):
#         snippet = self.get_obj(pk=pk)
#         print(111111111111111111)
#         print(type(snippet))
#         print(snippet)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         serializer = SnippetSerializer(self.get_obj(pk=pk), data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_obj(pk=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer,UserSerializer
# from rest_framework import mixins
# from rest_framework import generics
#
#
# class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request,*args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request,*args,**kwargs)
#
#
# class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return  self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# """
# 我们使用GenericAPIView构建了我们的视图，并且用上了ListModelMixin和CreateModelMixin。
# 基类提供核心功能，而mixin类提供.list()和.create()操作。然后我们明确地将get和post方法绑定到适当的操作
#
# """
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# """
# 使用GenericAPIView类来提供核心功能，并添加mixins来提供.retrieve()），.update()和.destroy()操作
# """
#
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer,UserSerializer
# from rest_framework import generics
# from django.contrib.auth.models import User
# from snippets.permissions import IsOwnerOrReadOnly
# from rest_framework import permissions
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     #这里表示在snippet中的用户是登录的用户而不是传入的请求用户
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#     #IsAuthenticatedOrReadOnly:设置只用经过身份认证的用户(登陆)可以进行读写，否则执行访问get方法
#     #IsOwnerOrReadOnly:自定义的IsOwnerOrReadOnly表示只用创建的用户才能够进行修改
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     #这里表示在snippet中修改后的用户是登录的用户而不是传入的请求用户
#     def perform_update(self, serializer):
#         serializer.save(owner=self.request.user)
#
#     # IsAuthenticatedOrReadOnly:设置只用经过身份认证的用户(登陆)可以进行读写，否则执行访问get方法
#     # IsOwnerOrReadOnly:自定义的IsOwnerOrReadOnly表示只用创建的用户才能够进行修改
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
#
#
#
#
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse
# from rest_framework import renderers, generics
# from rest_framework.response import Response
#
#
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response(
#         {
#             'user': reverse('user-list', request=request, format=format),
#             'snippets': reverse('snippet-list', request=request, format=format) #reverse里面的名字是url中的命名空间
#         }
#     )
#
#
# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     #这里的渲染器把原本的html原本渲染为页面
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)


from snippets.models import Snippet
from rest_framework import viewsets
from snippets.serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import permissions,renderers
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    """
    @action()
    action装饰器可以接收两个参数：
    methods: 声明该action对应的请求方式，列表传递
    detail: 声明该action的路径是否与单一资源对应，及是否是xxx/<pk>/action方法名/
        True 表示路径格式是xxx/<pk>/action方法名/
        False 表示路径格式是xxx/action方法名/
    """

    @action(detail=True, permission_classes=(permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,),
            renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

        #设置为false时使用
        #return Response({'status': False, 'code': 3001, 'data': {}, 'message': 'eclipse 文件不存在,请联系平台人员!'})

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



from restful.tasks import add


def test(request):
    result = add.delay(2, 3)
    return render(request, 'test.html')

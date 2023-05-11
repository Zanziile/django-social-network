from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import PostSerializer
from .models import Post
from .forms import PostForm


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_create(requset):
    form = PostForm(requset.data)

    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = requset.user
        post.save()

    return JsonResponse({'hello': 'hepp'})

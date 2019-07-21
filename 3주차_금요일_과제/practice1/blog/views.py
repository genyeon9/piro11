from django.http import Http404
from django.shortcuts import render, get_object_or_404
from . models import Post

# Create your views here.

def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '') #q가 있으면 가져오고 없으면 빈 문자열
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html',{
        'post_list':qs
    })

def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(Post, id=id)  #지정 Record가 없는 것은 서버오류(500)가 아니므로 404오류로 바꿔줘야 한다.

    return render(request, 'blog/post_detail.html', {
        'post':post,
    })

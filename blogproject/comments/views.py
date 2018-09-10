from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm


# Create your views here.
def post_comment(requset,post_pk):
    post = get_object_or_404(Post,pk=post_pk)

    if requset.method == 'POST':
        form = CommentForm(requset.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post':post,
                       'form':form,
                       'comment_list':comment_list
                       }
            return render(requset,'blog/detail.html',context=context)

    return redirect(post)
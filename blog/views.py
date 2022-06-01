from django.views import generic
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse,reverse_lazy

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    paginate_by = 7

class PostCreate(generic.CreateView):
    model = Post
    form_class = PostForm    
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id)
#     comments = post.comments.filter(active=True)
#     new_comment = None

#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             new_comment.user = request.user
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     context = {
#         'post': post,
#         'comments': comments,
#         'new_comment': new_comment,
#         'comment_form': comment_form,
#     }

#     return render(request, "blog/post_detail", context)

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    pk_url_kwarg="id" 

class PostComment(generic.DetailView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment.html'
    pk_url_kwarg="id"

class PostUpdate(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_update.html"
    success_url = reverse_lazy("post_list")
    pk_url_kwarg="id"
    

class PostDelete(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("post_list")
    pk_url_kwarg = "id" 

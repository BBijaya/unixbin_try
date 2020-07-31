from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.core.mail import send_mail
# importing models
from blog.models import Post, Email
# form
from blog.forms import NewsLetterForm
# importing paginator
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.





def test(request):
    return HttpResponse("<h1> UNIXBIN TRIAL PROJECT </h1>")


class BlogHomeView(ListView):
    """
    home view for blog
    """
    model = Post
    template_name = "blog/home.html"
    queryset = Post.published.all()
    paginate_by = 10
    
    # def get(self, request, *args, **kwargs):
    #     object_list = Post.published.all()
    #     top_five = Post.published.all().order_by('-views')[:5]
    #     also_like = Post.published.all().order_by('views')[:5]
    #     return render(request, self.template_name, {'object_list':object_list, 'top_five':top_five, 'also_like':also_like, })

    def post(self, request, *args, **kwargs):
        if 'search' in request.POST:
            search_term = request.POST.get('search', None)
            object_list = Post.published.filter(title__icontains=search_term)
            top_five = Post.published.all().order_by('-views')[:5]
            also_like = Post.published.all().order_by('views')[:5]
            return render(request, "blog/search_result.html", {'object_list':object_list, 'top_five':top_five, 'also_like':also_like, })
        else:
            return HttpResponse("<h1> UNIXBIN TRIAL PROJECT </h1>")
    def get_context_data(self, *args, **kwargs):
        """
        adding required data in context
        """
        top_five = Post.published.all().order_by('-views')[:5]
        also_like = Post.published.all().order_by('views')[:5]
        context = super(BlogHomeView, self).get_context_data(*args, **kwargs)
        context["top_five"] = top_five
        context["also_like"] = also_like
        return context


# https://github.com/jazzband/sorl-thumbnail
# mightneed to use this for thumbnailgeneration

class PostDetailView(DetailView):
    """
    Post detail view
    """
    model = Post
    template_name = "blog/post_detail.html"
    slug_url_kwarg = "the_slug"
    # you can also not define it here and directly use the slug as <slug> in url
    # now after defining "slug_url_kwargs", you must use as <slug:the_slug>

    def get_context_data(self, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs['the_slug'])
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        post.views = post.views + 1
        post.save()
        top_five = Post.published.all().order_by('-views')[:5]
        also_like = Post.published.all().order_by('views')[:5]
        # context = super(BlogHomeView, self).get_context_data(*args, **kwargs)
        context["top_five"] = top_five
        context["also_like"] = also_like
        return context

class TagListView(ListView):
    model = Post
    template_name = "blog/tag_related.html"
    paginate_by = 10
    # context_object_name = "posts"
    # by default it's object_list

    def get_queryset(self):
        return Post.objects.filter(status='published', tags__slug=self.kwargs.get('tag_slug'))


class DebianListView(ListView):
    """
    All post categorized debian
    """
    model = Post
    template_name = "blog/debian.html"
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(category='debian')

class UbuntuListView(ListView):
    """
    All post categorized ubuntu
    """
    model = Post
    template_name = "blog/ubuntu.html"
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(category='ubuntu')

class CentosListView(ListView):
    """
    All post categorized ubuntu
    """
    model = Post
    template_name = "blog/centos.html"
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(category='centos')

class RedhatListView(ListView):
    """
    All post categorized ubuntu
    """
    model = Post
    template_name = "blog/redhat.html"
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(category='redhat')

class ArchLinuxListView(ListView):
    """
    All post categorized ubuntu
    """
    model = Post
    template_name = "blog/archlinux.html"
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(category='archlinux')


def contact(request):

    if request.method == "POST":
        request.POST.get('is_private', False)
        msg_sender_name = request.POST.get('message_sender_name', default=False)
        msg_email = request.POST.get('message_email', default=False )
        msg_subject = request.POST.get('message_subject', default=False)
        msg_body = request.POST.get('message_body', default=False)

        # send email
        send_mail(
            msg_subject + msg_sender_name, #subject
            msg_body, #message
            msg_email, #from_email
            ['bijaya@example.com'], # to email

        )   

        return render(request, "blog/contact.html", {'message_sender_name':msg_sender_name })

    return render(request, "blog/contact.html", {})

class NewsLetterView(CreateView):
    model = Email
    form_class = NewsLetterForm
    template_name = "blog/newsletter.html"
    
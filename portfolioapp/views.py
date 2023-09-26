from django.shortcuts import render, redirect ,get_object_or_404
from django.http import FileResponse
from django.conf import settings
from .models import BlogEntry ,Comment
from django.contrib.auth.decorators import login_required
import os

def index(request):
    return render(request, 'index.html')

def projeler(request):
    return render(request, 'projeler.html')

def iletisim(request):
    return render(request, 'iletisim.html')

def hakkimda(request):
    return render(request, 'hakkimda.html')

def blog(request):
    if request.user.is_authenticated:
        blog_entries = BlogEntry.objects.all().order_by('-created_at')
        return render(request, 'blog.html', {'blog_entries': blog_entries})
    else:
        return render(request, 'blog.html')

def profile(request):
    return render(request, 'profile.html')

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)


# İngilizce Sayfalar
def indexEng(request):
    return render(request, 'en/indexEng.html')

def about(request):
    return render(request, 'en/about.html')

def contact(request):
    return render(request, 'en/contact.html')

def project(request):
    return render(request, 'en/project.html')

def blogEng(request):
    if request.user.is_authenticated:
        blog_entries = BlogEntry.objects.all().order_by('-created_at')
        return render(request, 'en/blogEng.html', {'blog_entries': blog_entries})
    else:
        return render(request, 'en/blogEng.html')

# Download CV
def download_cv(request):
    cv_file_path = os.path.join(settings.MEDIA_ROOT, 'Doğukan-CV-English.pdf')
    response = FileResponse(open(cv_file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="Doğukan-CV-English.pdf"'
    return response

# Blog gönderi paylaşma
def share_blog_post(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            BlogEntry.objects.create(author=request.user, content=message)
    return redirect('blog')  # veya başka bir sayfaya yönlendirme yapabilirsiniz


# Yorum düzenleme
def edit_blog_post(request, blog_post_id):
    blog_post = get_object_or_404(BlogEntry, id=blog_post_id)
    
    # Sadece yazarın kendi yorumunu düzenleme izni varsa
    if request.user == blog_post.author:
        if request.method == 'POST':
            new_content = request.POST.get('new_content', '')
            if new_content:
                blog_post.content = new_content
                blog_post.save()
                return redirect('blog')
        return render(request, 'edit_blog_post.html', {'blog_post': blog_post})
    else:
        # Yazar dışında kişiler düzenlemeye çalışırsa, istediğiniz işlemi yapabilirsiniz.
        return redirect('blog')  

# Yorum silme
def delete_blog_post(request, blog_post_id):
    if request.user.is_superuser:
        blog_post = get_object_or_404(BlogEntry, id=blog_post_id)
        blog_post.delete()
    return redirect('blog')

#Entry e Yorum Yapma
def add_comment(request, blog_post_id):
    blog_post = get_object_or_404(BlogEntry, id=blog_post_id)
    if request.method == 'POST':
        text = request.POST.get('comment', '')
        if text:
            Comment.objects.create(author=request.user, blog_entry=blog_post, text=text)
    
    return redirect('blog')
from django.http.response import HttpResponse
from django.shortcuts import render

data = {
    "blogs": [
        {
            "id": 1,
            "title": "tarih unutulmaz",
            "image": "1.jpg",
            "is_active": True,
            "is_home": True,
            "description": "tarih bir kitap"
        },
        {
            "id": 2,
            "title": "insanlar",
            "image": "2.jpg",
            "is_active": True,
            "is_home": True,
            "description": "kişisel gelişim"
        },
        {
            "id": 3,
            "title": "harry porter",
            "image": "3.jpg",       
            "is_active": True,
            "is_home": True,
            "description": "dünya klasikleri"
        }
    ]
}

# Create your views here.
def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, id):
    blogs = data["blogs"]
    selectedBlog = None

    for blog in blogs:
        if blog["id"] == id:
            selectedBlog = blog
            
    return render(request, "blog/blog_details.html",   {
        "blog": selectedBlog
    })

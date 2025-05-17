from django.shortcuts import render

def index(request):
    return render(request, "website/index.html")

def english_front(request):
    return render(request, "website/english_front.html")

def japanese_front(request):
    return render(request, "website/japanese_front.html")

def chinese_front(request):
    return render(request, "website/chinese_front.html")


def posts(request):
    pass

def post_detail(request):
    pass
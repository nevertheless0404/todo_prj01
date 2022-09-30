from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Review

# 화면 template
def index(request):
    review = Review.objects.all()
    context = {
        "review": review,
    }
    return render(request, "board/index.html", context)


def detail(request, pk_):
    Review.objects.get(id=pk_)
    review = Review.objects.all()
    context = {"review": review}

    return render(request, "board/detail.html", context)


def new(request):

    return render(request, "board/new.html")


def edit(request, pk_):
    review_ = Review.objects.get(id=pk_)
    context = {
        "review": review_,
    }
    return render(request, "board/edit.html", context)


def create(request):
    content = request.GET.get("content")
    title = request.GET.get("title")
    Review.objects.create(content=content, title=title)

    context = {
        "content": content,
        "title": title,
    }

    return redirect("board:index")


def delete(request, pk_):
    Review.objects.get(id=pk_).delete()

    return redirect("board:index")


def update(request, pk):
    review = Review.objects.get(id=pk)

    # 데이터를 받아오고
    title_ = request.GET.get("title")
    content_ = request.GET.get("content")

    # 데이터를 수정
    review.title = title_
    review.content = content_

    # 데이터를 수정한 것을 반영한다.
    review.save()

    return redirect("board:index")

from django.shortcuts import render

from .forms import ContactForms
from .models import *


# Create your views here.

def index(requests):
    recipe = Recipe.objects.all()
    ctg = Category.objects.all()

    ctx = {
        'recipe': recipe,
        'ctgs': ctg

    }
    return render(requests, "index.html", ctx)


def about(requests):
    ctgs = Category.objects.all()
    ctx = {
        'ctgs': ctgs
    }
    return render(requests, "about.html", ctx)


def blog(requests):
    ctgs = Category.objects.all()
    ctx = {
        'ctgs': ctgs
    }
    return render(requests, "blog-post.html", ctx)


class ContactForms:
    pass


def contact(requests):
    ctgs = Category.objects.all()
    contact = Contact()

    if requests.POST:
        form = ContactForms(requests.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

#        contact.name = requests.POST.get('name', '')
#        contact.email = requests.POST.get('email', '')
#        contact.subject = requests.POST.get('subject', '')
#        contact.message = requests.POST.get('message', '')
#        contact.save()


    ctx = {
        'ctgs': ctgs
    }
    return render(requests, "contact.html", ctx)


def element(requests):
    ctgs = Category.objects.all()
    ctx = {
        'ctgs': ctgs
    }
    return render(requests, "elements.html", ctx)


def recipe(requests, pk=None):
    root = Recipe.objects.get(pk=pk)
    ctgs = Category.objects.all()

    ctx = {
        'root': root,
        'ctgs': ctgs
    }

    return render(requests, "receipe-post.html", ctx)



def rec_ctg(requests, slug=None):
    ctgs = Category.objects.all()
    search = requests.GET.get("search", None)
    ctx = {}
    if slug:
        ctg = Category.objects.get(slug=slug)
        receipes = Recipe.objects.all().filter(ctg_id=ctg)
        ctx['ctg'] = ctg
        ctx['recipe'] = receipes

    if search:

        result = Recipe.objects.all()
        receipes = []
        for i in result:
            if search.lower() in i.name.lower() or search.lower() == i.name.lower() or search.lower() == i.name[0].lower():
                receipes.append(i)

        ctx['search'] = search
        ctx['recipe'] = recipe

        ctg = search

    ctx['ctgs'] = ctgs

    return render(requests, "receipe_ctg.html", ctx)

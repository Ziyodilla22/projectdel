from .forms import CategoryForm
from recipe.models import Category
from django.shortcuts import render, redirect


def list_detail_delete(requests, pk=None, delete=None):
    ctx = {}
    if pk:
        html = 'dashboard/category/detail.html'
        ctx['root'] = Category.objects.get(pk=pk)

    elif delete:
        Category.objects.get(pk=delete).delete()

        return redirect("dashboard_ctg_list")

    else:
        html = 'dashboard/category/list.html'
        ctx['roots'] = Category.objects.all()

    return render(requests, html, ctx)


def add_edit(requests, pk=None):
    if pk:
        root = Category.objects.get(pk=pk)
    else:
        root = None

    form = CategoryForm(instance=root)
    if requests.POST:
        forms = CategoryForm(requests.POST, requests.FILES, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect("dashboard_ctg_list")
        else:
            print("errorr", forms.errors)

    ctx = {
        "form": form
    }

    return render(requests, 'dashboard/category/forms.html', ctx)

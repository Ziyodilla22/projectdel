from .forms import RecipeForm
from recipe.models import Recipe
from django.shortcuts import render, redirect


def list_detail_delete(requests, pk=None, delete=None):
    ctx = {}
    if pk:
        html = 'dashboard/recipe/detail.html'
        ctx['root'] = Recipe.objects.get(pk=pk)

    elif delete:
        Recipe.objects.get(pk=delete).delete()

        return redirect("dashboard_rec_list")

    else:
        html = 'dashboard/recipe/list.html'
        ctx['roots'] = Recipe.objects.all()

    return render(requests, html, ctx)


def add_edit(requests, pk=None):
    if pk:
        root = Recipe.objects.get(pk=pk)
    else:
        root = None

    form = RecipeForm(instance=root)
    if requests.POST:
        forms = RecipeForm(requests.POST, requests.FILES, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect("dashboard_rec_list")
        else:
            print("errorr", forms.errors)

    ctx = {
        "form": form
    }

    return render(requests, 'dashboard/recipe/forms.html', ctx)

from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm  # User Authentication:
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Week, Choice  # Models


@login_required()
def index(request):
    latest_week_poll = Week.objects.get(pk=1)
    context = {
        "name": request.user,
        "week_poll": latest_week_poll
    }
    return render(request, "index.html",context)


class DetailsView(DetailView):
    model = Week
    template_name = "detail.html"


class ResultsView(DetailView):
    model = Week
    template_name = "results.html"


@login_required()
def vote(request, week_id):
    try:
        week = Week.objects.get(pk=1)
        selected_choice = week.choice_set.get(pk=request.POST["choice"])
    except Week.DoesNotExist:
        raise Http404("Poll for said week does not exists")
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect("results", week_id)

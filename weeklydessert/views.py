from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm  # User Authentication:
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .models import Week, Choice  # Models


@login_required()
def index(request):
    try:
        latest_week_poll = Week.objects.get(pk=1)
        context = {
            "name": request.user,
            "week_poll": latest_week_poll
        }
    except Week.DoesNotExist:
        context = {
            "name": request.user,
        }
    return render(request, "index.html", context)


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


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# def signin(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#
#     user = authenticate(request, username=username, password=password)
#
#     if user is not None:
#         login(request, user)

# Create your views here.
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
# from django.contrib.auth.models import User

from travels.models import TravelPlan

class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class TravelPlanOwnerMixin(object):
    def get_object(self, queryset=None):
        if queryset is None:
            queryset=self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied
        return obj

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



class ListTravelPlan(LoggedInMixin, TravelPlanOwnerMixin, ListView):
    model = TravelPlan
    template_name ='travelplan_list.html'

    def get_queryset(self):
        return TravelPlan.objects.filter(owner=self.request.user)


class CreateTravelPlan(LoggedInMixin, TravelPlanOwnerMixin, CreateView):
    model = TravelPlan
    template_name = 'edit_travelplan.html'

    def get_success_url(self):
        return reverse('travelplan-list')

class TravelPlanView(LoggedInMixin, TravelPlanOwnerMixin, DetailView):
    model = TravelPlan
    template_name = 'travelplan.html'

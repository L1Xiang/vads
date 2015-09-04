from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.views.generic.edit import FormView, CreateView
from vads.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from braces import views
from . import models
from . import forms
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from django.db.models import Count

# The home page of our web
def index(request):
    return render_to_response('vads/index.html', 
                              RequestContext(request))
    
class RestrictToUserMixin(views.LoginRequiredMixin):
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
class UserProfileUpdateView(views.LoginRequiredMixin,
                            views.SetHeadlineMixin,
                            generic.UpdateView):
    form_class = UserProfileForm
    headline= 'Update'
    model = models.UserProfile
    
    
class UserProfieDetailView(
                           views.SetHeadlineMixin,
                           generic.DetailView,
                           ):
    form_class = UserProfileForm
    headline = 'Detail'
    model = models.UserProfile

class ScreenListView(
                     views.LoginRequiredMixin,
                     generic.ListView):
    model = models.Screen
    
    def get_queryset(self):
        return self.request.user.screens.all()

class ScreenDetailView(
            RestrictToUserMixin,
            generic.DetailView):
    model = models.Screen
    
class ScreenCreateView(views.LoginRequiredMixin,
                       views.SetHeadlineMixin,
                       generic.CreateView):
    form_class = forms.ScreenForm
    headline = 'Create'
    model = models.Screen
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ScreenCreateView, self).form_valid(form)
    
class ScreenUpdateView(
                       RestrictToUserMixin,
                       views.SetHeadlineMixin,
                       generic.UpdateView):       
    form_class = forms.ScreenForm
    headline = 'Update'
    model = models.Screen
    
    
class ScreenDeleteView(
                       RestrictToUserMixin,
                       views.LoginRequiredMixin,
                       views.SetHeadlineMixin,
                       generic.DeleteView):       
    form_class = forms.ScreenForm
    headline = 'Delete'
    model = models.Screen
    
    
# View class about uploaded ads
class AdCreateView(
                   LoginRequiredMixin,
                   views.SetHeadlineMixin,
                   generic.CreateView):
    model = models.Ad
    headline = 'Create'
    form_class = forms.AdForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(AdCreateView, self).form_valid(form)
    
class AdDetailView(
                   RestrictToUserMixin,
                   views.SetHeadlineMixin,
                   generic.DetailView):
    headline = 'Detail'
    model = models.Ad
    
class AdListListView(RestrictToUserMixin,
                     generic.ListView
                    ):
    model = models.AdList
    
    def get_queryset(self):
        queryset = super(AdListListView, self).get_queryset()
        queryset.annotate(ad_count=Count('ads'))
        print(Count("ads"))
        return queryset

class AdListDetailView(
                       views.LoginRequiredMixin,
                       generic.DetailView):
    model = models.AdList
    form_class = forms.AdForm
    http_method_names = ['post', 'get']
    
    def get_context_data(self, **kwargs):
        context = super(AdListDetailView, self).get_context_data(**kwargs)
        context.update({'form': self.form_class(self.request.POST or None)})
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = self.get_object()
            ad = form.save(commit=False)
            ad.ad_list = obj
            ad.user = request.user
            ad.save()
        else:
            return self.get(request, *args, **kwargs)
        return redirect(obj) 

class AdListCreateView(views.LoginRequiredMixin,
                       views.SetHeadlineMixin,
                       generic.CreateView):
    form_class = forms.AdListForm
    headline = 'Create'
    model = models.AdList
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(AdListCreateView, self).form_valid(form)
    
class AdListUpdateView(views.LoginRequiredMixin,
                       views.SetHeadlineMixin,
                       generic.UpdateView):
    form_class = forms.AdListForm
    headline = 'Update'
    model = models.AdList
        
    
    
    
    

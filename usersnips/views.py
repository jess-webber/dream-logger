from django.shortcuts import render
from django.http import HttpResponse
from .forms import SnippetForm
from .models import Snippet
from django.contrib import messages

def allsnips(request):
    snipps = Snippet.objects.filter(user=request.user)
    return render(request, 'allsnips.html', {'snipps' : snipps})

def snippet_detail(request):
    form = SnippetForm(request.POST or None, request.FILES or None)
    if request.method =='POST':

        if form.is_valid():

            obj = form.save(commit = False)
            obj.user = request.user;
            obj.save()
            form = SnippetForm()
            messages.success(request, "Dream saved!")


    return render(request, 'form.html', {'form':form})

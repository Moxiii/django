from django.shortcuts import render , redirect
from sql.inject import * 
from django.conf import settings 
from django.http import HttpResponse    
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {"title":"acceuil"}
    return render(request ,'scrappator/index.html',context=context)
@login_required
def about(request):
    context={"title":"about"}
    return render(request ,'scrappator/about.html',context=context )
@login_required
def scrappator(request):
    return render(request ,'scrappator/app.html',context={"title":"scrappator"})




    



from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response

#imports para Roles y Permisos
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/login/")

def login(request):
    #return render(request, 'pages/login.html', {})
    return HttpResponseRedirect("/login/")

from django.shortcuts import redirect

@login_required
def login_success(request):
    # Redirects users based on whether they are in the admins group
    if request.user.groups.filter(name="user").exists():
        print (request.user.username)
        # user is an admin
        return redirect("/dashboard/home")
    else:
        context = {
            #'all_ventas': all_ventas,
        } 
        #return render(request, 'pages/home.html', context)
        return redirect("/login/", context)

# Create your views here.

def home(request):
     
     context = {}
     
     context = get_context_data(request)
     
     return render(request, 'pages/index.html', context)

#User signup - Registro
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'pages/signup.html', {'form': form})


#--------------------*--------------------*------------------------#

from googleads import adwords
from dashboard import get_campaigns
from django.template.loader import get_template
from ReportingApp.utils import render_to_pdf
from dashboard.forms import GetReportingForm 


def get_context_data(request):

    context ={}
    try:
        simpleList = []
        simpleList = get_campaigns.getCampaigns()
        context ={'all_cajas' : simpleList}
    except Exception as e:
        print (e)
     
    return context    
    #return render(request, 'pages/index.html', context)

def campaignsToPDF(request, *args, **kwargs):
    
    class SimpleClass(object):
        pass
    
    campanias  = []
    campanias = get_campaigns.getCampaigns()
    context = {
        'campanias': campanias,
    } 

    template = get_template ('pdf/campaigns.html')
    html = template.render(context)
    pdf = render_to_pdf('pdf/campaigns.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "InformeX_cierre%s.pdf" #%(cierre_id)
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        response['content-Disposition'] = content
        return response
    else:
        return HttpResponse("Not Found")  

def getReporting(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GetReportingForm(request.POST)
        print(form)
        
        errors = []
        error = False
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            observaciones = form.cleaned_data['observaciones']
            
            # Initialize the AdWords client.
            adwords_client = adwords.AdWordsClient.LoadFromStorage()
            
            
            return render(request, 'reporting/index.html', {'errors': errors})
        else:
            errors.append("No existe un dia de trabajo creado.")
            return render(request, 'reporting/index.html', {'errors': errors})


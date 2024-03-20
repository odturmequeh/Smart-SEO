from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from add_URL.models import Url, Url_new
from add_URL.form import Urlform
from urllib.request import Request, urlopen
from urllib import error
from django.contrib import messages
from django.urls import reverse_lazy

def envio_info(info, parmeter_form_str):
    info_search=info.lower()
    info_send=url_new(n=info_search)
    info_send.save()

def base(request):

    return render(request,"add_URL/base.html")

def home(request):
    input_url=Urlform()
    url_valida=False
    
    if request.method == "POST":
        
        url_info= request.POST["url_input"]
        url_info=url_info.lower()
        if (str(url_info[0:8]) == "https://" or str(url_info[0:7]) == "http://"):
            try:
                urlopen(url_info)
                url_valida=True   
            except error.HTTPError:
                url_valida=False
                messages.error(request, "Url, no encontrada o invalida. Verifícala")
                return redirect("/")
            except:        
                url_valida=False
                messages.error(request, "Url, no encontrada o invalida. Veirifícala")
                return redirect("/")
            if url_valida:
                url_input_now=Url.objects.filter(url__icontains=url_info)
                if url_input_now:
                    return redirect ("/compra")
                else:    
                    url_input=Url(url=url_info)
                    url_input.save()
                    return redirect("/url_new")
        else:
            messages.error(request, 'Debe incluir http o https')
            return redirect("/") 
    
    return render(request,"add_URL/home.html")

def url_new(request):
    if request.method == "POST":
        input_search= request.POST["input_search"]
        input_search=input_search.lower()
        input_company=request.POST["input_company"]
        input_company=input_company.lower()
        input_email=request.POST["input_email"]
        input_email=input_email.lower()
        info_send=Url_new(terminos_busqueda=input_search, industria=input_company, email=input_email)
        info_send.save()

        return redirect("/compra")
    
    return render(request, "add_URL/url_new.html")

def blog(request):

    return render(request,"add_URL/blog.html")

def contacto(request):

    return HttpResponse("contacto")

def compra(request):

    return HttpResponse("compra")


# Create your views here.

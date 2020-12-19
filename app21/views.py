from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.

def covid(request):
    return render(request,'covid.html')
def showdata(request):


    data=requests.get("https://api.rootnet.in/covid19-in/hospitals/beds")

    result=data.text

    json_data=json.loads(result)

    if json_data["success"]:


        return render(request, 'showdata.html',{"information":json_data})

    else:

        return render(request,'showdata.html',{'error':'Sorry We cannot process your Data'})



def medicalcollage(request):


    data=requests.get("https://api.rootnet.in/covid19-in/hospitals/medical-colleges")

    result=data.text

    json_data=json.loads(result)

    if json_data["success"]:


        return render(request, 'medical.html',{"information":json_data})

    else:

        return render(request,'medical.html',{'error':'Sorry We cannot process your Data'})


def contact(request):


    data=requests.get("https://api.rootnet.in/covid19-in/contacts")

    result=data.text

    json_data=json.loads(result)

    if json_data["success"]:


        return render(request, 'contact.html',{"information":json_data})

    else:

        return render(request,'contact.html',{'error':'Sorry We cannot process your Data'})




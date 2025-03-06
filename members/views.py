from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

def member(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('member.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))
def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('member_detail.html')
    context = {
        'mymembers': mymember,
    }
    return HttpResponse(template.render(context,request))
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
def test(request):
    template = loader.get_template("test.html")
    context = {
        'fruits':['apple','banana','manga','chenwa'],
    }
    return HttpResponse(template.render(context,request))

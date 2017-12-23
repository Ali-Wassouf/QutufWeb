# Create your views here.
from django.http import HttpResponse
import xmltodict, json

from django.shortcuts import render
from .Solution.ALP.Views.run_Qutuf import runit


def index(request):
    """The home page for learning log"""
    phrase = request.GET.get('phrase', '')
    type = request.GET.get('type', '')

    if phrase and type:
        outputDict = runit(phrase)
        if type == 'xml':

            #file = open('D:\\Python projects\\QutufWeb\\QutufWebTest\\mainTest\\Output\\test.xml', encoding="utf8").read()
            return HttpResponse(outputDict['xml'], content_type='text/xml')
        elif type == 'html':

            # file = open('D:\\Python projects\\QutufWeb\\QutufWebTest\\mainTest\\Output\\test.xml', encoding="utf8").read()
            return HttpResponse(outputDict['HTML'], content_type='text/html')
        elif type == 'json':
            o = xmltodict.parse(outputDict['xml'])
            return HttpResponse(json.dumps(o), content_type='application/json')

    else:
        return render(request, 'mainTest/index.html')


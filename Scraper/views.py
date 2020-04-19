from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs

def ExtractCounts(url):
     WorldOMeterHtml = requests.get(url)
     WorldOMeterSouped = bs(WorldOMeterHtml.content,"html5lib")
     maincounter_numbers = WorldOMeterSouped.findAll("div",attrs={'class':'maincounter-number'})
     result = {}
     result['totalCases'] = maincounter_numbers[0].find("span").text
     result['deaths'] = maincounter_numbers[1].find("span").text
     result['recovered'] = maincounter_numbers[2].find("span").text
     result['activeCases'] =format(int(result['totalCases'].replace(',',''))-int(result['deaths'].replace(',',''))-int(result['recovered'].replace(',','')),",")
     return result


# Create your views here.
def main(request):
    worldresult=ExtractCounts("https://www.worldometers.info/coronavirus/")
    indiaResult=ExtractCounts("https://www.worldometers.info/coronavirus/country/india/")
    return render(request,"resultSite/index.html",{"worldresult":worldresult,"indiaResult":indiaResult})


from django.shortcuts import render,HttpResponse

def home(request):
    return render(request, 'userapp/base.html')


def name(request):
    return render(request, 'userapp/name.html')



def app1(request):
    return HttpResponse('<h1 style="background-color:Tomato;">Tomato</h1><h1 style="background-color:Orange;">Orange</h1><h1 style="background-color:DodgerBlue;">DodgerBlue</h1><h1 style="background-color:MediumSeaGreen;">MediumSeaGreen</h1><h1 style="background-color:Gray;">Gray</h1><h1 style="background-color:SlateBlue;">SlateBlue</h1><h1 style="background-color:Violet;">Violet</h1><h1 style="background-color:LightGray;">LightGray</h1>')

def app2(request):
    return HttpResponse('<h2>Radio Buttons</h2><p>Choose your favorite Web language:</p><form><inputtype="radio"name="fav_language" value="HTML"> <label for="html">HTML</label><br>\<input type="radio" id="css" name="fav_languagvalue="CSS"> <label for="css">CSS</label><br> \<input type="radio" id="javascript" name="fav_language" value="JavaScript"><label for="javascript">Ja')





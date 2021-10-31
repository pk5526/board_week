from django.shortcuts import render
from googletrans import Translator

def index(request):
    context={}
    if request.method=="POST":
        text1=request.POST.get("pretext")
        f=request.POST.get("from")
        t=request.POST.get("to")
        translator=Translator()
        trans1=translator.translate(text1,src=f,dest=t)
        context.update({
            "text":trans1.text,
            "pretext":text1,
            "from":f,
            "to":t
        })



    return render(request,"trans/index.html",context)
                       



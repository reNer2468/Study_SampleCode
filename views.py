from django.shortcuts import render
from django.db.models import Q
from analize_data.models import Analize_Data
from .graph import Plot_Hist

# Create your views here.
def index(request):
    Total_Data=Analize_Data.objects.all()
    Searched_Data1=[data.ViewCount for data in Total_Data]
    Searched_Data2=[data.ChatRate for data in Total_Data]
    
    context={"Analize_ViewCount":Plot_Hist(Searched_Data1,"blue","viewcount","viewcount"),"Analize_ChatRate":Plot_Hist(Searched_Data2,"red","chatrate","chatrate")}
    return render(request,"analize_data/analysis.html",context)

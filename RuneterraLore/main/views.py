from django.shortcuts import render,get_object_or_404, redirect
from .models import Region,Champion
# Create your views here.


def home_page(request):
	regions = list(Region.objects.all().order_by('name'))
	start_regions = regions[0:3]
	collapse_regions = regions[3:]

	champions = list(Champion.objects.all().order_by('name'))
	start_champions = champions[0:4]
	collapse_champions = champions[4:]
	tosend = {
		'start_champ':start_champions,
		'collapse_champ': collapse_champions,
		'start_reg':start_regions,
		'collapse_reg': collapse_regions
	}
	print(collapse_regions)
	return render(request,'index.html',tosend)


def region_page(request,name):
	region = get_object_or_404(Region, name = name)
	champions = Champion.objects.filter(region = region)
	print(champions)
	return render(request, 'region.html',{'region':region,'champions':champions})


def champion_page(request,name):
	champion = get_object_or_404(Champion, name=name)
	region = champion.region.get()
	champions = Champion.objects.filter(region= region)
	
	return render(request, 'champion.html',{'champion': champion, 'region': region, 'champions':champions})

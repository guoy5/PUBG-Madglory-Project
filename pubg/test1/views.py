from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from test1.player_performance import player_stats

# Create your views here.

def home(Request):
	# Go to Homepage
	return render(Request, 'homepage.html')

def search(Request):
	# If users enter correct player names, go to the stats page
	# Otherwise, show the error page or return to the homepage
	if Request.GET.get('playername'):
		playername = Request.GET.get('playername')
		result = player_stats(playername)
		if result:
			return render(Request, 'statistical_page1.html', result)
		else:
			return render(Request, 'error_page.html')
	else:
		return render(Request, 'homepage.html')

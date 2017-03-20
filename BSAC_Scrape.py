from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import sys
# Above, we are importing all the libraries (pre-written Python functions that we'll be using)
 
def scrapeHomefield(csv_file, startyr, endyr):
	""" Input: Name of CSV file we want to write to, start year, and end year"""
	""" Action: Scrapes our desired homefield advantage data between startyr and endyr, inclusive"""

	# Desired url is of form: "http://www.pro-football-reference.com/years/[year]/games.htm"
	# Where [year] is the year (i.e. 2016, 2015, 2014, etc.)
	pre_url = "http://www.pro-football-reference.com/years/"
	post_url = "/games.htm"

	# We open the csv file to write to it
	with open(csv_file, "w", newline="") as myfile:
		wr = csv.writer(myfile)
		wr.writerow(['Home Team', 'Away Team', 'Home Score', 'Away Score', 'Home Win?'])
		# We cycle through pro-football-reference from startyr to endyr, inclusive
		# for i in range(a, b) cycles through a, a+1, ..., b-2, b-1
		for i in range(startyr, endyr+1):
			
			# We make the URL by combining three separate parts
			season_url = pre_url +str(i)+post_url
			# scrapeYear is the function below
			scrapeYear(season_url, wr)

def scrapeYear(year_url, wr):
	""" year_url is the url we will be scraping from"""
	""" wr is the CSV file we will be writing to """
	""" For a given NFL year, scrapes the Home Team, Away Team, Home Score, Away Score, and 
	whether the Home Team won for every team """

	# We open our URL into an HTML object (roughly speaking)
	html = urlopen(year_url)
	# We make a soup object for us to do our parsing
	soup = BeautifulSoup(html, "lxml")

	# boxscores is a list of a tags of form:
	# <a href="/boxscores/198009070min.html">boxscore</a>

	#To-Do #1: [Find a list of all the boxscore links]

	# To-Do #2: Loop through all the box-scores, finding the desired information for each

	for bs in boxscores:

		# Find the following:
		# loser
		# homewin
		# winner
		# ptsWin
		# ptsLoss

		# To-Do #3: Logic - we have the winning and losing teams, but we want the 
		# home team and away team and home score and away score
		# We also want a variable 'win' which is 1 if the home team won and 0 if they lost

		if homewin.text == "@":
			# fill in:
			# hometeam = 
			# awayteam = 
			# homescore = 
			# awayscore =
			# win = 
		else:
			# fill in:
			# hometeam = 
			# awayteam = 
			# homescore = 
			# awayscore =
			# win =

		# We put the items we want to return in a list
		toReturn = [hometeam, awayteam, homescore, awayscore, win]
		# We write those objects to our CSV file
		wr.writerow(toReturn)
	
	# Always decompose the soup (if you make it, remember to decompose / discard it as a general rule)
	soup.decompose()

file = "C:\\Users\\Steven\\Desktop\\NFL_Homefield.csv"
scrapeHomefield(file, 2016, 2016)
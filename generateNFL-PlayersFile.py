import os
import urllib
import sys
from bs4 import BeautifulSoup
import json

baseUrl = 'https://sports.yahoo.com/nfl/players?type=lastname&query={0}'
ABBREVIATIONS_FILE_NAME = 'nfl-team_abbreviations.txt'

def getAbbreviationsOfTeamsDictFromFile(fileName):
	abbreviationMap = {}
	with open(fileName) as file:
		for line in file.readlines():
			line = line.strip('\n')
			components = line.split('\t')
			abbreviationMap[components[0]] = components[1]
	return abbreviationMap

def obtainPlayerDictsForStartingLetter(letter):
	playersForLetter = []
	html = urllib.urlopen(baseUrl.format(letter)).read()
	b = BeautifulSoup(html, 'html.parser')
	playerTbl = b.findAll('tr', attrs={'class': 'ysprow1'})
	playerTbl.extend(b.findAll('tr', attrs={'class': 'ysprow2'}))
	for player in playerTbl:
		playerSpecificData = player.findAll('td')
		try:
			name = playerSpecificData[0].a.text
			position = playerSpecificData[1].text
			team = playerSpecificData[2].a.text
			player = {'player': name, 'pos': position, 'team': team}
			playersForLetter.append(player)
		except:
			sys.stderr.write(str(playerSpecificData) + ' for letter ' + letter + '\n')
	return playersForLetter

def main():
	allPlayers = []
	alphabet = [chr(ord('A') + i) for i in range(0, 26)]

	abbreviationMap = getAbbreviationsOfTeamsDictFromFile(ABBREVIATIONS_FILE_NAME)

	for letter in alphabet:
		allPlayers.extend(obtainPlayerDictsForStartingLetter(letter))

	for player in allPlayers:
		player['team'] = abbreviationMap[player['team']]
	# sys.stdout.write('callback({"list": ' + str(allPlayers) + '});')
	sys.stdout.write(json.dumps(allPlayers))

if __name__ == '__main__':
	main()
#print("Hello")
from match import main
#print("HelloAgain")

blueName = "BlueTryout"
redName = "RedTryout"
blueTeam = {}
redTeam = {}
blueDraft = [0,1,2,3,4]
redDraft = [5,6,7,8,9]
gameId = ""
f = open("input.txt", "r")
fileData = []
for line in f:
	fileData.append(line.replace("\n",""))
blueTeam["TOP"] = fileData[2]
blueTeam["JNG"] = fileData[3]
blueTeam["MID"] = fileData[4]
blueTeam["ADC"] = fileData[5]
blueTeam["SUP"] = fileData[6]
redTeam["TOP"] = fileData[7]
redTeam["JNG"] = fileData[8]
redTeam["MID"] = fileData[9]
redTeam["ADC"] = fileData[10]
redTeam["SUP"] = fileData[11]
gameId = fileData[22]

main(1, 2, blueTeam, redTeam, blueDraft, redDraft, gameId)

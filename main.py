def scoutcheck(PlayerName):
	global namecheck
	global actualname
	PlayerName = PlayerName.upper()
	PlayerNameLength = len(PlayerName)
	importercheckfile = open('import.txt', 'r')
	importercheckline = importercheckfile.readline()

	while (importercheckline):
		importercheck = importercheckline[:PlayerNameLength]
		if (importercheck == PlayerName):
			namecheck = True
			actualname = importercheckline[:importercheckline.find(":")]
		importercheckline = importercheckfile.readline()
		
	return namecheck
	return actualname

def rearrangemaxvalue():
	global importlist
	global usagelist

	xreplacelist = []
	yreplacelist = []

	for z in range(len(usagelist)):
		ilist = max(usagelist)
		index = usagelist.index(ilist)
		xreplace = importlist[index]
		yreplace = usagelist[index]
		xreplacelist.append(xreplace)
		yreplacelist.append(yreplace)
		importlist.remove(xreplace)
		usagelist.remove(yreplace)
	
	importlist = xreplacelist
	usagelist = yreplacelist

	return usagelist
	return importlist 

usernamelist = []
namecheck = False
actualname = ""

usernameamount = input("Enter the amount of players you want to scout: ")
ucheck = 0

while (ucheck != 1):
	if (((usernameamount).isdigit()) == True):
		usernameamount = int(usernameamount)
		ucheck = 1
	else:
		usernameamount = input("\nYour previous response was not a number. Input a number: ")

if (ucheck == 1):
	for i in range (usernameamount):
		username = input("\nEnter the username of one of the players you want to scout: ")
		while(namecheck == False):
			scoutcheck(username)
			if (namecheck == True):
				usernamelist.append(actualname)
			else:
				username = input("\nThe username you imputted prior was not in the import. Try another: ")
		namecheck = False

importlist = []

importfile = open("import.txt", "r")
importline = importfile.readline()
while importline:
	if ((((importline[:(len(importline)-2)]) in usernamelist)) == True):
		for counter1 in range(3):
			importline = importfile.readline()
			importlinelength = importline.find(":")
			modLine = importline[:importlinelength]
			importlist.append(modLine)
		importline = importfile.readline()
	importline = importfile.readline()
importfile.close()

teamlist = importlist

print(teamlist) 

teamvarlist = []
teamtrio = 0
for varcounter in range (int(len(teamlist)/3)):
 teamvarlist.append(teamlist[teamtrio] + " \ " +  teamlist[teamtrio + 1] + " \ " + teamlist[teamtrio + 2] )
 teamtrio = teamtrio + 3

print(teamvarlist)

importlist.sort()

importlen = len(importlist)

usagelist = []
moncounter = 1

counter3 = 0

for counter2 in range (importlen):
	if (counter3 == (len(importlist)-1)):
		break
	
	c1 = importlist[counter3]
	c2 = importlist[counter3+1]

	if (c1 == c2):
		importlist.remove(c1)
		moncounter = moncounter + 1 
		
	else:
		counter3 = counter3 + 1
		usagelist.append(moncounter)
		moncounter = 1

rearrangemaxvalue()


usagefile = open('usage.txt', 'w')
for counter5 in range (len(importlist)):
  if (counter5 < len(teamvarlist)):
    usagefile.write(teamvarlist [counter5] + "\t" + importlist[counter5] +  "\t" + str(usagelist[counter5]) + "\n")
  else:
    usagefile.write(" \t" + importlist[counter5] +  "\t" + str(usagelist[counter5]) + "\n")
usagefile.close()
#!/usr/local/python-2.7/bin/python2
from datetime import datetime
import time

def nowDate():
	now = datetime.now()
	return "<p><strong>Today: </strong>%s/%s/%s" %(now.month, now.day, now.year) + "</p>"

def mmDdYyyyDate(inDate):
	date = time.strptime(inDate,'%m %d %Y')
	formattedDate = time.strftime ("%B %d, %Y", date)
	return "<p><strong>Birthday: </strong>" + formattedDate + "</p>"

	
def stringInputResults(inString):
	charNum = len(inString)
	trimmed = len(inString.strip())
	uppercase = inString.upper()
	lowercase = inString.lower()
	dmaccFound = findDmacc(lowercase)
	return "<h2>" + inString + "</h2>"\
			+ "<p><strong>Untrimmed Character Count:</strong> %s" %(charNum) + "</p>"\
			+ "<p><strong>Trimmed Character Count:</strong> %s" %(trimmed) + "</p>"\
			+ "<p><strong>Lowercase String:</strong> " + lowercase + "</p>" \
			+ "<p><strong>Uppercase String:</strong>" + uppercase + "</p>"

			
def findDmacc(lowercaseStringToSearch):
	foundSubstring = lowercaseStringToSearch.find("dmacc")
	if foundSubstring:
		return "DMACC is found in the string"
	else:
		return "DMACC is not found in the string" 

def formatNumber(inNum):
	formattedNum = "{:,}".format(inNum)
	formattedMoney = "{:,.2f}".format(inNum)
	
	digitSum = 0
	numToSum = str(inNum)
	for digit in numToSum:
		digit = int(digit)
		digitSum = digitSum + digit
		
	return "<p><strong>Formatted Number: </strong> %s" %(formattedNum) + "</p>"\
			+ "<p><strong>Formatted Money: </strong> $ %s" %(formattedMoney) + "</p>"\
			+"<p><strong>Digit Sum of Number: </strong> %s" %(digitSum) + "</p>"





		
print "Content-Type: text/html"
print 

print """
<!DOCTYPE html>
<html>
<head>
<title>Python Practice</title>

<style>
body {
	background-image: url("coolColor.png");
}

.container{
	background-color: white;
	width: 50%;
	margin: auto;
	margin-top: 5%;
}

#dates{
	width: 99%;
	margin: auto;
	margin-bottom: 25px;
	text-align: center;
	border: 10px solid #804000;
	background-color: rgba(128, 64, 0, 0.4);
}	

#string{
	width: 99%;
	margin: auto;
	margin-bottom: 25px;
	text-align: center;
	border: 10px solid #cc6600;
	background-color: rgba(204, 102, 0, 0.4);
}

#number{
	width: 99%;
	margin: auto;
	text-align: center;
	border: 10px solid #e6b800;
	background-color: rgba(230, 184, 0, 0.4);
	
}
</style>
</head>
<body>
	<div class="container">
	<div id="dates">
		<h2>Dates</h2>
"""

print nowDate()

print mmDdYyyyDate("03 24 1990")

print """
	</div>
	</div>
	
	<div class="container">
	<div id="string">
"""

print stringInputResults("            Hello DMACC, I'm Joe!")

print """
	</div>
	</div>
	
	<div class="container">
	<div id="number">
		<h2>1234567890</h2>
"""

print formatNumber(1234567890)

print"""
	</div>
	</div>
</body>
</html>
"""



#---------------------------------------------------------------------
# --FUNCTION 1--
# Crawl the given website, depth limit given (DUMMY)
def crawl(sURL, depth):
	print("Crawl: " + sURL + ", depth: " + str(depth));
	if depth == 0:
		return;
	else:
		sHTML = getPage(sURL);
		savePage(sHTML, sURL);
		arrLinks = getLinks(sHTML);
		for link in arrLinks:
			crawl(link, depth - 1);
			
#---------------------------------------------------------------------
# --FUNCTION 2--
# Retrieve the web page
# Retruen its HTML as one string
def getPage(sURL):
	import requests;
	try:
		response = requests.get(sURL);
		return response.content;
	except:
		print("Something is wrong. Skip.");
		return "ERROR";

#---------------------------------------------------------------------
# --FUNCTION 3--
# Save the page content to a file
# The file name will be generated based on the url 
def savePage(sContent, sURL):
	fname = getFileName(sURL);
	f1 = open(fname, "w");
	s2 = str(sContent);
	f1.write(s2);
	f1.close();
	# print("save page: " + sURL);

#---------------------------------------------------------------------
# --FUNCTION 4--
# Remove all the special charactors from sURL
def getFileName(sURL):
	sRes = "";
	for x in sURL:
		if (x>='a' and x<='z') or (x>='A' and x<='Z'):
			sRes += x;
		else:
			sRes += "_";
	return "data/" + sRes;
	
#---------------------------------------------------------------------
# --FUNCTION 5--	
# Return an array of strings 
# Each element is a link in the given content
def getLinks(sContent):
	import re;
	r1 = re.compile("http://[a-zA-Z0-9_\.]+");
	s2 = str(sContent);
	arr = r1.findall(s2);
	return arr;

#---------------------------------------------------------------------
# === MAIN PROGRAM === (implement the functions)
# savePage("Easy Job!", "http://hofstra.edu");
# print( getFileName("http://hofstra.edu") );
# print( getLinks("<html> http://abc.com http://nbc.com </html>") );
# print( getPage("http://www.hofstra.edu") );
crawl("http://www.hofstra.edu", 3);

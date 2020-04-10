from bs4 import BeautifulSoup as Soup
import pandas as pd
import time
import glob

time = time.strftime("%Y%m%d-%H%M%S")


filenames = glob.glob("/home/jeet/Documents/kml/files/*.kml")

arr = []
n=0

for file in filenames : 

	with open(file) as data:
	    kml_soup = Soup(data, 'lxml-xml')

	for a in kml_soup.find('name'):
		name = a.string
		print(name)

	for a in kml_soup.find_all('coordinates'):
		if len(a.string)>50 :
			line =  a.string.strip()
			line = line.replace(",0","")
			line = line.replace("                ","")
			s="; "
			coord = s.join(line.splitlines())
			

	hosp = [name,coord]
	arr.append(hosp)
	n=n+1

finallist = pd.DataFrame(arr, columns=list('xy'))
finallist.to_excel("output"+time+".xlsx")
print(f"Done for {n} hospitals!")

import sys
import os
import requests
import pafy
from bs4 import BeautifulSoup
def download(url):
	r=requests.get(url)
	if r.status_code !=200:
		return 
	url=url.split('//')
	if url[0]=='http://' or url[0]=='https://':
		prefix=url[0]
	else:
		prefix='https://'
	url=url[-1].split('/')[0]
	url=prefix+url
	playlist=BeautifulSoup(r.text,"html.parser").findAll("td",{"class" : "pl-video-title"})
	dir=os.path.dirname(os.path.abspath(__file__))
	folder=BeautifulSoup(r.text,"html.parser").find("div",{"class":"pl-header-content "})
	folder=folder.h1.contents[0].split('|')[0]
	if os.path.exists(folder):
   		shutil.rmtree(folder)
	os.makedirs(folder)
	list=[]
	for link in playlist:
		link=link.a.attrs['href']
		if link[:7]=='http://' or link[:8]=='https://':
			list.append(link)
		if link[:1]!='/':
			link=('/'+link)
		list.append(url+link)
	print(list)
	for link in list:
		video=pafy.new(link)
		print(video)
		stream=video.streams
		best=video.getbest(preftype="mp4")
		filename = best.download(filepath=dir+'/'+folder+'/'+video.title+'.'+best.extension,quiet=False)

print(__file__) #contains full path
print(__name__) # __name__ == file name while importing
if __name__=='__main__' :
	if len(sys.argv)<2:
		print('Usage : python_latest_version filepath Website_Url')
	else:
		download(sys.argv[1])

# Use python2 to use pafy module :)
import sys
import os
import requests
import pafy
def dmusic(url):
	video=pafy.new(url)
	print(video)
	stream=video.audiostreams
	name=video.title.split('|')[0]
	bestaudio=video.getbestaudio()
	dir=os.path.dirname(os.path.abspath(__file__))
	filename = bestaudio.download(filepath=dir+'/'+video.title+'.'+bestaudio.extension,quiet=False)
print(__file__) #contains full path
print(__name__) # __name__ == file name while importing
if __name__=='__main__' :
	if len(sys.argv)<2:
		print('Usage : python_latest_version filepath Website_Url')
	else:
		dmusic(sys.argv[1])

# Use python2 to use pafy module :)
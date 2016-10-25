import sys
import os
import requests
import pafy
def download(url):
	video=pafy.new(url)
	print(video)
	stream=video.streams
	best=video.getbest(preftype="mp4")
	dir=os.path.dirname(os.path.abspath(__file__))
	filename = best.download(filepath=dir+'/'+video.title+'.'+best.extension)
print(__file__) #contains full path
print(__name__) # __name__ == file name while importing
if __name__=='__main__' :
	if len(sys.argv)<2:
		print('Usage : python_latest_version filepath Website_Url')
	else:
		download(sys.argv[1])

# Use python2 to use pafy module :)
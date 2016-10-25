# Python_Youtube_Downloader
This repository contains four different scripts to download videos and songs from youtube by making the use of module "PAFY".
Here is how to use the module "PAFY" in your own python code. 

>>> import pafy
create a video instance from a YouTube url:

>>> url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
>>> video = pafy.new(url)
get certain attributes:

>>> video.title
'Richard Jones: Introduction to game programming - PyCon 2014'

>>> video.rating
5.0

>>> video.viewcount, video.author, video.length
(1916, 'PyCon 2014', 10394)

>>> video.duration, video.likes, video.dislikes
('02:53:14', 25, 0)

>>> print(video.description)
Speaker: Richard Jones

list available streams for a video:

>>> streams = video.streams
>>> for s in streams:
...     print(s)
...
normal:mp4@1280x720
normal:webm@640x360
normal:mp4@640x360
normal:flv@320x240
normal:3gp@320x240
normal:3gp@176x144
show all formats, file-sizes and their download url:

>>> for s in streams:
...    print(s.resolution, s.extension, s.get_filesize(), s.url)
...
1280x720 mp4 2421958510 https://r1---sn-aiglln7e.googlevideo.com/videoplayba[...]
640x360 webm 547015732 https://r1---sn-aiglln7e.googlevideo.com/videoplaybac[...]
640x360 mp4 470655850 https://r1---sn-aiglln7e.googlevideo.com/videoplayback[...]
320x240 flv 345455674 https://r1---sn-aiglln7e.googlevideo.com/videoplayback[...]
320x240 3gp 208603447 https://r1---sn-aiglln7e.googlevideo.com/videoplayback[...]
176x144 3gp 60905732 https://r1---sn-aiglln7e.googlevideo.com/videoplayback?[...]
get best resolution regardless of file format:

>>> best = video.getbest()
>>> best.resolution, best.extension
('1280x720', 'mp4')
get best resolution for a particular file format: (mp4, webm, flv or 3gp)

>>> best = video.getbest(preftype="webm")
>>> best.resolution, best.extension
('640x360', 'webm')
get url, for download or streaming in mplayer / vlc etc:

>>> best.url
'http://r12---sn-aig7kner.c.youtube.com/videoplayback?expire=1369
Download video and show progress:

>>> best.download(quiet=False)
3,734,976 Bytes [0.20%] received. Rate: [ 719 KB/s].  ETA: [3284 secs]
Download video, use specific directory and/or filename:

>>> filename = best.download(filepath="/tmp/")

>>> filename = best.download(filepath="/tmp/Game." + best.extension)
Get audio-only streams (m4a and/or ogg vorbis):

>>> audiostreams = video.audiostreams
>>> for a in audiostreams:
...     print(a.bitrate, a.extension, a.get_filesize())
...
256k m4a 331379079
192k ogg 172524223
128k m4a 166863001
128k ogg 108981120
48k m4a 62700449
Download the 2nd audio stream from the above list:

>>> audiostreams[1].download()
Get the best quality audio stream:

>>> bestaudio = video.getbestaudio()
>>> bestaudio.bitrate
'256'
Download the best quality audio file:

>>> bestaudio.download()
show all media types for a video (video+audio, video-only and audio-only):

>>> allstreams = video.allstreams
>>> for s in allstreams:
...     print(s.mediatype, s.extension, s.quality)
...

normal mp4 1280x720
normal webm 640x360
normal mp4 640x360
normal flv 320x240
normal 3gp 320x240
normal 3gp 176x144
video m4v 1280x720
video webm 1280x720
video m4v 854x480
video webm 854x480
video m4v 640x360
video webm 640x360
video m4v 426x240
video webm 426x240
video m4v 256x144
video webm 256x144
audio m4a 256k
audio ogg 192k
audio m4a 128k
audio ogg 128k
audio m4a 48k

Installation : 

pafy can be installed using pip:

$ [sudo] pip install pafy
or use a virtualenv if you don’t want to install it system-wide:

$ virtualenv venv
$ source venv/bin/activate
$ pip install pafy

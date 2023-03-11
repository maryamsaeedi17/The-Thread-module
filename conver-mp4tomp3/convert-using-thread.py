from threading import Thread
from time import time
from moviepy import editor

def convert(video_name, audio_name):
    video = editor.VideoFileClip(video_name)
    video.audio.write_audiofile(audio_name)

videos=[["baran nikrah- ayeneh.mp4", "ayeneh2.mp3"],
        ["baran nikrah- baz baran.mp4", "baz baran2.mp3"],
        ["baran nikrah- cheghadr gozashte'am.mp4", "cheghadr gozashte'am2.mp3"],
        ["fatemeh mohammadi- monajat torki.mp4", "monajat torki2.mp3"],
        ["khosro shakibayi- Ziba.mp4", "Ziba2.mp3"],
        ["mojtaba shakoori- zendegi.mp4", "zendegi2.mp3"]
]

start_time=time()

threads=[]
for video,audio in videos:
    new_thread=Thread(target=convert,args=[video,audio])
    threads.append(new_thread)

for t in threads:
    t.start()

for t in threads:
    t.join()


end_time=time()

print(end_time-start_time)

#result= 32.042940616607666

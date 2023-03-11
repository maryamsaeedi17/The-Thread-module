from time import time
from moviepy import editor

def convert(video_name, audio_name):
    video = editor.VideoFileClip(video_name)
    video.audio.write_audiofile(audio_name)

videos=[["baran nikrah- ayeneh.mp4", "ayeneh.mp3"],
        ["baran nikrah- baz baran.mp4", "baz baran.mp3"],
        ["baran nikrah- cheghadr gozashte'am.mp4", "cheghadr gozashte'am.mp3"],
        ["fatemeh mohammadi- monajat torki.mp4", "monajat torki.mp3"],
        ["khosro shakibayi- Ziba.mp4", "Ziba.mp3"],
        ["mojtaba shakoori- zendegi.mp4", "zendegi.mp3"]
]

start_time=time()

for video, audio in videos:
    convert(video, audio)


end_time=time()

print(end_time-start_time)

#result=27.624950408935547 s
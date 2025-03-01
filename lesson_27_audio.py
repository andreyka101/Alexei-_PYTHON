# pip install audioplayer


from audioplayer import AudioPlayer


audio = AudioPlayer("audio.mp3")


print("start")
audio.play(block=True)
print("end")




# audio.play()
# input("12222")
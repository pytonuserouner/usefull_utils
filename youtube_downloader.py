from pytube import YouTube


"""
Загрузка видео с Youtube.
"""


link = input("Enter the link of youtube video:  ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download("Downloads\python")
print("Download completed!!")
import streamlink
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

def stream_video(window, video_frame, url):
    streams = streamlink.streams(url)
    if streams:
        stream_url = streams['best'].url
        cap = cv2.VideoCapture(stream_url)

        def update_frame():
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                video_frame.config(image=photo)
                video_frame.image = photo
                window.after(30, update_frame)

        update_frame()

# 메인 코드
root = tk.Tk()
video_frame = tk.Label(root)
video_frame.pack()

youtube_url = "https://www.youtube.com/live/F-0nWc4dKE4?si=MfdKaQHFp_oIRn2n"
stream_video(root, video_frame, youtube_url)

root.mainloop()
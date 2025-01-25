from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=xxxxx'])


# Command line
# yt-dlp 'https://www.youtube.com/watch?v=xxxx'
# Mandatory download: ffmpeg from ubuntu app center
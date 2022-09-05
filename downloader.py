#!/usr/bin/env python3
'''Download FLAC audio from Youtube using a CSV in the format: Title, Artist, Album, Link'''
import os
import sys
import csv
from mutagen.flac import FLAC

OUTDIR = sys.argv[2] # cannot have ending slash

def _make_safe(_str):
    return ''.join([chr(c) for c in _str.encode('ascii', 'ignore') if not chr(c) in r'\|/*?<>:"\''])

for file in sys.argv[1:]:
    try:
        data = [tuple(line) for line in csv.reader(open(file, 'r', encoding='utf-8'))]
    except Exception as ee: # pylint: disable=broad-except
        print(f'Error: Could not open and parse file \'{file}\'')
        continue

    for x, line in enumerate(data):
        try:
            artist, title, album, link,*_ = line
            safe_artist, safe_title = _make_safe(artist), _make_safe(title)
            if not os.path.exists(f'{title} - {artist}.flac'):
                os.system(f'yt-dlp -x \"{link}\" --audio-format \"flac\" \
                          -o \"{os.path.join(OUTDIR, f"{safe_title} - {safe_artist}.%(ext)s")}\"')
                audio = FLAC(os.path.join(OUTDIR, f"{safe_title} - {safe_artist}.flac"))
                audio['TITLE'] = title
                audio['ARTIST'] = artist
                audio['ALBUM'] = album

                audio.save()
        except Exception as e: # pylint: disable=broad-except
            print(f'Error: Line {x} in file \'{file}\': {line}')
            print(e)

# NOTE: add these
# doom soundtrack
# bruno mars
# daft punk
# David Guetta
# avicii
# maroon 5
# metallica
# me me me 3 parts english
# Two Steps From Hell
# Tank!
# Cruel Angel's Thesis (Eng)


# NOTE: Last Song: NF - The Search

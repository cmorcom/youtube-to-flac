# youtube-to-flac
Python script to download FLAC audio from youtube. Additional script added to convert FLAC to ALAC for my iPod Classic.

## Run Notes
Run the script using python3 (I use 3.10)
Usage:
```python
/usr/bin/python3 downloader.py INPUT.csv /path/to/output/dir
```

## Input File Format
For simplicity, see the excel or csv I used. The CSV format is:
```csv
Title, Artist, Album, Link
```
Be mindful of special characters that can ruin paths or are not ascii. These are ignored using the `_make_safe()` method. 
This will be updated later.

## FLAC to ALAC
Use foobar2000. I've been getting crackling noise from how my script does it.

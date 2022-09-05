import os
for root,dirs,files in os.walk('..'):
    print(files)
    for f in files:
        if f.endswith('.flac'):
            print(f'ffmpeg -i \"..\\{f}.flac\" -acodec alac \"..\\alac\\{f}.m4a\"')
            os.system(f'ffmpeg -i \"..\\{f}.flac\" -acodec alac \"..\\alac\\{f}.m4a\"')
            exit(0)
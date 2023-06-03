from Mytools.music.core.music_run import Mymusic

if __name__ == '__main__':
    try:
        Thismusic = input("<this.name.music>")
        Thislist = Thismusic.endswith(".mp3")
        if Thislist:

            pass
        else:
            Thismusic += ".mp3"
        Mymusic(family='True',
                name=fr'..\lib\music\{Thismusic}',
                number=2).music()
    except:
        pass

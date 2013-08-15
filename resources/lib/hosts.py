import resources.lib.util as util


class Host():
    __thumb = ''

    def __init__(self, server, label, thumb=None):
        self.server = server
        self.label = label

        if thumb:
            self.__thumb = thumb

    @property
    def thumb(self):
        return self.__thumb


''' Resolvable Hosts '''
dailymotion = Host('dailymotion.com', 'Daily Motion', 'dailymotion.png')
facebook = Host('facebook.com', 'Facebook', 'facebook.png')
hostingbulk = Host('hostingbulk.com', 'Hosting Bulk')
nowvideo = Host('nowvideo.eu', 'Now Video', 'nowvideo.png')
putlocker = Host('putlocker.com', 'PutLocker', 'putlocker.png')
tunepk = Host('tune.pk', 'Tune PK', 'tunepk.jpg')
videoweed = Host('videoweed.es', 'Video Weed', 'videoweed.jpg')
youtube = Host('youtube.com', 'Youtube', 'youtube.png')

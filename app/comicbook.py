import os
from natsort import natsorted


class comicbook(object):
    filelist = []

    def __init__(self, name, filename=None):
        self.name = name.replace('//', '/')
        self.localpath = "res/" + name + "/"
        self.filename = filename
        self.generate_filelist()
        if self.filename is None or not self.filename:
            self.filename = self.filelist[0]

    def generate_filelist(self):
        x, dlist, flist = os.walk(self.localpath).next()
        # Filter out system files
        flist = [v for v in flist if not v.startswith('.')]
        flist = [v for v in flist if not v.startswith('Thumbs.db')]
        flist = [v for v in flist if not v.startswith('desktop.ini')]
        flist = [v for v in flist if not v.endswith('.txt')]
        flist = [v for v in flist if not v.endswith('.url')]
        flist = [v for v in flist if not v.startswith('README')]
        # Sort files
        self.filelist = natsorted(flist)
        self.dirlist = natsorted(dlist)

    def thumbnail_path(self):
        try:
            print self.filelist[0]
            return self.filelist[0]
        except IndexError:
            return None

    def thumbnail_mimetype(self):
        return 'image/jpeg'

    def get_prev_image(self):
        idx = self.current_image() - 1
        if idx >= 0:
            return os.path.join('/', self.name, self.filelist[idx])
        else:
            return os.path.join('/', self.name)

    def get_next_image(self):
        idx = self.current_image() + 1
        if idx < len(self.filelist):
            return os.path.join('/', self.name, self.filelist[idx])
        else:
            return os.path.join('/', self.name, '..').rstrip('/')

    def get_image(self):
        return os.path.join('/', self.name, self.filename, 'img')

    def current_image(self):
        return self.filelist.index(self.filename)

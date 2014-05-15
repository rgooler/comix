import os
import sys
from natsort import natsorted

class comicbook(object):
    filelist = []

    def __init__(self, name, filename=None):
        self.name = name
        self.path = name + "/"
        self.localpath = "res/" + name + "/"
        self.filename = filename
        self.generate_filelist()
        if self.filename is None or not self.filename:
            self.filename = self.filelist[0]        

    def generate_filelist(self):
        x, self.dirlist, self.filelist = os.walk(self.localpath).next()
        #Filter out system files
        self.filelist = [ v for v in self.filelist if not v.startswith('.') ]
        self.filelist = [ v for v in self.filelist if not v.startswith('thumbs.db') ]
        self.filelist = [ v for v in self.filelist if not v.startswith('desktop.ini') ]
        self.filelist = [ v for v in self.filelist if not v.endswith('.txt') ]
        self.filelist = [ v for v in self.filelist if not v.startswith('README') ]

    def thumbnail_path(self):
        try:
            return self.filelist[0]
        except IndexError:
            return None

    def thumbnail_mimetype(self):
        return 'image/jpeg'

    def get_prev_image(self):
        try:
            idx = self.current_image() - 1
            if idx >= 0:
                return os.path.join('/', self.name, self.filelist[idx])
            else:
                return os.path.join('/', self.name)
        except IndexError:
            print "get_prev_image - IndexError"
            return os.path.join('/', self.name)

    def get_next_image(self):
        try:
            idx = self.current_image() + 1
            if idx < len(self.filelist):
                return os.path.join('/', self.name, self.filelist[idx])
            else:
                return os.path.join('/', self.name, '..')
            return 
        except IndexError:
            return os.path.join('/', self.name, '..')

    def get_image(self):
        try:
            return os.path.join('/', self.name, self.filename, 'img')
        except IndexError:
            return None

    def current_image(self):
        return self.filelist.index(self.filename)
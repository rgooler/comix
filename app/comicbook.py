import os
import sys
from natsort import natsorted


class comicbook(object):
    filelist = []

    def __init__(self, name):
        self.name = name
        self.path = name + "/"
        self.localpath = "res/" + name + "/"
        self.generate_filelist()

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

    def get_prev_image(self, filename=None):
        try:
            prevfile = self.filelist[self.current_image() - 1]
            return os.path.join('/', self.name, prevfile)
        except IndexError:
            return os.path.join('/', self.name)

    def get_next_image(self,filename=None):
        try:
            nextfile = self.filelist[self.current_image(filename) + 1]
            return os.path.join('/', self.name, nextfile)
        except IndexError:
            return '/'

    def get_image(self, filename=None):
        try:
            if filename is None or not filename: 
                filename = self.filelist[0]
            return os.path.join('/', self.name, filename, 'img')
        except IndexError:
            return None

    def current_image(self, filename=None):
        if filename is None or not filename:
            return 0
        return self.filelist.index(filename)


if __name__ == "__main__":
    try:
        first_comic = os.walk('../res/').next()[1][1]
        #first_comic = [x[0].replace('../res/','',1) for x in os.walk('../res/')][1]
    except IndexError:
        print "Cannot find any comics"
        sys.exit(1)
    cb = comicbook(first_comic)

    import pprint
    pp = pprint.PrettyPrinter(indent=2)
    pp = pp.pprint
    pp(cb.__dict__)
    pp(get_list_of_images)
import os
import sys
from natsort import natsorted


class comicbook(object):
    current_image = 0
    filelist = []

    def __init__(self, name):
        self.name = name
        self.path = name + "/"
        self.localpath = "res/" + name + "/"
        self.generate_filelist()

    def generate_filelist(self):
        x, self.dirlist, self.filelist = os.walk(self.localpath).next()
        print self.localpath
        print x
        print self.dirlist
        print self.filelist
        x, self.dirlist, self.filelist = os.walk(self.localpath).next()
        print self.localpath
        print x
        print self.dirlist
        print self.filelist

    def thumbnail_path(self):
        return self.filelist[0] or None


    def thumbnail_mimetype(self):
        return 'image/jpeg'

    def get_next_image(self):
        if self.current_image == 0:
            return None
        else:
            return self.filelist[self.current_image - 1]

    def get_prev_image(self):
        try:
            return self.filelist[self.current_image + 1]
        except IndexError:
            return None

    def get_image(self, index=None):
        try:
            if index is None: index = 0
            return os.path.join(self.name, self.filelist[index])
        except IndexError:
            return None


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
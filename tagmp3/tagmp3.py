#!/usr/bin/env python2.7

import ConfigParser
import shutil
import sys

import eyed3

config = ConfigParser.ConfigParser()
config.read('sermon.ini')
metadata = dict(config.items('DEFAULT'))

filename = '{}-{}-{}.mp3'.format(
    metadata['date'],
    metadata['series'],
    metadata['title']
)
shutil.copyfile(sys.argv[1], filename)

sermon = eyed3.load(filename)

# audiofile.tag.save()

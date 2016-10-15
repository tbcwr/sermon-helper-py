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
sermon.tag.title = unicode('{} ({})'.format(metadata['verse'], metadata['title']))
# TODO: sermon.tag.composer = unicode(metadata['preacher'])
sermon.tag.artist = unicode(metadata['church'])
sermon.tag.album = unicode(metadata['series'])
sermon.tag.album_artist = unicode(metadata['church'])
sermon.tag.genre = unicode("Sermon")
# TODO: sermon.tag.recording_date = dateutil.parser.parse(metadata['date'])
sermon.tag.save()

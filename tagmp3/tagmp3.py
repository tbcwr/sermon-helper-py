#!/usr/bin/env python2.7

import ConfigParser
import shutil
import sys

import eyed3
from eyed3.id3.frames import ImageFrame

config = ConfigParser.ConfigParser()
config.read('sermon.ini')
metadata = dict(config.items('DEFAULT'))

filename = '{}-{}-{}.mp3'.format(
    metadata['date'],
    metadata['series'],
    metadata['title']
)
shutil.copyfile(metadata['source'], filename)

sermon = eyed3.load(filename)
sermon.tag.title = unicode('{} ({})'.format(metadata['verse'], metadata['title']))
sermon.tag.setTextFrame('TCOM', unicode(metadata['preacher']))   # composer
sermon.tag.artist = unicode(metadata['church'])
sermon.tag.album = unicode(metadata['series'])
sermon.tag.album_artist = unicode(metadata['church'])
sermon.tag.genre = unicode("Sermon")
sermon.tag.setTextFrame('TYER', unicode(metadata['date'].split('-', 1)[0]))      # Recording Year

# Example: https://github.com/nicfit/eyed3/blob/360357c9248649526ef5a45569fbbe98464accc9/src/eyed3/plugins/classic.py#L943
# Signature: https://github.com/nicfit/eyed3/blob/360357c9248649526ef5a45569fbbe98464accc9/src/eyed3/id3/tag.py#L1373
with open(metadata['artwork'], "rb") as artwork_image:
    sermon.tag.images.set(ImageFrame.OTHER, artwork_image.read(), 'image/PNG')

sermon.tag.save()

#!/usr/bin/env python2.7

import ConfigParser
import shutil
import sys

import eyed3
from eyed3.id3.frames import ImageFrame

REQUIRED_CONFIGS = {
    'artwork',
    'church',
    'date',
    'preacher',
    'series',
    'source',
    'title',
    'verse'
}

config = ConfigParser.ConfigParser()
config.read('sermon.ini')
metadata = dict(config.items('DEFAULT'))

missing_configs = REQUIRED_CONFIGS - set(metadata.keys())
if missing_configs:
    for config in missing_configs:
        print("Missing '{}' config in sermon.ini.".format(config))
    sys.exit(1)

for key, value in metadata.iteritems():
    if not value:
        print("Config '{}' not set in sermon.ini.".format(key))
        sys.exit(1)

filename = '{}-{}-{}.mp3'.format(
    metadata['date'],
    metadata['series'],
    metadata['title']
)
shutil.copyfile(metadata['source'], filename)

sermon = eyed3.load(filename)
# http://stackoverflow.com/a/31327380/2687324
sermon.initTag()

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

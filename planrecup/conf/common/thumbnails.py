'''
Created on 15 janv. 2014

@author: rux
'''
from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS


THUMBNAIL_PRESERVE_EXTENSIONS = ('png',)
THUMBNAIL_DEBUG = False
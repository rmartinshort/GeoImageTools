#!/usr/bin/env python 

import chopper as ic
from sklearn.pipeline import Pipeline


image_pipeline = Pipeline(
    [ 
        ('chop_image',ic.ImageChopper())
    ] 
)
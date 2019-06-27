#!/usr/bin/env python
#RMS 2019

import pipeline
from config import config

def run_test() -> None:

	infilename = '../example_data/myExportImageTask4.tif'

	X = pipeline.image_pipeline.fit_transform(infilename)

	print(X)


if __name__ == "__main__":

	run_test()
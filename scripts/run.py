#!/usr/bin/env python

from iBeatles.iBeatles import main

import multiprocessing
import sys

__file__ = "iBeatles"

# Run the GUI
multiprocessing.freeze_support()
sys.exit(main(sys.argv))

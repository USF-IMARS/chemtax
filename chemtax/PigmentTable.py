import logging

import pandas

from dep.SB_support import readSB

class PigmentTable(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def load_seabass_file(self, filepath):
        reader = readSB(
            filename=filepath
        )
        self.df = pandas.DataFrame(reader.data)
        return self

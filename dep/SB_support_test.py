# std modules:
from unittest import TestCase

# modules from this package:
from test_data.TestDataHelper import get_test_files, TestFileType

# tested module(s):
from dep.SB_support import readSB

class Test_SB_support_readSB(TestCase):

    # === tests ============================================================
    def test_loading_all_sb_files(self):
        """ readSB can load all test .sb files """
        for test_file in get_test_files(
            lambda d: d['type'] == TestFileType.seabass
        ):
            reader = readSB(
                filename=test_file
            )

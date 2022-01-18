# std modules:
from unittest import TestCase

# modules from this package:
from chemtax.PigmentTable import PigmentTable
from test_data.TestDataHelper import get_test_files, TestFileType

# tested module(s):
from chemtax.guess_taxa_from_pigments import guess_taxa_from_pigments

class Test_guess_taxa_from_pigments(TestCase):
    TEST_PIGMENT_TABLES = [
        PigmentTable().load_seabass_file(test_file) for test_file in get_test_files(
            lambda d: d['type'] == TestFileType.seabass
        )
    ]
    # === tests ============================================================
    def test_calls(self):
        """ can guess taxa from all .sb files w/o throwing exceptions """
        for pigment_table in self.TEST_PIGMENT_TABLES:
            guess_taxa_from_pigments(
                pigment_dataframe = pigment_table,
                taxa_list=[],
            )

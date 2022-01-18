"""
This file contains info on the included test data and helper methods useful
for importing file & data into tests.
"""

def get_test_files(filter_function):
    """
    returns iterable of all file types matching the filter lambda

    examples:
    ---------
    get_test_files(lambda d: d['type'] == TestFileType.seabass)
    get_test_files(lambda d: 'real_data' in d['tags'])
    get_test_files(lambda d: d['fname'] == '73414bf657_WS16074_HPLC.sb')
    """
    list_of_dicts = filter(filter_function, TEST_FILES)
    return ['test_data/' + file_dict['fpath'] for file_dict in list_of_dicts]


class TestFileType:
    seabass = '.sb'


class TestFile(dict):
    def __init__(self, type, fpath, description, tags):
        self['type'] = type
        self['fpath'] = fpath
        self['description'] = description
        self['tags'] = tags


"""
# To add a test file to the TEST_FILES variable use the following boilerplate:
TestFile(
    type=TestFileType.filetype_name_here,
    fpath="filepath_to_the_file_relative_to_test_data_dir",
    description="human-readable notes here.",
    tags=[],
),
"""
TEST_FILES = [
TestFile(
    type=TestFileType.seabass,
    fpath="73414bf657_WS16074_HPLC.sb",
    description="file provided to Tylar via email by Seabastian on 2022-01.",
    tags=['real_data'],
),

]  # NOTE: TEST_FILES should be the last thing in the file

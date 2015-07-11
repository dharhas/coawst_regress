import os

def get_coawst_path():
    """get path for coawst source code

    This looks in current directory for the config file
    """
    path = os.getcwd()
    filename = os.path.join(path, 'coawst_config.txt')
    with open(filename) as f:
        try:
            path = f.read().strip()
            return path
        except:
            raise IOError('unable to read coawst_config.txt in the current directory')


def get_testcases_path():
    """get location of testcases template dir
    """
    return os.path.join(os.path.dirname(__file__), 'testcases')
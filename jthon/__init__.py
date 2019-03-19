from .jthon import Jthon


def load(file: str=None, data={}):
    '''Load a file into memory

    Parameters
    -----------
    file : Required[:class:`str`]
            Provide the file you'd like to load into memory, Example; file = jthon.load('test_file')
    '''
    return Jthon(file, data)

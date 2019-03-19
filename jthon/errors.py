class Jthon_Error(Exception):
    pass


class Jthon_Name_Error(Jthon_Error):
    def __init__(self):
        message = 'Cannot save a file that has no name'
        super(Jthon_Name_Error, self).__init__(message)

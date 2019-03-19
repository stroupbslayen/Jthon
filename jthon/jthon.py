import os
import json
from . import errors
from .found import Found

default_arg = "god_please_don't_let_this_exist"


def filter(value, items, exact):
    if exact:
        return
    try:
        if value in items:
            return True
    except:
        return


class Jthon:
    '''Allows for easier manipulation of json files.

    It will check if a json file already exists with the given file name and open that, otherwise it will create a new one.

    Default datatype is a DICT, although you can pass what you want to it. EX: example=jthon.load(file_name,[]) would pass a list to the json.

    To update the data, modify the json using the "data" attribute. EX: example.data.append('test') would add 'test' to the list declared above.

    Commit changes with the "save" attribute. EX: example.save() would save the changes to the json file'''

    def __init__(self, file=None, data={}):
        if file:
            if not file.endswith('.json'):
                file = file + '.json'
            if not os.path.isfile(file):
                pass
            else:
                try:
                    with open(file) as f:
                        data = json.load(f)
                except ValueError:
                    pass
        self.file_name = file
        self.data = data
        self.type = type(self.data)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, given):
        try:
            return self.data[given]
        except:
            return

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def get(self, key, default=None):
        if isinstance(self.data, dict):
            v = self.data.get(key, default)
            if v is not None:
                return Jthon(data=v)
        if isinstance(self.data, (list, tuple)):
            try:
                return self.data.index(key)
            except ValueError:
                return default

    def save(self, file=None, sort_keys: bool = True):
        '''Save your json file

                Parameters
                -----------
                file : Optional[:class:`str`]
                        You can specifiy a different file name with this option.
                sort_keys : Optional[:class:`bool`]
                        Define if you want to sort keys, True/False/None. Example; `sort_keys=None` True by default.

                Example:
                file.save(sort_keys=None)
                '''
        if not self.file_name and not file:
            raise errors.Jthon_Name_Error
        else:
            if file:
                self.file_name = file
            if not self.file_name.endswith('.json'):
                self.file_name = self.file_name + '.json'
            with open(self.file_name, "w") as f:
                json.dump(self.data, f, indent=4, sort_keys=sort_keys)

    def find(self, key=default_arg, value=default_arg, limit: int = None, exact=True):
        '''Returns a list of dicts whos key matches the searched key

                Parameters
                -----------
                value : Required[:class:`str`]
                        A string to search for in value, can set to be exact or in.
                key : Required[:class:`str`]
                        A string to search for in key, can set to be exact or in.			
                limit : Optional[:class:`int`]
                        A limit on the amount of keys to return in the search, example; `limit=5` would return the first 5 results.
                exact : Optional[:class:`bool`]
                        An option to search for an exact match or an `in` string of keys. Example; `exact=False` would search for `contains`

                Example:
                file = jthon.load('EarthquakeExample')
                x = file.find(value='Anchorage', limit=3, exact=False)
                for v in x:
                        print(v.value)

                Returns
                -----------
                Find returns a list of `Found` Objects,
                key - A `list` of keys found that match.
                value - A `list` of values found that match.
                siblings -  A `dataset` that your found object belongs to.

                Extension of above;
                x = file.find(value='Anchorage', limit=3, exact=False)
                print(x.siblings)

                '''
        lst = []
        #parent = None
        if isinstance(self.data, (list, tuple)):
            for item in self.data:
                lst += Jthon(data=item).find(key, value=value, limit=limit, exact=exact)
        elif isinstance(self.data, dict):
            for k, v in self.data.items():
                if isinstance(v, dict):
                    lst += Jthon(data=v).find(key, value=value, limit=limit, exact=exact)
                elif isinstance(v, (list, tuple)):
                    lst += Jthon(data=v).find(key, value=value, limit=limit, exact=exact)
                if k == key:
                    if value != default_arg or filter(value, v, exact):
                        if v == value:
                            lst.append(Found(k, v, self.data))
                    else:
                        lst.append(Found(k, v, self.data))
                elif v == value or filter(value, v, exact):
                    lst.append(Found(k, v, self.data))
                if limit and limit <= len(lst):
                    break
        if limit:
            return lst[:limit]
        return lst

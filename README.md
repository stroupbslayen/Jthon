# Jthon

This is a utility to make working with JSON files easier.

## Installation
```py
pip install jthon
```

## Example

```py
from jthon import Jthon

'''Creates or reads a json file if it already exists and Passes a list as the datatype. The default datatype is a dict'''

file = Jthon('json_file') # Enter the name of the JSON file. If the file exists then the data attribute will be the contents of the file.

file.data['key'] = 'value' # Add a key and value to the data attribute

file.save() # The current state of the data attribute will be saved to JSON file

```
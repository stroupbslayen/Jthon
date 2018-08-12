# Example

```py
from pyson import Pyson

'''Creates or reads a json file if it already exists and Passes a list as the datatype. The default datatype is a dict'''

x=Pyson('json_file',[]) 

x.data.append('something') # Data is stored and called with the data attribute

x.save # The current state of the data attribute will be saved to json_file
```
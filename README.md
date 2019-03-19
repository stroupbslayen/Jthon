# Jthon

This is a utility to make working with JSON files easier.

## Installation 

pip install jthon


### Usage
```
import jthon
file = jthon.load('test_file')
urls = file.find('url', limit=2)
print(f"Number of results limited to [{len(urls)}]: {', '.join(str(url) for url in urls)}")
title = file.get('data').get('children')[1].get('data').get('title')
print(title)
file['data']['dist'] = 25
file.save(sort_keys=None)
```
More examples can be found in the examples folder
### Requirements

```
python3 >
```



## Authors
* **StroupBSlayen** - [GitHub](https://github.com/stroupbslayen)
* **ProbsJustin** - [GitHub](https://github.com/SobieskiCodes)

## License

This project is licensed under MIT - see the [LICENSE.md](LICENSE) file for details



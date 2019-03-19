import jthon
file = jthon.load('test_file')
urls = file.find('url', limit=2)
print(f"Number of results limited to [{len(urls)}]: {', '.join(str(url) for url in urls)}")
title = file.get('data').get('children')[1].get('data').get('title')
print(title)
file['data']['dist'] = 25
file.save(sort_keys=None)

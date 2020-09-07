# pyrss
A python library to scrape RSS !
## Installation!
```bash
git clone https://github.com/alirezadigi/pyrss.git
cd ./pyrss
sudo python3 setup.py install #linux
python setup.py install #windows
```
## Basic usage
```python
import pyrss
from requests import get

url = "http://www.isna.ir/rss"
url_content = get(url).text

rss_soup = pyrss.parserss(url_content)
for item in rss_soup.find_all("item"):
    print(item.title.text)
    print(item.link.text)
    print()
 
```
## TODO list
- [ ] Adding project to pypi!
- [ ] Adding some more features!

# HTML Table Extractor
_HTML Table Extractor is a python library that uses [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) extract data from complicated and messy html table_

## Important links
* Repository: https://github.com/yuanxu-li/html-table-extractor
* Issues: https://github.com/yuanxu-li/html-table-extractor/issues

## Installation

```bash
pip install 'beautifulsoup4==4.5.3'
pip install html-table-extractor
```

## Usage

```python
from html_table_extractor.extractor import Extractor
table_doc = """
<table><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>
"""
extractor = Extractor(table_doc)
extractor.parse()
extractor.return_list()
```

## Team

* Justin Li

## Errors/ Bugs

If something is not working correctly, or if you have any suggestion on improvements, [report it here](https://github.com/yuanxu-li/table-extractor/issues)

## Copyright

Copyright (c) 2017 Justin Li. Released under the [MIT License](https://github.com/yuanxu-li/html-table-extractor/blob/master/README.md)

Third-party copyright in this distribution is noted where applicable.
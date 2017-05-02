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

### Example 1

<table><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>

```python
from html_table_extractor.extractor import Extractor
table_doc = """
<table><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>
"""
extractor = Extractor(table_doc)
extractor.parse()
extractor.return_list()
```
It will print out:
```python
[[u'1', u'2'], [u'3', u'4']]
```

### Example 2

<table>
    <tr>
        <td rowspan=2>1</td>
        <td>2</td>
        <td>3</td>
    </tr>
    <tr>
        <td colspan=2>4</td>
    </tr>
    <tr>
        <td colspan=3>5</td>
    </tr>
</table>

```python
from html_table_extractor.extractor import Extractor
table_doc = """
<table>
  <tr>
    <td rowspan=2>1</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <td colspan=2>4</td>
  </tr>
  <tr>
    <td colspan=3>5</td>
  </tr>
</table>
"""
extractor = Extractor(table_doc)
extractor.parse()
extractor.return_list()
```
It will print out:
```python
[[u'1', u'2', u'3'], [u'1', u'4', u'4'], [u'5', u'5', u'5']]
```

### Example 3

<table>
    <tr>
        <td rowspan=2>1</td>
        <td>2</td>
        <td rowspan=3>3</td>
    </tr>
    <tr>
        <td colspan=2>4</td>
    </tr>
    <tr>
        <td colspan=2>5</td>
    </tr>
</table>

```python
from html_table_extractor.extractor import Extractor
table_doc = """
<table>
    <tr>
        <td rowspan=2>1</td>
        <td>2</td>
        <td rowspan=3>3</td>
    </tr>
    <tr>
        <td colspan=2>4</td>
    </tr>
    <tr>
        <td colspan=2>5</td>
    </tr>
</table>
"""
extractor = Extractor(table_doc)
extractor.parse()
extractor.return_list()
```
It will print out:
```python
[[u'1', u'2', u'3'], [u'1', u'4', u'3'], [u'5', u'5', u'3']]
```

## Team

* Justin Li

## Errors/ Bugs

If something is not working correctly, or if you have any suggestion on improvements, [report it here](https://github.com/yuanxu-li/table-extractor/issues)

## Copyright

Copyright (c) 2017 Justin Li. Released under the [MIT License](https://github.com/yuanxu-li/html-table-extractor/blob/master/README.md)

Third-party copyright in this distribution is noted where applicable.

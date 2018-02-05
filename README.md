# HTML Table Extractor
[![Build Status](https://travis-ci.org/yuanxu-li/html-table-extractor.svg?branch=master)](https://travis-ci.org/yuanxu-li/html-table-extractor)

_HTML Table Extractor is a python library that uses [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) to extract data from complicated and messy html table_

## Important links
* Repository: https://github.com/yuanxu-li/html-table-extractor
* Issues: https://github.com/yuanxu-li/html-table-extractor/issues

## Installation

```bash
pip install 'beautifulsoup4==4.5.3'
pip install html-table-extractor
```

## Usage

### Example 1 - Simple

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

### Example 2 - Transformer

<table><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>

```python
from html_table_extractor.extractor import Extractor
table_doc = """
<table><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>
"""
extractor = Extractor(table_doc, transformer=int)
extractor.parse()
extractor.return_list()
```
It will print out:
```python
[[1, 2], [3, 4]]
```

### Example 3 - Pass BS4 Tag

<table><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>

```python
from html_table_extractor.extractor import Extractor
from bs4 import BeautifulSoup
table_doc = """
<html><table id='wanted'><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table><table id='unwanted'><tr><td>not wanted</td></tr></table></html>
"""
soup = BeautifulSoup(table_doc, 'html.parser')
extractor = Extractor(soup, id_='wanted')
extractor.parse()
extractor.return_list()
```
It will print out:
```python
[[u'1', u'2'], [u'3', u'4']]
```

### Example 4 - Complex

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

### Example 5 - Conflicted

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

### Example 6 - Write to file

<table><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>

```python
from html_table_extractor.extractor import Extractor
table_doc = """
<table><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>
"""
extractor = Extractor(table_doc).parse()
extractor.write_to_csv(path='.')
```
It will write to a given path and create a new csv file called `output.csv`:
```
1,2
3,4

```

## Team

* [@yuanxu-li](https://github.com/yuanxu-li)

## Errors/ Bugs

If something is not working correctly, or if you have any suggestion on improvements, [report it here](https://github.com/yuanxu-li/table-extractor/issues)

## Copyright

Copyright (c) 2017 Justin Li. Released under the [MIT License](https://github.com/yuanxu-li/html-table-extractor/blob/master/README.md)

Third-party copyright in this distribution is noted where applicable.

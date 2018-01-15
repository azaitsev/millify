# millify
Convert long numbers into a human-readable format in Python

## Installation
```bash
pip install millify
```

## Usage

### Convert to number with binary prefix
```python
from millify import millify

millify(1234)
# '1k'

millify('1234') #same for strings
# '1k'

millify(12345678)
# '12M'

millify(12345678, precision=2)
# '12.35M'

millify(10000, precision=2) # hide nulls in decimals by default
# '10k'

millify(10000, precision=2, drop_nulls=False)
# '10.00k'

prefixes = ['kB', 'MB', 'GB']
millify(10000, prefixes=prefixes)
# '10kB'
```


### Add a thousands separator

```python
from millify import prettify

prettify(1234)
# '1,234'

prettify('1234') #same for strings
# '1,234'

prettify(1234, '`')
# '1`234'

```

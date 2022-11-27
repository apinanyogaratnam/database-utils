# Postgres Database Utils

A python package for postgres database utilities.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Install the package using pip:

```sh
pip install database-utils
```

## Usage

Create a database connection:
```python
from postgres_database_utils import create_connection

connection = create_connection(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="postgres",
)
```

## Support

Please [open an issue](https://github.com/apinanyogaratnam/postgres-database-utils/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/apinanyogaratnam/postgres-database-utils/compare/).

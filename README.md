# Postgres Database Utils

[![Downloads](https://static.pepy.tech/personalized-badge/postgres-database-utils?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/postgres-database-utils)

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
from postgres_database_utils import create_connection, PostgresCredentials

credentials = PostgresCredentials(host='localhost', database='postgres', user='postgres', password='postgres', port=5432)

connection = create_connection(credentials)
```

## Support

Please [open an issue](https://github.com/apinanyogaratnam/postgres-database-utils/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/apinanyogaratnam/postgres-database-utils/compare/).

<!-- TODO: remove parameters from create_connection except postgres credentials on next version update -->

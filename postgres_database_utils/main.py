import warnings

import pandas as pd
import psycopg2

warnings.filterwarnings("ignore")


class PostgresCredentials:
    def __init__(self: 'PostgresCredentials', host: str, database: str, user: str, password: str, port: int = 5432) -> None:
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port


class ConnectionError(Exception):
    """Exception raised when connection to database fails."""

    pass


def create_connection(postgres_credentials: PostgresCredentials) -> psycopg2.connect:
    """Create a connection to the database.

    Args:
        postgres_credentials (PostgresCredentials): The Postgres credentials class to use to access credentials.

    Raises:
        ConnectionError: If the connection fails.

    Returns:
        psycopg2.connection: The connection to the database.
    """
    if not postgres_credentials:
        raise ConnectionError('Credentials must be provided.')
    try:
        return _get_connection(postgres_credentials)
    except (Exception, psycopg2.DatabaseError) as error:
        raise ConnectionError(error) from error


def _get_connection(postgres_credentials):
    host = postgres_credentials.host
    database = postgres_credentials.database
    user = postgres_credentials.user
    password = postgres_credentials.password
    port = postgres_credentials.port

    return psycopg2.connect(host=host, database=database, user=user, password=password, port=port)


def query_database(
    connection: psycopg2.connect, query: str, params: tuple | None = None, close_connection: bool = True
) -> list:
    """Execute a query on the database.

    Args:
        connection (psycopg2.connection): The connection to the database.
        query (str): The query to execute.
        params (tuple, optional): The parameters of the query. Defaults to None.
        close_connection (bool, optional): If the connection should be closed after the query. Defaults to True.

    Returns:
        list: The result of the query.
    """
    if not connection:
        raise ConnectionError("No connection to database.")

    results = pd.read_sql(query, connection, params).replace(float("nan"), None).to_dict(orient="records")

    if close_connection:
        connection.close()

    return results

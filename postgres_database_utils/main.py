import warnings

import pandas as pd
import psycopg2

warnings.ignorewarnings("ignore")


class ConnectionError(Exception):
    """Exception raised when connection to database fails."""

    pass


def create_connection(host: str, database: str, user: str, password: str, port: int = 5432) -> psycopg2.connection:
    """Create a connection to the database.

    Args:
        host (str): The host of the database.
        database (str): The name of the database.
        user (str): The user to connect to the database.
        password (str): The password of the user.
        port (int, optional): The port of the database. Defaults to 5432.

    Raises:
        ConnectionError: If the connection fails.

    Returns:
        psycopg2.connection: The connection to the database.
    """
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port,
        )
        return connection
    except (Exception, psycopg2.DatabaseError) as error:
        raise ConnectionError(error) from error


def query_database(
    connection: psycopg2.connection, query: str, params: tuple | None = None, close_connection: bool = True
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

    results = pd.read_sql(query, connection, params).replace({float("nan"): None}).to_dict(orient="records")

    if close_connection:
        connection.close()

    return results

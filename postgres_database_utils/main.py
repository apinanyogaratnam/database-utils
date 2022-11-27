import psycopg2


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
        raise ConnectionError(error)

import pytest
from getdoctor.app import create_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app()

    # create the database and load test data
    #with app.app_context():
    #    init_db()
    #    get_db().executescript(_data_sql)

    yield app

    # close and remove the temporary database
    #os.close(db_fd)
    #os.unlink(db_path)

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()





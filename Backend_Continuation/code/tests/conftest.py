import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import db
import models
from main import app



TEST_DATABASE_URL = db.DB_URL.rsplit("/", 1)[0] + "/library_test"
  
test_engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    bind=test_engine,
    autocommit=False,
    autoflush=False,
)


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    db.Base.metadata.drop_all(bind=test_engine)
    db.Base.metadata.create_all(bind=test_engine)
    yield
    db.Base.metadata.drop_all(bind=test_engine)
    test_engine.dispose()


@pytest.fixture
def client(setup_test_database):
    def override_get_db():
        session = TestingSessionLocal()
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[db.get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()

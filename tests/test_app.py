import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)

    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_app_uses_writable_storage():
    app = create_app()
    assert app.instance_path
    assert app.instance_path
    assert app.instance_path.endswith("cybershield-ai") or app.instance_path.endswith("cybershield-ai")


def test_scan_page_renders(client):
    response = client.post(
        "/scan",
        data={"url": "https://example.com"},
        follow_redirects=True,
    )
    assert response.status_code == 200

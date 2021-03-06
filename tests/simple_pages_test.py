"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/page1">Git</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data
    assert b'<a class="nav-link" href="/page5">OOP & Testing</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"About ME" in response.data

def test_request_about(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"My name is Austin. Welcome to my Bootstrap Site!" in response.data

def test_request_page1(client):
    """This makes the Git page 1"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"GIT - WHAT IS IT?" in response.data

def test_request_page2(client):
    """This makes the Docker page 2"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"THE DOCKER PLATFORM" in response.data

def test_request_page3(client):
    """This makes the Python/Flask page 3"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"PYTHON / FLASK" in response.data

def test_request_page4(client):
    """This makes the CI/CD page 4"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"CONTINUOUS INTEGRATION & DELIVERY" in response.data

def test_request_page5(client):
    """This makes the OOP & Testing page 5"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"PROJECT 2 CONTENT AND EXAMPLES" in response.data

def test_request_page_not_found(client):
    """This makes the error page"""
    response = client.get("/page6")
    assert response.status_code == 404

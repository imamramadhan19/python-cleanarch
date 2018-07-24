import os, sys
testfolder = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(testfolder,"../../../../"))
sys.path.append(project_root)

from manage import app

def test_index_returns_200():
    request, response = app.test_client.get('/v1/posts')
    assert response.status == 200
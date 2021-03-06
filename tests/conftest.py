
import pytest
import bottle

from cork import Cork

@pytest.fixture
def mytmpdir(tmpdir):
    """Setup tmp directory with test files
    """
    tmpdir.mkdir('views')
    tmpdir.join('users.json').write("""{"admin": {"email_addr": null, "desc": null, "role": "admin", "hash": "69f75f38ac3bfd6ac813794f3d8c47acc867adb10b806e8979316ddbf6113999b6052efe4ba95c0fa9f6a568bddf60e8e5572d9254dbf3d533085e9153265623", "creation_date": "2012-04-09 14:22:27.075596"}}""")
    tmpdir.join('roles.json').write("""{"special": 200, "admin": 100, "user": 50}""")
    tmpdir.join('register.json').write("""{}""")
    tmpdir.join('registration_email.tpl').write("""Username:{{username}} Email:{{email_addr}} Code:{{registration_code}}""")
    tmpdir.join('password_reset_email.tpl').write("""Username:{{username}} Email:{{email_addr}} Code:{{reset_code}}""")
    return tmpdir

@pytest.fixture
def aaa(mytmpdir):
    aaa = Cork(mytmpdir, smtp_server='localhost', email_sender='test@localhost')
    return aaa




#        mb = self.setup_test_db()
#        self.aaa = MockedUnauthenticatedCork(backend=mb,
#            smtp_server='localhost', email_sender='test@localhost')
#        cookie_name = None
#        if hasattr(self, 'purge_test_db'):
#            self.purge_test_db()
#
#        del(self.aaa)
#        cookie_name = None



def assert_is_redirect(e, path):
    """Check if an HTTPResponse is a redirect.

    :param path: relative path without leading slash.
    :type path: str
    """
    assert isinstance(e, bottle.HTTPResponse), "Incorrect exception type passed to assert_is_redirect"
    assert e.status_code == 302, "HTTPResponse status should be 302 but is '%s'" % e.status
    redir_location = e.headers['Location'].rsplit('/', 1)[1]
    assert redir_location == path, "Redirected to %s instead of %s" % (redir_location, path)

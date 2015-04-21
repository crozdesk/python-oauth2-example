"""
  Crozdesk OAuth2 integration example.
"""
import json
import webapp2
import httplib2
from oauth2client.client import OAuth2WebServerFlow

CLIENT_ID = "API_KEY"
CLIENT_SECRET = "API_SECRET"

PORT = 3000
CALLBACK_URL = "http://localhost:%d/users/auth/crozdesk/callback" % PORT
REMOTE_URL = "https://crozdesk.com"
REMOTE_USER_DETAILS = "%s/api/v1/users/me" % REMOTE_URL

"""
  WebApp2 home page
"""
class MainPage(webapp2.RequestHandler):
    """
        GET /
    """
    def get(self):
        flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                                   client_secret=CLIENT_SECRET,
                                   scope='public',
                                   redirect_uri=CALLBACK_URL,
                                   token_uri='%s/oauth/token' % REMOTE_URL,
                                   auth_uri='%s/oauth/authorize' % REMOTE_URL,
                                   revoke_uri='%s/oauth/revoke' % REMOTE_URL)
        code = self.request.get("code")
        if not code:
            auth_uri = flow.step1_get_authorize_url()
            self.response.write("""\
<html>
<title>Crozdesk Python Example</title>
<body>
<a href="%s">Click here to login with Crozdesk.</a>
</body>
</html>""" % auth_uri)
        else:
            credentials = flow.step2_exchange(code)
            http = httplib2.Http()
            http = credentials.authorize(http)
            response, content = http.request(REMOTE_USER_DETAILS, "GET")
            oauth_data = json.loads(content)
            self.response.write(oauth_data)

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/users/auth/crozdesk/callback', MainPage)
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(application, host='127.0.0.1', port=PORT)

if __name__ == '__main__':
    main()

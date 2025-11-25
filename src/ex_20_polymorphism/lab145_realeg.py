class browser:
    def make_http_request(self,url):
        print("making http request without auth:",url)
    def make_http_request(self,url,auth=None):
        print("making http request with auth",url,auth)
test=browser()
test.make_http_request("http://www.python.org")
test.make_http_request("http://www.python.org","admin")
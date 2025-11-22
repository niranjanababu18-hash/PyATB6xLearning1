class baseclass:
    def __init__(self):
        self._token="ABC123SECRET"
    def _gettoken(self):
        return self._token
class UserAPI(baseclass):
    def get_user_data(self):
        print(f"fetching user data with token {self._token}")
test=UserAPI()
test.get_user_data()
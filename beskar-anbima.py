import requests
import json
import base64


class AnbimaConnect:
    """
    Generates the API key from ANBIMA Feeds, using the clientId:clientSecred encoded
    in base 64 to use in the sandbox
    """

    AUT_ASCII = "O4gotNUBB6MC:Ul5aXNLa3Q4G"
    URL = "https://api.anbima.com.br/oauth/access-token"

    def __init__(self):
        self.message_bytes = AnbimaConnect.AUT_ASCII.encode('ascii')
        self.message_64 = base64.b64encode(self.message_bytes).decode('ascii')
        self.header_aut = {
            "Content-type": "application/json",
            "Authorization": f"Basic {self.message_64}"
        }
        self.data_aut = {
            "grant_type": "client_credentials"
        }

    def request_key(self):
        """
        Crestes a post request to the ANBIMA REST API
        :return: ANBIMA access_token, token_type, expires_in
        """
        aut = requests.post(url=AnbimaConnect.URL,
                            headers=self.header_aut,
                            data=json.dumps(self.data_aut),
                            allow_redirects=True)
        return aut.content


class AnbimaFeed:

    ACCESS_TOKEN = "GkivA66rn8pH"
    TOKEN_TYPE = "access_token"


if __name__ == '__main__':



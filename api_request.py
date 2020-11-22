import requests
import pprint
import json
import wsf_config


class ApiRequest(object):
    """
    Managing all the Api requests and returning the response with json/text file along with http status code.
    """

    HEADERS_TEMPLATE = {'Content-Type': 'application/json'}

    def __init__(self):

        self.logger = wsf_config.logger
        self.base_url = wsf_config.url
        self.set_default_header()

    def set_default_header(self):
        """
        Set default header template as application/json format
        """
        self.headers = self.HEADERS_TEMPLATE.copy()

    def set_header(self, key, value):
        """
        Parameters:
                key:  Key to add to the self.headers dictionary
                value:  Value to set in the self.headers dictionary
        """
        self.headers[key] = value

    def remove_header(self, key):
        del self.headers[key]

    def clear_headers(self):
        """Set self.headers to an empty dictionary"""
        self.headers = {}

    def get_json_or_text(self, response):
        """
        Converting the response to Json format, If the response is in String format then returning the same.
        :parameter:
            response: the http/https response
        """
        try:
            return json.loads(response.text)
        except ValueError as e:
            if str(e) == 'No JSON object could be decoded':
                return response.text
            else:
                raise

    def get(self, endpoint, api_headers=None):
        """
        Parameters:
                endpoint:  the endpoint string normally will contain a beginning '/' character.
                api_headers:  optional headers dictionary, defaults to None
        Returns (status, response text) tuple
        """

        return self.request('GET', endpoint, api_headers)

    def post(self, endpoint, payload, api_headers=None, type=None, files=None, allow_redirects=True):
        """
        Parameters:
                endpoint:  the endpoint string normally will contain a beginning '/' character.
                payload:  typically JSON
                api_headers:  optional headers dictionary, defaults to None
                files:  optional files parameter for for multipart encoding upload
                        e.g) 'name': file-like-objects (or {'name': ('filename', fileobj)})
        Returns (status, response text) tuple
        """

        return self.request('POST', endpoint, payload, api_headers, type, files)

    def request(self, rest_action, endpoint, payload="", type=None, api_headers=None, files=None):
        """
        Parameters:
                rest_action: 'GET', 'POST'
                        endpoint:  the endpoint string normally will contain a beginning '/' character.
                        payload:  typically JSON
                        api_headers:  optional headers dictionary, defaults to None
                        files:  optional files parameter for for multipart encoding upload
                            e.g) 'name': file-like-objects (or {'name': ('filename', fileobj)})
                Returns (status, response text) tuple
        """

        response = self.http_request(rest_action, endpoint, payload, api_headers, files)

        # Handle ValueError for non JSON data returned
        return response.status_code, self.get_json_or_text(response)

    def http_request(self, rest_action, endpoint, payload="", api_headers=None, files=None):
        """
        Parameters:
                rest_action: 'GET', 'POST'
                        endpoint:  the endpoint string normally will contain a beginning '/' character.
                        payload:  typically JSON
                        api_headers:  optional headers dictionary, defaults to None
                        files:  optional files parameter for for multipart encoding upload
                            e.g) 'name': file-like-objects (or {'name': ('filename', fileobj)})
                Returns (status, response text) tuple
        """

        if api_headers is None:
            api_headers = self.headers

        url = self.base_url + endpoint

        # Log requests
        self.logger.info("URL is " + url)
        self.logger.info("Headers are:")
        self.logger.info(pprint.pformat(api_headers))
        self.logger.info("Payload is " + str(payload))

        if rest_action == 'GET':
            response = requests.get(url, headers=api_headers)
        elif rest_action == 'POST':
            if files:
                response = requests.post(
                    url, data=payload, headers=api_headers, files=files)
            else:
                response = requests.post(
                    url, data=payload, headers=api_headers)

        # Log responses
        self.logger.info("Status is " + str(response.status_code))
        self.logger.info("Response Headers are:")
        self.logger.info(response.headers)
        self.logger.info("Response body is: ")
        self.logger.info(pprint.pformat(response.text))

        return response

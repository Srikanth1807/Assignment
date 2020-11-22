from framework_test_case import FrameworkTestCase
from api_request import ApiRequest


class StocktimeSeriesTestCase(FrameworkTestCase):
    """
    Parent class for all the Stock Time Series Api Requests.
    """

    def __init__(self):
        """
        Initializes
            self.api - object with which to call Stocktime Series service endpoints
        """
        super(StocktimeSeriesTestCase, self).__init__()
        self.api = ApiRequest()
        self.logger.info("End of StocktimeSeriesTestCase__init__() ")

    def setup(self):
        super(StocktimeSeriesTestCase, self).setup()
        
    def teardown(self):
        super(StocktimeSeriesTestCase, self).teardown()

    def stocktime_get(self, endpoint):
        """
        stocktime_get will perform a GET to an stocktime series endpoint
        the endpoint string normally will contain a beginning '/' character.
        """

        return self.api.request('GET', endpoint)

    def stocktime_post(self, endpoint, payload):
        """
        stocktime_post will perform a POST to a stocktime series endpoint with a payload.
        The endpoint string normally will contain a beginning '/' character.
        The payload object will typically, depending on the endpoint, be a JSON object
        """

        return self.api.request('POST', endpoint, payload)

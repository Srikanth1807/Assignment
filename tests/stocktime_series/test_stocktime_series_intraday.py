from unittest import TestCase
from .stocktime_series_test_case import StocktimeSeriesTestCase
from api_request import ApiRequest
import pytest


class TestStockTimeSeriesIntraday(TestCase):
    """
    Verification of StockTimeSeries for TIME_SERIES_INTRADAY  api with Valid ans Invalid test cases.
    """

    st = StocktimeSeriesTestCase()
    stock = st.stocktime_series
    intraday = stock.get("Intraday")
    func = intraday.get("function")
    symbol = intraday.get("symbol")
    interval = intraday.get("interval")
    apikey = intraday.get("apikey")

    def test_valid_stockime_series_intraday(self):
        """
        Verifying the StocktimeSeries with valid request parameters and verifying the response according to given
        parameters.
        :return:
        """

        endpoint = "function={0}&symbol={1}&interval={2}&apikey={3}".format(self.func, self.symbol, self.interval,
                                                                            self.apikey)

        (status, response) = self.st.stocktime_get(endpoint=endpoint)
        print("Http Response for endpoint: " + endpoint)
        print(response)

        self.st.logger.info("Expected 200 OK status but actually found" + str(status))
        assert status == 200, "Expected 200 OK status but actually found" + str(status)

        self.st.logger.info("Expected symbol value: " + self.symbol + " But Actually found " +
                            response.get("Meta Data").get("2. Symbol"))
        assert response.get("Meta Data").get("2. Symbol") == self.symbol, \
            "Expected symbol value: " + self.symbol + " But Actually found " + response.get("Meta Data").get(
                "2. Symbol")

        self.st.logger.info("Expected interval value: " + self.interval + "But Actually found: " +
                            response.get("Meta Data").get("4. Interval"))
        assert response.get("Meta Data").get("4. Interval") == self.interval, \
            "Expected interval value: " + self.interval + "But Actually found: " + response.get("Meta Data").get(
                "4. Interval")

        self.st.logger.info("Test Passed")

    def test_stocktime_series_intraday_with_invalid_function(self):
        """
        Verifying the StocktimeSeries with an invalid value for function parameter.
        :return:
        """

        endpoint = "function={0}&symbol={1}&interval={2}&apikey={3}".format("INVALID", self.symbol, self.interval,
                                                                            self.apikey)

        (status, response) = self.st.stocktime_get(endpoint=endpoint)
        print("Http Response for endpoint: " + endpoint)
        print(response)

        self.st.logger.info("Expected 200 OK status but actually found" + str(status))
        assert status == 200, "Expected 200 OK status but actually found" + str(status)

        self.st.logger.info("Expected Error Message in response But found:  " + str(response))
        assert response.get("Error Message") == "This API function (INVALID) does not exist.", \
            "Expected Error Message in response But found:  " + str(response)

    def test_stocktime_series_intraday_with_invalid_symbol(self):
        """
        Verifying the StocktimeSeries with an invalid value for symbol parameter.
        :return:
        """

        endpoint = "function={0}&symbol={1}&interval={2}&apikey={3}".format(self.func, "INVALID", self.interval,
                                                                            self.apikey)

        (status, response) = self.st.stocktime_get(endpoint=endpoint)
        print("Http Response for endpoint: " +endpoint)
        print(response)

        self.st.logger.info("Expected 200 OK status but actually found" + str(status))
        assert status == 200, "Expected 200 OK status but actually found" + str(status)

        self.st.logger.info("Expected Error Message in response But found:  " + str(response))
        assert response.get("Error Message") == "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_INTRADAY.", \
            "Expected Error Message in response But found:  " + str(response)

    def test_stocktime_series_intraday_with_invalid_interval(self):
        """
        Verifying the StocktimeSeries with an invalid value for interval parameter.
        :return:
        """

        endpoint = "function={0}&symbol={1}&interval={2}&apikey={3}".format(self.func, self.symbol, "INVALID",
                                                                            self.apikey)

        (status, response) = self.st.stocktime_get(endpoint=endpoint)
        print("Http Response for endpoint: " + endpoint)
        print(response)

        self.st.logger.info("Expected 200 OK status but actually found" + str(status))
        assert status == 200, "Expected 200 OK status but actually found" + str(status)

        self.st.logger.info("Expected Error Message in response But found:  " + str(response))
        assert response.get("Error Message") == "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_INTRADAY.", \
            "Expected Error Message in response But found:  " + str(response)

    def test_stocktime_series_intraday_with_invalid_apikey(self):
        """
        Verifying the StocktimeSeries with an invalid value for apikey parameter.
        :return:
        """

        endpoint = "function={0}&symbol={1}&interval={2}&apikey={3}".format(self.func, self.symbol, self.interval,
                                                                            "INVALID")

        (status, response) = self.st.stocktime_get(endpoint=endpoint)
        print("Http Response for endpoint: " + endpoint)
        print(response)

        self.st.logger.info("Expected Error Message in response But found:  " + str(response))
        assert response.get("Error Message") == "This API Key (INVALID) does not exist.", \
            "Expected Error Message in response But found:  " + str(response)


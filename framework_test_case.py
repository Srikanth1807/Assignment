import wsf_config

class FrameworkTestCase(object):
    """
    This is used to provide the config data or test data to the multiple services/api(if presented)
    """

    def __init__(self):
        """
        Initializing global variables for config and test data.
        """
        self.logger = wsf_config.logger
        self.stocktime_series = wsf_config.stock_time_series
        self.logger.info("Frame")

    def setup(self):
        """
        For the Connections and Maintenance of DB objects.
        :return:
        """
        self.logger.info("Framework setup Called")

    def teardown(self):
        """
        Cleaning up the variables or objects
        :return:
        """
        self.logger.info("Framework teardown Called")

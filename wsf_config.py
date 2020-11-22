import json
import logging
import os

"""
This file is used for Reading the data from Config file and Test Data(if presented)
"""
logging_level = logging.INFO

try:
    # print(os.path.dirname(os.path.abspath(__file__)))
    # config_path = os.getcwd() + "\config\config.json"
    config_path = os.path.dirname(os.path.abspath(__file__)) + '/config/config.json'
    # print(config_path)
    fp = open(config_path, 'r')
    data = json.loads(fp.read())
    # print(data)
    url = data.get("base_url")
    stock_time_series = data.get("StockTimeSeries")

except IOError:
    print("Unable to find Config File")

logging.basicConfig(filename="logger.log",  level=logging_level)
logger = logging.getLogger(__name__)

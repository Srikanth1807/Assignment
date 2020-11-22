Title: Assignement on Alpha Vantage API Documenttation

Prerequisites:
	Download Python-3.xx : Download the latest from https://www.python.org/downloads/ 
	Download PyCharm IDE(Optional): Download the PyCharm from https://www.jetbrains.com/pycharm/download/
	Download pip installer script(optional)

Installation:
	1. Run Python excutable(.exe) file clcik on install.
	2. Add Python installed location to System Environment varaibles.
	3. Add "Python insstallled location\Scripts" location to System Environment varaibles.
	4. Add"Python insstallled location\site-packages" location to System Environment varaibles.
	5. Open Command Prompt and type Python to verify the Installation.

	sample  display on Command Prompt for successfull installation: 
	Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>>

	6. Install PyCharm and set python Interpreter.

Run the Tests:
Add/Install all the required Python Modules given in requirements.txt file

To run the tests follow the below steps:
1. Open terminal/command prompt.
2. Navigate to the project folder(Assignement)
3. Enter below cmd
	pytest pytest tests\stocktime_series\test_stocktime_series_intraday.py --html=output.html
4. After execution of above command, it will generate the TestReport as output.html file in the root level of project. 

config - directory is for mantaining test data files, config files or any type of input files required for the tests.

tests - package contains the testcases for multiple modules/services. here we had only one implemented i.e, subpackage stocktime_series and this stocktime_series will contains all the test scripts related to the Stock Time Series test cases.

util - package is to handle DB conncetions or to implement our own assertions(For this project we didnot used our own assertions)

assets - directory is generated when we excute the script with html report - supporting directory to html file.
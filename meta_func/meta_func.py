from functools import wraps
from time import time, sleep
import warnings
import sys # for verbose exception information
from inspect import getargspec

def stringified_warnings(warn_list):
	return [str(w) for w in warn_list]

def meta_func(ignore_errors=False):
	_LogInfoDict = dict()
	def decorating_function(user_function):
		@wraps(user_function)
		def wrapper(*args,**kwargs):
			_LogInfoDict['argspec'] = getargspec(user_function)
			_LogInfoDict['args'] = args if args else None
			_LogInfoDict['kwargs'] = kwargs if kwargs else None
			_LogInfoDict['error_info'] = None
			_LogInfoDict['func_name'] = user_function.__name__
			with warnings.catch_warnings(record=True) as w:
				_LogInfoDict['time_started'] = time()
				warnings.simplefilter("always")
				try:
					_LogInfoDict['return_value'] = user_function(*args,**kwargs)
				except:
					_LogInfoDict['error_info'] = sys.exc_info()
					_LogInfoDict['return_value'] = None
				_LogInfoDict['time_ended'] = time()
				_LogInfoDict['time_elapsed'] = round(_LogInfoDict['time_ended'] - _LogInfoDict['time_started'],6) # millionths of sec
				_LogInfoDict['warnings'] = stringified_warnings(w) if w else None
				if ignore_errors is False and _LogInfoDict['error_info']:
					raise _LogInfoDict['error_info'][0]
			return _LogInfoDict['return_value']

		def log_info():
			return _LogInfoDict

		wrapper.__wrapped__ = user_function
		wrapper.log_info = log_info
		return wrapper
	return decorating_function
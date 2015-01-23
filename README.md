# Metadata for Functions
Python decorator function to track metadata on function calls

# Example
```python
@meta_func(ignore_errors=True)
    def self_mult(n):
        sleep(0.2)
        return n*n

    print(self_mult(10)) # => 100
    print(self_mult.log_info()) # => {'time_started': 1422042033.971449, 'warnings': None, 'args': (10,), 'error_info': None, 'time_ended': 1422042034.171857, 'time_elapsed': 0.200408, 'return_value': 100, 'kwargs': None}

    print(self_mult(15)) # => 225
    print(self_mult.log_info()) # => {'time_started': 1422042034.172171, 'warnings': None, 'args': (15,), 'error_info': None, 'time_ended': 1422042034.373299, 'time_elapsed': 0.201128, 'return_value': 225, 'kwargs': None}

    print(self_mult("foo")) # => None
    print(self_mult.log_info()) # => {'time_started': 1422042034.373651, 'warnings': None, 'args': ('foo',), 'error_info': (<type 'exceptions.TypeError'>, TypeError("can't multiply sequence by non-int of type 'str'",), <traceback object at 0x10fcea098>), 'time_ended': 1422042034.574758, 'time_elapsed': 0.201107, 'return_value': None, 'kwargs': None}
```

# Usage
Decorate a function with `@meta_func()` passing the optional keyword argument ignore_errors = True/False. ignore_errors tells `@meta_func` whether or not to raise any exception your decorated function raises or to solely log to the error_info attribute.

# Compatibility
Tested compatible with Py2.7 and Py3, but this code is provided as is with no warranty or guarantee, implied or explicit.

# More Information
Please see my blog post here: http://garrens.com/blog/2015/01/23/metadata-for-functions-python-decorator/
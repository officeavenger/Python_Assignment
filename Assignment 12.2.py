def suppress_exception(*args, exception_type, default_result, **kwargs):
    def exception_handler(func):
        def inner_function(*func_args, **func_kwargs):
            print(func_args, func_kwargs)
            try:
                result = func(*func_args, **func_kwargs)
                return result
            except exception_type:
                return default_result
            except Exception as ex:
                raise ex
        return inner_function
    return exception_handler

@suppress_exception(exception_type=KeyError, default_result=False)
def login(user, password):
    print(f'Logging in as {user}')
    return users.get(user) == password

users = {'a': 123, 'b': 1234}
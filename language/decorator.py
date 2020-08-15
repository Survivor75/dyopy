from functools import wraps
import time


def my_logger(orig_func):
    from language import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Tom', 22)


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Executed Before', original_function.__name__)
        result = original_function(*args, **kwargs)
        print('Executed After', original_function.__name__, '\n')
        return result
    return wrapper_function


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decorator_function


@prefix_decorator('LOG:')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)
display_info('Travis', 30)


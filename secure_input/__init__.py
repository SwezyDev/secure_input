from .secure_input import secure_input

def __call__(*args, **kwargs):
    return secure_input(*args, **kwargs)

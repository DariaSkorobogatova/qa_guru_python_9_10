import os
import tests


def to_avatar(file_name):
    return str(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), f'../resources/{file_name}')
        )
    )
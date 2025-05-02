# -*- coding: utf-8 -*-
__author__ = 'Ragu.Sekaran'
import os

from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

from utils.yml_data import YMLData


def config(filename=None):
    filename = filename or os.path.join(
        os.path.dirname(__file__),
        'config_test.yaml'
    )

    if os.path.exists(filename):
        return YMLData.load(filename)
    else:
        raise EnvironmentError(
            'Unable to locate the configuration file'
        )


def environment_password(
        token=config().ui.rewards.test_user.test_user_approver.Password
):
    return decrypt_password(token)


def decrypt_password(token):
    try:
        with open(
                os.path.join(
                    os.path.dirname(__file__),
                    '.key'
                ), 'r'
        ) as key:
            cipher_key = ''.join(
                line.strip()
                for line in key.readlines()
            )

        if cipher_key.startswith("b'"):
            cipher_key = cipher_key.strip('b').strip("'")

        plain_text = Fernet(
            cipher_key.encode()
        ).decrypt(
            token.encode()
        ).decode()
    except InvalidToken:
        plain_text = token
    except Exception:
        raise

    return plain_text

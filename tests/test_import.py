# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from smoke import *  # noqa
from smokebase import *  # noqa


# pylint: disable=unused-import,unused-variable
def test_import():
    _ = Steem()
    _ = account.PasswordKey

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.log_exception()."""


import pytest

from anglerfish import log_exception


def test_log_exception():
    pass # FIXME: pytest.raises() dont like try:...except:... ?
    #  with pytest.raises(ZeroDivisionError):
    #     try:
    #         0 / 0
    #     except Exception:
    #         log_exception()

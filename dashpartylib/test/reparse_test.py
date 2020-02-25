#! /usr/bin/python3
import tempfile
import pytest

from dashpartylib.test import conftest  # this is require near the top to do setup of the test suite
from dashpartylib.test import util_test
from dashpartylib.test.util_test import CURR_DIR
from dashpartylib import server
from dashpartylib.lib import (config, check, database)


def test_book(testnet):
    """Reparse all the transactions in the database to see check blockhain's integrity."""
    conftest.DISABLE_ALL_MOCK_PROTOCOL_CHANGES_AT_BLOCK = True
    util_test.reparse(testnet=testnet)

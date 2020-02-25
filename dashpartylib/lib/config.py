import sys

"""Variables prefixed with `DEFAULT` should be able to be overridden by
configuration file and command‐line arguments."""

UNIT = 100000000        # The same across assets.


# Versions
VERSION_MAJOR = 9
VERSION_MINOR = 58
VERSION_REVISION = 0
VERSION_STRING = str(VERSION_MAJOR) + '.' + str(VERSION_MINOR) + '.' + str(VERSION_REVISION)


# Counterparty protocol
TXTYPE_FORMAT = '>I'
SHORT_TXTYPE_FORMAT = 'B'

TWO_WEEKS = 2 * 7 * 24 * 3600
MAX_EXPIRATION = 4 * 2016   # Two months

MEMPOOL_BLOCK_HASH = 'mempool'
MEMPOOL_BLOCK_INDEX = 9999999


# SQLite3
MAX_INT = 2**63 - 1


# Bitcoin Core
OP_RETURN_MAX_SIZE = 80  # bytes


# Currency agnosticism
BTC = 'DSH'
XCP = 'DSP'

BTC_NAME = 'Dash'
XCP_NAME = 'Dashparty'
APP_NAME = XCP_NAME.lower()

DEFAULT_RPC_PORT_REGTEST = 24900
DEFAULT_RPC_PORT_TESTNET = 14900
DEFAULT_RPC_PORT = 4900

DEFAULT_BACKEND_PORT_REGTEST = 29332
DEFAULT_BACKEND_PORT_TESTNET = 19332
DEFAULT_BACKEND_PORT = 9332

DEFAULT_INDEXD_PORT_REGTEST = 29432
DEFAULT_INDEXD_PORT_TESTNET = 19432
DEFAULT_INDEXD_PORT = 9432

UNSPENDABLE_REGTEST = 'yvDashpartyxxxxxxxxxxxxxxxxxzQLvSm'
UNSPENDABLE_TESTNET = 'yvDashpartyxxxxxxxxxxxxxxxxxzQLvSm'
UNSPENDABLE_MAINNET = 'XmDashpartyxxxxxxxxxxxxxxxxy1ZmXZH'

ADDRESSVERSION_TESTNET = b'\x8c'
P2SH_ADDRESSVERSION_TESTNET = b'\x13'
PRIVATEKEY_VERSION_TESTNET = b'\xef'
ADDRESSVERSION_MAINNET = b'\x4c'
P2SH_ADDRESSVERSION_MAINNET = b'\x10'
PRIVATEKEY_VERSION_MAINNET = b'\x80'
ADDRESSVERSION_REGTEST = b'\x8c'
P2SH_ADDRESSVERSION_REGTEST = b'\x13'
PRIVATEKEY_VERSION_REGTEST = b'\xef'
MAGIC_BYTES_TESTNET = b'\xce\xe2\xca\xff'
MAGIC_BYTES_MAINNET = b'\xbf\x0c\x6b\xbd'
MAGIC_BYTES_REGTEST = b'\xe2\xca\xff\xce'

BLOCK_FIRST_TESTNET_TESTCOIN = 0
BURN_START_TESTNET_TESTCOIN = 0
BURN_END_TESTNET_TESTCOIN = 0     # Fifty years, at ten minutes per block.

BLOCK_FIRST_TESTNET = 261473
BLOCK_FIRST_TESTNET_HASH = '0000036507a876e1670e72a480187e3e795b8b0120d634349f454ae3a5befe79'
BURN_START_TESTNET = 261473
BURN_END_TESTNET = 5000000              # Fifty years, at ten minutes per block.

BLOCK_FIRST_MAINNET_TESTCOIN = 278270
BURN_START_MAINNET_TESTCOIN = 278310
BURN_END_MAINNET_TESTCOIN = 2500000     # A long time.

BLOCK_FIRST_MAINNET = 1217265
BLOCK_FIRST_MAINNET_HASH = '00000000000000065776638efd9436a73a158c5b35fc9fe645def9b9065cd437'
BURN_START_MAINNET = 1217265
BURN_END_MAINNET = 1000000000

BLOCK_FIRST_REGTEST = 0
BLOCK_FIRST_REGTEST_HASH = '000008ca1832a4baf228eb1553c03d3a2c8e02399550dd6ea8d65cec3ef23d2e'
BURN_START_REGTEST = 101
BURN_END_REGTEST = 150000000

BLOCK_FIRST_REGTEST_TESTCOIN = 0
BURN_START_REGTEST_TESTCOIN = 101
BURN_END_REGTEST_TESTCOIN = 150

# Protocol defaults
# NOTE: If the DUST_SIZE constants are changed, they MUST also be changed in counterblockd/lib/config.py as well
    # TODO: This should be updated, given their new configurability.
# TODO: The dust values should be lowered by 90%, once transactions with smaller outputs start confirming faster: <https://github.com/mastercoin-MSC/spec/issues/192>
DEFAULT_REGULAR_DUST_SIZE = 5430         # TODO: This is just a guess. I got it down to 5530 satoshis.
DEFAULT_MULTISIG_DUST_SIZE = 7800        # <https://bitcointalk.org/index.php?topic=528023.msg7469941#msg7469941>
DEFAULT_OP_RETURN_VALUE = 0
DEFAULT_FEE_PER_KB_ESTIMATE_SMART = 1024
DEFAULT_FEE_PER_KB = 25000               # sane/low default, also used as minimum when estimated fee is used
ESTIMATE_FEE_PER_KB = True               # when True will use `estimatesmartfee` from bitcoind instead of DEFAULT_FEE_PER_KB
ESTIMATE_FEE_CONF_TARGET = 3
ESTIMATE_FEE_MODE = 'CONSERVATIVE'

# UI defaults
DEFAULT_FEE_FRACTION_REQUIRED = .009   # 0.90%
DEFAULT_FEE_FRACTION_PROVIDED = .01    # 1.00%


DEFAULT_REQUESTS_TIMEOUT = 20   # 20 seconds
DEFAULT_RPC_BATCH_SIZE = 20     # A 1 MB block can hold about 4200 transactions.

# Custom exit codes
EXITCODE_UPDATE_REQUIRED = 5


DEFAULT_CHECK_ASSET_CONSERVATION = True

BACKEND_RAW_TRANSACTIONS_CACHE_SIZE = 20000
BACKEND_RPC_BATCH_NUM_WORKERS = 6

UNDOLOG_MAX_PAST_BLOCKS = 100 #the number of past blocks that we store undolog history

DEFAULT_UTXO_LOCKS_MAX_ADDRESSES = 1000
DEFAULT_UTXO_LOCKS_MAX_AGE = 3.0 #in seconds

ADDRESS_OPTION_REQUIRE_MEMO = 1
ADDRESS_OPTION_MAX_VALUE = ADDRESS_OPTION_REQUIRE_MEMO # Or list of all the address options
OLD_STYLE_API = True

API_LIMIT_ROWS = 1000

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

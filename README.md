[![Build Status Travis](https://travis-ci.org/Dashparty/dashparty-lib.svg?branch=develop)](https://travis-ci.org/Dashparty/dashparty-lib)
[![Build Status Circle](https://circleci.com/gh/Dashparty/dashparty-lib.svg?&style=shield)](https://circleci.com/gh/Dashparty/dashparty-lib)
[![Coverage Status](https://coveralls.io/repos/Dashparty/dashparty-lib/badge.png?branch=develop)](https://coveralls.io/r/Dashparty/dashparty-lib?branch=develop)
[![Latest Version](https://pypip.in/version/dashparty-lib/badge.svg)](https://pypi.python.org/pypi/dashparty-lib/)
[![License](https://pypip.in/license/dashparty-lib/badge.svg)](https://pypi.python.org/pypi/dashparty-lib/)
[![Docker Pulls](https://img.shields.io/docker/pulls/counterparty/counterparty-server.svg?maxAge=2592000)](https://hub.docker.com/r/counterparty/counterparty-server/)


# Description
`dashparty-lib` is the reference implementation of the [Counterparty Protocol](https://counterparty.io) in Dash.

**Note:** for the command-line interface to `dashparty-lib`, see [`counterparty-cli`](https://github.com/Dashparty/counterparty-cli).


# Installation

For a simple Docker-based install of the Dashparty software stack, see [this guide](http://counterparty.io/docs/federated_node/).


# Manual installation

Download the latest [Dash Core](https://github.com/bitcoin/bitcoin/releases) and create
a `dash.conf` file with the following options:

```
rpcuser=dashrpc
rpcpassword=rpc
server=1
txindex=1
rpctimeout=300
zmqpubhashblock=tcp://127.0.0.1:28832
zmqpubhashtx=tcp://127.0.0.1:28832
addresstype=legacy
```
**Note:** you can and should replace the RPC credentials. Remember to use the changed RPC credentials throughout this document.

Download and install latest Indexd:
```
$ git clone https://github.com/Dashparty/indexd-server.git
$ cd indexd-server
$ cp .env-mainnet-example .env
 -- Modify .env with your rpcuser and rpcpassword --
$ npm install
$ npm start
```

You could run the indexd daemon with a process manager like `forever` or `pm2` (recommended).

Then, download and install `dashparty-lib`:

```
$ git clone https://github.com/Dashparty/dashparty-lib.git
$ cd dashparty-lib
$ sudo pip3 install --upgrade -r requirements.txt
$ sudo python3 setup.py install
```

Followed by `dashparty-cli`:

```
$ git clone https://github.com/Dashparty/dashparty-cli.git
$ cd dashparty-cli
$ sudo pip3 install --upgrade -r requirements.txt
$ sudo python3 setup.py install
```

Note on **sudo**: both dashparty-lib and dashparty-server can be installed by non-sudoers. Please refer to external documentation for instructions on using pip without root access and other information related to custom install locations.


Then, launch the daemon via:

```
$ dashparty-server bootstrap
$ dashparty-server --backend-password=rpc start
```

# Basic Usage

## Via command-line

(Requires `dashparty-cli` to be installed.)

* The first time you run the server, you may bootstrap the local database with:
	`$ dashparty-server bootstrap`

* Start the server with:
	`$ dashparty-server start`

* Check the status of the server with:
	`$ dashparty-client getinfo`

* For additional command-line arguments and options:
	`$ dashparty-server --help`
	`$ dashparty-client --help`

## Via Python

Bare usage from Python is also possible, without installing `dashparty-cli`:

```
$ python3
>>> from dashpartylib import server
>>> db = server.initialise(<options>)
>>> server.start_all(db)
```

# Configuration and Operation

The paths to the **configuration** files, **log** files and **database** files are printed to the screen when starting the server in ‘verbose’ mode:
	`$ dashparty-server --verbose start`

By default, the **configuration files** are named `server.conf` and `client.conf` and located in the following directories:

* Linux: `~/.config/dashparty/`
* Windows: `%APPDATA%\Dashparty\`

Client and Server log files are named `dashparty.client.[testnet.]log` and `dashparty.server.[testnet.]log`, and located in the following directories:

* Linux: `~/.cache/dashparty/log/`
* Windows: `%APPDATA%\Local\Dashparty\dashparty\Logs`

Counterparty API activity is logged in `server.[testnet.]api.log` and `client.[testnet.]api.log`.

Counterparty database files are by default named `dashparty.[testnet.]db` and located in the following directories:

* Linux: `~/.local/share/dashparty`
* Windows: `%APPDATA%\Roaming\Dashparty\dashparty`

## Configuration File Format

Manual configuration is not necessary for most use cases. "back-end" and "wallet" are used to access Dash server RPC.

A `dashparty-server` configuration file looks like this:

	[Default]
	backend-name = indexd
	backend-user = <user>
	backend-password = <password>
	indexd-connect = localhost
	indexd-port = 9432
	rpc-host = 0.0.0.0
	rpc-user = <rpcuser>
	rpc-password = <rpcpassword>

The ``force`` argument can be used either in the server configuration file or passed at runtime to make the server keep running in the case it loses connectivity with the Internet and falls behind the back-end database. This may be useful for *non-production* Dashparty servers that need to maintain RPC service availability even when the backend or counterparty server has no Internet connectivity.

A `dashparty-client` configuration file looks like this:

	[Default]
	wallet-name = bitcoincore
	wallet-connect = localhost
	wallet-user = <user>
	wallet-password = <password>
	counterparty-rpc-connect = localhost
	counterparty-rpc-user = <rpcuser>
	counterparty-rpc-password = <password>


# Developer notes

## Versioning

* Major version changes require a full (automatic) rebuild of the database.
* Minor version changes require a(n automatic) database reparse.
* All protocol changes are retroactive on testnet.

## Continuous integration
 - TravisCI is setup to run all tests with 1 command and generate a coverage report and let `python-coveralls` parse and upload it.
   It does runs with `--skiptestbook=all` so it will not do the reparsing of the bootstrap files.
 - CircleCI is setup to split the tests as much as possible to make it easier to read the error reports.
   It also runs the `integration_test.test_book` tests, which reparse the bootstrap files.


# Further Reading

* [Official Project Documentation](http://counterparty.io/docs/)

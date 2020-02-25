FROM dashparty/base

MAINTAINER Dashparty Developers <dev@dashparty.io>

# Install dashparty-lib
COPY . /dashparty-lib
WORKDIR /dashparty-lib
RUN pip3 install -r requirements.txt
RUN python3 setup.py develop
RUN python3 setup.py install_apsw

# Install dashparty-cli
# NOTE: By default, check out the dashparty-cli master branch. You can override the BRANCH build arg for a different
# branch (as you should check out the same branch as what you have with dashparty-lib, or a compatible one)
# NOTE2: In the future, dashparty-lib and counterparty-cli will go back to being one repo...
ARG CLI_BRANCH=master
ENV CLI_BRANCH ${CLI_BRANCH}
RUN git clone -b ${CLI_BRANCH} https://github.com/Dashparty/dashparty-cli.git /dashparty-cli
WORKDIR /dashparty-cli
RUN pip3 install -r requirements.txt
RUN python3 setup.py develop

# Additional setup
COPY docker/server.conf /root/.config/dashparty/server.conf
COPY docker/start.sh /usr/local/bin/start.sh
RUN chmod a+x /usr/local/bin/start.sh
WORKDIR /

EXPOSE 4900 14900

# NOTE: Defaults to running on mainnet, specify -e TESTNET=1 to start up on testnet
ENTRYPOINT ["start.sh"]

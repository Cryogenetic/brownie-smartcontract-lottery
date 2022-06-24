from brownie import Lottery, network, config
from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
)
from web3 import Web3
import time

SUBSCRIPTION_ID = 7098


def deploy_lottery():
    account = get_account()
    print(f"The active network is {network.show_active()}")
    price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    subscription_id = SUBSCRIPTION_ID
    lottery = Lottery.deploy(price_feed_address, subscription_id, {"from": account})
    time.sleep(1)
    print(f"Contract deployed to {lottery.address}")


def main():
    deploy_lottery()

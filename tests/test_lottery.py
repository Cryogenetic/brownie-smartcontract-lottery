from brownie import Lottery, accounts, config, network
from web3 import Web3
from scripts.helpful_scripts import get_account


def test_get_entrance_fee():
    account = get_account()
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )

    # ~0.04 eth per $50 usd 6/24/22
    assert lottery.getEntranceFee() > Web3.toWei(0.03, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.05, "ether")


def test_rng():
    account = get_account()
    contractaddress = address(this).address
    random_number = Lottery.requestRandomWords()

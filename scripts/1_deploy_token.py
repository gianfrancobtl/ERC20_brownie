from brownie import ARSTToken
from scripts.helpful_scripts import get_account, network, config
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    ARST_token = ARSTToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(ARST_token.name())

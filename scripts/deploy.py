from brownie import accounts, SimpleStorage

def deploy_simple_storage():
  account = accounts[0]
  # account = accounts.load("stu-account")
  # print(account)
  simple_storage = SimpleStorage.deploy({"from": account})
  stored_value = simple_storage.retrieve()
  print(stored_value)

def main(): 
    deploy_simple_storage() 
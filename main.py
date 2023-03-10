import json
from PolygonScanLib.Accounts import Accounts
from PolygonScanLib.Contracts import Contracts

#------------------------------------------------
def main():
  """
  accounts = Accounts()
  accountAddresses = [
                "0x1ED783A27ef74cfa6FD1c5712241F6C2217A9b79", 
                "0xef46D5fe753c988606E6F703260D816AF53B03EB",
                "0x3f2f4aa023c6ed149d342229afac6e140e149114",   # Contract address
                "0x000D5fe753c988606E600000F703260D816AF000",   # A fake address
                "0x000D503260D816AF000",                        # In invalid address
              ]

  print("Begin-Accounts: Get MATIC Balance for a Single Address.")
  for address in accountAddresses:
    balance = accounts.getBalance(address)
    print(f"[{address}]: {balance}")
  print("End-Accounts: Get MATIC Balance for a Single Address.")
  print()
  
  print("Begin-Accounts: Get MATIC Balance for Multiple Addresses in a Single Call.")
  balances = accounts.getBalances(accountAddresses)
  for address, balance in balances.items():
    print(f"[{address}]: {balance}")
  print("End-Accounts: Get MATIC Balance for Multiple Addresses in a Single Call.")
  print()

  print("Begin-Accounts: Get a list of 'Normal' Transactions By Address.")
  for address in accountAddresses:
    noramlTransactions = accounts.getNormalTransactions(address, startblock=0, endblock=99999999, page=1, offset=5, sort="desc")
    print(f"[{address}]: {noramlTransactions}") 
  print("End-Accounts: Get a list of 'Normal' Transactions By Address.")
  print()

  print("Begin-Accounts: Get a list of 'Internal' Transactions by Address.")
  for address in accountAddresses:
    noramlTransactions = accounts.getInternalTransactions(address, startblock=0, endblock=99999999, page=1, offset=5, sort="desc")
    print(f"[{address}]: {noramlTransactions}")
  
  print("End-Accounts: Get a list of 'Internal' Transactions by Address.")
  print()
  """

  contracts = Contracts()
  contractAddresses = [
                "0x3f2f4aa023c6ed149d342229afac6e140e149114", 
                "0xc2132d05d31c914a87c6611c10748aeb04b58e8f", 
                "0xef46D5fe753c988606E6F703260D816AF53B03EB",   # Account address
                "0x000D5fe753c988606E600000F703260D816AF000",   # A fake address
                "0x000D503260D816AF000",                        # In invalid address
              ]

  """
  print("Begin-Contracts: Get Contract ABI for Verified Contract Source Codes.")
  for address in contractAddresses:
    info = contracts.getABI(address)
    print(f"[{address}]: {info}") 
  print("End-Contracts: Get Contract ABI for Verified Contract Source Codes.")
  print()
  """
  
  print("Begin-Contracts: Get Contract Source Code for Verified Contract Source Codes.")
  for address in contractAddresses:
    info = contracts.getSourceCode(address)
    print(f"[{address}]: {info}") 
  print("End-Contracts: Get Contract Source Code for Verified Contract Source Codes.")
  print()
  

main()
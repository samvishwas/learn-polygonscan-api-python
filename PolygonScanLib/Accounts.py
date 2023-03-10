from PolygonScanLib.Requests import get

#--- https://docs.polygonscan.com/api-endpoints/accounts

class Accounts:
  PARAMS = {
    "module": "account",  
  }

  #--- Get MATIC Balance for a Single Address
  def getBalance(self, address):
      params = self.PARAMS | {
          "action": "balance",
          "address": address
        }
      response = get(params)
      # print(response);
      return int(response['result'])

  #--- Get MATIC Balance for Multiple Addresses in a Single Call
  def getBalances(self, addresses):
      params = self.PARAMS | {
          "action": "balancemulti",
          "tag": "latest",
          "address": ",".join(addresses)
        }    
      response = get(params)
      # print(response);

      balances = {}
      result = response.get('result')
      if result:
          for item in result:
              account = item.get('account')
              balance = int(item.get('balance'))
              balances[account] = balance
      return balances

  #--- Get a list of 'Normal' or 'Internal' Transactions By Address
  def getTransactions(self, address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc", action="txlist"):
      params = self.PARAMS | {
          "action": action,
          "address": address,
          "startblock": startblock,
          "endblock": endblock,
          "page": page,
          "offset": offset,
          "sort": sort
        }    
      response = get(params)
      return response.get('result')
  
  #--- Get a list of 'Normal' Transactions By Address
  def getNormalTransactions(self, address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
      return self.getTransactions(address, startblock, endblock, page, offset, sort, action="txlist")
      
  #--- Get a list of 'Internal' Transactions by Address
  def getInternalTransactions(self, address, startblock=0, endblock=99999999, page=1, offset=10, sort="asc"):
      return self.getTransactions(address, startblock, endblock, page, offset, sort, action="txlistinternal")


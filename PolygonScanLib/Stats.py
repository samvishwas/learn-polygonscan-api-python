from decimal import Decimal
from PolygonScanLib.Requests import get

#--- https://docs.polygonscan.com/api-endpoints/stats-1

class Stats:
  PARAMS = {
    "module": "stats",  
  }

  #--- Get Total Supply of MATIC on the Polygon POS Chain
  def getTotalSupplyOfMATIC(self):
      params = self.PARAMS | {
          "action": "maticsupply"
        }
      response = get(params)
      # print(response);
      return int(response['result'])

  #--- Get MATIC Last Price
  # Valid values for currency parameter:
  # "maticusd" - default value
  # "maticbtc"
  def getMATICLastPrice(self, currency="maticusd"):
      params = self.PARAMS | {
          "action": "maticprice"
        }
      response = get(params)
      # print(response);
      return Decimal(response["result"][currency])
  
  

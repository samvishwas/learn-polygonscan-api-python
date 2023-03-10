from PolygonScanLib.Requests import get

#--- https://docs.polygonscan.com/api-endpoints/contracts

class Contracts:
  PARAMS = {
    "module": "contract",  
  }


  #--- Get Contract ABI or Source Code for Verified Contract Source Codes
  def getInfo(self, address, action="getabi"):
      params = self.PARAMS | {
          "action": action,
          "address": address
        }
      response = get(params)
      # print(response);
      return response['result']
  
  #--- Get Contract ABI for Verified Contract Source Codes
  def getABI(self, address):
      return self.getInfo(address, action="getabi")

  #--- Get Contract Source Code for Verified Contract Source Codes
  def getSourceCode(self, address):
      return self.getInfo(address, action="getsourcecode")

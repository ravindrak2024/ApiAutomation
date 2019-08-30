from .SHAHash import SHAHash

class addSignatureInPushCall(object):

   def __init__(self,function):
       self.function=function

   def __call__(self,url,header,payload):
       print("CALL ClassBasedDecoratorWithParams")
       if 'x-signature' in header.keys():
            method=''
            if 'Post' in self.function.__name__:
                method='POST'
            elif 'Put' in self.function.__name__:
                method='PUT'

            header['x-signature']=SHAHash.getSignatureEvaluatedHeader(method,url,header,payload)
       return self.function(self,url,header,payload)



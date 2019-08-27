import hashlib
import time


class SHAHash:

    @classmethod
    def getSignatureEvaluatedHeader(cls,data):
        push_key=data['x-api-key']
        push_key_secret=data['x-signature']
        timestamp=int(time.time())

        pass







    @staticmethod
    def __GetIntegrity(hash_type,data):
        """Calculate the integirty value of given data using remote peers hash"""
        if hash_type == None:
            return None
        elif hash_type == 0:
            # SHA-1
            return hashlib.sha1(data).digest()
        elif hash_type == 1:
            # SHA-224
            return hashlib.sha224(data).digest()
        elif hash_type == 2:
            # SHA-256
            return hashlib.sha256(data).digest()
        elif hash_type == 3:
            # SHA-384
            return hashlib.sha384(data).digest()
        elif hash_type == 4:
            # SHA-512
            return hashlib.sha512(data).digest()
        else:
            return None

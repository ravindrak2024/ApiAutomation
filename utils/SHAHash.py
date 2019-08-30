import hashlib
import time
import json
import base64
from utils.LogInitilizer import LogInitilizer
logger=LogInitilizer.getLogger()

class SHAHash:

    @classmethod
    def getSignatureEvaluatedHeader(cls,method,url,header,payload):
        push_key=header['x-api-key']
        push_key_secret=header['x-signature']
        timestamp = int(time.time())
        header['x-timestamp']=str(timestamp)

        logger.info("Push key type - {}".format(type(push_key)))
        logger.info("url - {}".format(type(url)))
        logger.info("payload - {}".format(type(push_key)))
        logger.info("Timestamp type - {}".format(type(timestamp)))
        logger.info("Push key secret type - {}".format(type(push_key_secret)))


        signature_text=push_key+'+'+url+'+'+method+'+'+json.dumps(payload)+'+'+str(timestamp)+'+'+push_key_secret

        logger.info("Signature string {} with type {}".format(signature_text,type(signature_text.encode())))
        return SHAHash.__GetIntegrity(4,signature_text.encode())

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
            logger.info("Generating hash 512")
            return hashlib.sha512(data).hexdigest()
        else:
            return None

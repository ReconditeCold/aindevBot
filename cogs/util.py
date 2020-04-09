import base64
class Util():
    def __init__(self):
        

    
    def getainid(timestamp):
        timestr = str(timestamp)
        timelen = len(timestr)
        timeintf = int(timestr)
        finishedres = timeintf*timelen
        return finishedres
    def encodeb64(string):
        message = string
        message_bytes = message.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('utf-8')
        return base64_message
    def decodeb64(str11):
        base64_message2 = str11
        base64_bytes2 = base64_message2.encode('utf-8')
        message_bytes2 = base64.b64decode(base64_bytes2)
        message2 = message_bytes2.decode('utf-8')
        return message2
    
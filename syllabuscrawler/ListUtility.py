import re

class ListUtility:
    def splitter(data):
        #print( re.split('; |, .', data))
        #print(re.split("; | .", data))
        return data.split(".")
 
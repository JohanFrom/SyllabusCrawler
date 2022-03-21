import re

class ListUtility:
    def list_formating(data):
        data_split = data.split()
            
        # Grundläggande filtering
        removers = ["\n", "\r", "\r\n", "\n\r", "\t"]
        
        data_remove = [i for i in data_split if 
                            i not in removers]
        data_fixed = ' '.join(data_remove)
        return data_fixed.split(".")
 
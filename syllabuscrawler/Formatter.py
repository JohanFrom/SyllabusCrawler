import pandas as pd

class Formatter:
    
    def format_table(links, data, keywords): 
        df = pd.DataFrame({
            "URL": [links], keywords[0]: [data[0]], keywords[1]: [data[1]], keywords[2]: [data[2]]
        })
        
        return df
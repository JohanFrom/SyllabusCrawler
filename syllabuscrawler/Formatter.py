import pandas as pd

class Formatter:
    
    def format_tabel(links, content):
        df = pd.DataFrame({
            "URL": [links], "Innehåll": [content]
        })
        
        print(df)
        
        return df
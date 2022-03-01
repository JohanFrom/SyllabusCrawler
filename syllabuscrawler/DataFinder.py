class DataFinder:

    def search_for_keyword(data, keywords):
        empty_list = []
        for d in data:
            for keyword in keywords:
                if keyword != "":
                    if keyword in d:
                        empty_list.append(d)
                            
        return empty_list
        
        
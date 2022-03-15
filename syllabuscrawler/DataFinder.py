class DataFinder:

    def search_for_keyword(data, keywords):
        empty_list = []
        splitted_data = data.split(".")
        for d in splitted_data:
            for keyword in keywords:
                if keyword != "":
                    if keyword in d:
                        empty_list.append(d)
                           
        return empty_list
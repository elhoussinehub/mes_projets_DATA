class MySelectQuery:
    def __init__(self,data):
        lines = data.strip().split("\n")
        self.header = lines[0].split(",")
        self.row = []
        for line in lines[1:] :
            row = line.split(",")
            self.row.append(row)
    def where(self,column_name,criteria) :
        if column_name not in self.header :
            return None
        index = self.header.index(column_name)
        result = []
        for row in self.row :
            if row[index] == criteria :
                result.append(",".join(row))
        return result
    
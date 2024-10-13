class Table:
    def cannot_fly(self):
        print('table cannot fly')
class Chair:
    def cannot_fly(self):
        print('chair also cannot fly ')
table = Table()
chair = Chair()

def object_carrier(obj):
    obj.cannot_fly()
    
object_carrier(table)
object_carrier(chair)

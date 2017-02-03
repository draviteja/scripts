import operator

def sort_table_data(table,col=0):
    return sorted(table,key=operator.itemgetter(col))

table_data = (
    ('raviteja','d',1992),
    ('chaitanya','d',1989),
    ('moni','d',1998),
    ('soni','g',1998),
    )

for row in sort_table_data(table_data):
    print(row)

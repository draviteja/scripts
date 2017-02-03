#unique
def invert_dict(d):
    return dict([(v, k) for k, v in d.items()])

d = {
     'child1': 'parent1',
     'child2': 'parent2',
     }
print(invert_dict(d))



#non unique
def invertt_dict_nonunique(d):
    newdict = {}
    for k,v in d.items():
        newdict.setdefault(v,[]).append(k)
    return newdict

d = {
     'child1': 'parent1',
     'child2': 'parent1',
     'child3': 'parent2',
     'child4': 'parent2',
    }
        
print(invertt_dict_nonunique(d))

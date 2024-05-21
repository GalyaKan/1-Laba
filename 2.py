def simple_map(transformation, values):
    result = []
    for i in values:
        result.append (transformation(i))
    return(result)


values = [1, 3, 1, 5, 7]
operation = lambda x: x+5
print(simple_map(operation, values))
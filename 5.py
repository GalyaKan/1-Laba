def same_by(characteristic, objects):
    if not objects:
        return True

    first_value = characteristic(objects[0])
    return all(characteristic(obj) == first_value for obj in objects)

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
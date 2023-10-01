values = [0, 2, 10, 6, 5]
def same_by(characteristic, objects):
    value2 = list(map(characteristic, objects))
    for i in range(len(value2)):
        if value2[i-1] != value2[i]:
            return False
    return True
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")
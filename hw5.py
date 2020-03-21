def setUp(file):
    with open(file, "r") as txt:
        whole = txt.read().split("\n")
        arr = []
        for i in whole:
            arr.append(i.split(";"))
        return arr
        

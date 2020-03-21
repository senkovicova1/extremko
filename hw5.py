def setUp(file):
    with open(file, "r") as txt:
        whole = txt.read().split("\n").pop()
        return whole
        

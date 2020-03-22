def setUp(file):
    with open(file, "r") as txt:
        whole = txt.read().split("\n")
        arr = []
        for i in range(0, len(whole)-1):
            arr.append(whole[i].split(";"))
        return arr


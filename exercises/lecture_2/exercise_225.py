"""Dictionary Manipulations"""

values = {"eins": 1, "zwei": 2, "drei": 3}

values.update({"eins": 2})
del values["drei"]
values.clear()
values.update({"null": 0})
values.update({"eins": 0})
values["eins"] = 1
del values["null"]

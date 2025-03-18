from typing import List, Tuple, Dict

# following line declares a List object of strings.
# if violated, mypy shows error
cities = List[str] = ['Mumbai', 'Delhi', 'Chennai']

# This is Tuple with three elements respectively
# of str, int and float (type)
employee: Tuple[str, int, float] = ('Ravi', 25, 35000)

# Similarly in the following Dict, the object key should be str
# and value should be of int type, failing which
# static type checker throws error
marklist: Dict[str, int] = {'Ravi': 61, 'Anil': 72}
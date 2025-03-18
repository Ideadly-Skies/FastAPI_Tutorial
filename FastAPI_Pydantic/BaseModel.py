from typing import List
from pydantic import BaseModel, Field #type: ignore

class Student(BaseModel):
    id: int
    name: str = Field(None, title="The description of the item", max_length=10)
    subjects: List[str] = []

if __name__ == "__main__":
    # will automatically get the data types converted whenever possible
    data = {
        'id': 1,
        'name': 'ObieAnanda',
        'subjects': ["Eng", "Maths", "Sci"],
    }

    # populate an object of Student class with
    # a dictionary with matching structure
    s1 = Student(**data)
    print(s1.dict())
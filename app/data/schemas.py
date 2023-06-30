from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    emp_id: int
    name: str
    email: str
    department: str


class EmployeeUpdate(BaseModel):
    name: Optional[str]
    email : Optional[str]
    department: Optional[str]
    


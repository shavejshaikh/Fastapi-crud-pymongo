
from app.data import schemas
from app.data.database import employee_collection
from fastapi import APIRouter, status, HTTPException

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, summary="get all employee data")
async def get_all_employee():
    list_emp = []
    for emp in employee_collection.find():
        items = {
            "emp_id": emp['emp_id'],
            "name" : emp['name'],
            "email": emp['email'],
            "department": emp['department']
        }
        list_emp.append(items)
    return list_emp


@router.post("/", status_code=status.HTTP_201_CREATED, summary="create a employee") 
async def create_employee(employee: schemas.Employee):
    is_emp = employee_collection.find_one({"emp_id": employee.emp_id}, {"_id": 0})
    if not is_emp:
        emp = employee_collection.insert_one(employee.dict())
        if emp.acknowledged:
            return {"detail" : "successfully stored data"}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Employee collection have {employee.emp_id} data")


@router.get("/{emp_id}", status_code=status.HTTP_200_OK, response_model=schemas.Employee, summary="get employee")
def get_employee(emp_id:int):
    emp = employee_collection.find_one({"emp_id": emp_id}, {"_id": 0})
    if emp:
        return emp
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee collection doesn't have {emp_id} data")

@router.put("/{emp_id}", status_code=status.HTTP_200_OK)
async def update_employee(emp_id:int, emp_update: schemas.EmployeeUpdate):
    emp = employee_collection.find_one({"emp_id": emp_id}, {"_id": 0})
    if emp:
        emp_update = emp_update.dict(exclude_none=True)
        employee_collection.update_one({"emp_id": emp_id}, {"$set": emp_update})
        return {"detail" : "successfully updated data"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee collection doesn't have {emp_id} data")


@router.delete("/{emp_id}", status_code=status.HTTP_200_OK, response_description="delete a employee")
async def delete_employee(emp_id: int):
    emp = employee_collection.find_one({"emp_id": emp_id})
    if emp:
        employee_collection.delete_one({"emp_id": emp_id})
        return {"detail" : "successfully deleted data"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee collection doesn't have {emp_id} data")
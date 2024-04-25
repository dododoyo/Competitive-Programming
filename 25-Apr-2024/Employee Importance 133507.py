# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp_dict = {emp.id: emp for emp in employees}
        
        def helper(emp_id):
            emp = emp_dict[emp_id]
            total_importance = emp.importance
            for sub_id in emp.subordinates:
                total_importance += helper(sub_id);
            return total_importance
        
        return helper(id)
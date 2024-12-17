#Leetcode introduction to pandas question sheet

import pandas as pd  #Library import

#Problem 1 : Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data,columns=["student_id","age"])

#Problem 2 : Write a solution to get size of the dataframe
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    a = players.shape[0]
    b = players.shape[1]
    return[a,b]

#Problem 3 : Write a solution to display the first 3 rows of this DataFrame
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

#Problem 4 : Write a solution to select the name and age of the student with student_id = 101.
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id']==101, ['name','age']]

#Problem 5 : A company plans to provide its employees with a bonus. Write a solution to create a new column name bonus that contains the doubled values of the salary column.
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*2
    return employees

    
import pandas as pd
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers


import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*2
    return employees

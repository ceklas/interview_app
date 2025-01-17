-- 6. Employee count by designation
SELECT Designation, COUNT(E_ID) AS employee_count
FROM Employees
GROUP BY Designation
ORDER BY employee_count DESC;

-- 7. Branch-wise employee count
SELECT E_Branch, COUNT(E_ID) AS employee_count
FROM Employees
GROUP BY E_Branch
ORDER BY employee_count DESC;

-- 12. Names and designations of employees in 'NY' branch
SELECT E_Name, Designation
FROM Employees
WHERE E_Branch = 'NY';

-- 20. Current status and delivery date of shipments managed by 'Delivery Boy'
SELECT Current_Status, Delivery_Date
FROM Shipments
JOIN Employees ON Shipments.Managed_By = Employees.E_ID
WHERE Employees.Designation = 'Delivery Boy';
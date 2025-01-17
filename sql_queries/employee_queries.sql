-- 6. Explore employee count based on the designation-wise count of employees' IDs in descending order.
SELECT emp_designation, COUNT(emp_id) AS employee_count
FROM employee_details
GROUP BY emp_designation
ORDER BY employee_count DESC;

-- 7. Branch-wise count of employees for efficiency of deliveries in descending order.
SELECT emp_branch, COUNT(emp_id) AS employee_count
FROM employee_details
GROUP BY emp_branch
ORDER BY employee_count DESC;

-- 12. Retrieve the names and designations of all employees in the 'NY' E_Branch.
SELECT emp_name, emp_designation
FROM employee_details
WHERE emp_branch = 'NY';

-- 20. Retrieve the current status and delivery date of shipments managed by employees with the designation 'Delivery Boy'.
SELECT shipment_details.sd_status, shipment_details.sd_delivery_date
FROM shipment_details
JOIN employee_manages_shipment ON shipment_details.sd_id = employee_manages_shipment.sd_id
JOIN employee_details ON employee_manages_shipment.emp_id = employee_details.emp_id
WHERE employee_details.emp_designation = 'Delivery Boy';
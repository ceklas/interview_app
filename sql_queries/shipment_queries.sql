-- 4. Count customers as per shipment domain
SELECT Shipment_Domain, COUNT(*) AS customer_count
FROM Shipments
GROUP BY Shipment_Domain
ORDER BY customer_count DESC;

-- 11. Average shipment weight by payment status
SELECT Payment_Status, AVG(Shipment_Weight) AS avg_weight
FROM Shipments
WHERE Shipment_Content NOT LIKE 'H%'
GROUP BY Payment_Status;

-- 16. Average shipment weight for each shipment domain
SELECT Shipment_Domain, AVG(Shipment_Weight) AS avg_weight
FROM Shipments
GROUP BY Shipment_Domain;

-- 17. Shipment with the highest charges and corresponding client's name
SELECT S_ID, C_Name, Charges
FROM Shipments
JOIN Customers ON Shipments.C_ID = Customers.C_ID
ORDER BY Charges DESC
LIMIT 1;
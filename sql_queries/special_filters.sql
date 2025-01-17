-- 15. Clients with 'Card Payment' and 'Regular' service type
SELECT C_Name
FROM Customers
JOIN Payments ON Customers.C_ID = Payments.C_ID
WHERE Payments.Payment_Mode = 'Card Payment' AND Customers.Service_Type = 'Regular';

-- 18. Count of 'Express' service type shipments yet to be delivered
SELECT COUNT(*) AS express_pending
FROM Shipments
WHERE Service_Type = 'Express' AND Current_Status != 'Delivered';

-- 19. Clients with 'Not Paid' payment status in 'CA'
SELECT C_Name
FROM Customers
JOIN Payments ON Customers.C_ID = Payments.C_ID
WHERE Payments.Payment_Status = 'Not Paid' AND Customers.State = 'CA';
-- 8. Customers with membership over 10 years
SELECT C_ID, M_ID, 
       DATE_PART('year', AGE(Membership_End, Membership_Start)) AS tenure
FROM Memberships
WHERE DATE_PART('year', AGE(Membership_End, Membership_Start)) > 10;

-- 14. Membership start and end dates for customers with 'Paid' payment status
SELECT Membership_Start, Membership_End
FROM Memberships
WHERE Payment_Status = 'Paid';

-- 21. Membership dates for customers with 'Not Delivered' status
SELECT Membership_Start, Membership_End
FROM Memberships
JOIN Shipments ON Memberships.C_ID = Shipments.C_ID
WHERE Shipments.Current_Status = 'Not Delivered';
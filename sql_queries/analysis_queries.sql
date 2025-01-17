-- 1. Count the customer base based on customer type
SELECT C_TYPE, COUNT(*) AS customer_count
FROM Customers
GROUP BY C_TYPE
ORDER BY customer_count DESC;

-- 2. Count the customer base based on their status of payment
SELECT Payment_Status, COUNT(*) AS customer_count
FROM Payments
GROUP BY Payment_Status
ORDER BY customer_count DESC;

-- 3. Count the customer base based on their payment mode
SELECT Payment_Mode, COUNT(*) AS customer_count
FROM Payments
GROUP BY Payment_Mode
ORDER BY customer_count DESC;

-- 9. Average payment amount based on customer type (COD)
SELECT C_TYPE, AVG(Payment_Amount) AS avg_payment
FROM Payments
WHERE Payment_Mode = 'COD'
GROUP BY C_TYPE
ORDER BY avg_payment DESC;
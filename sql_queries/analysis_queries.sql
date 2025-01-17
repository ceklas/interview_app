-- 1. Count the customer base based on customer type to identify current customer preferences and sort them in descending order.
SELECT cust_type, COUNT(*) AS customer_count
FROM customer
GROUP BY cust_type
ORDER BY customer_count DESC;

-- 2. Count the customer base based on their status of payment in descending order.
SELECT payment_status, COUNT(*) AS customer_count
FROM payment_details
GROUP BY payment_status
ORDER BY customer_count DESC;

-- 3. Count the customer base based on their payment mode in descending order of count.
SELECT payment_mode, COUNT(*) AS customer_count
FROM payment_details
GROUP BY payment_mode
ORDER BY customer_count DESC;

-- 4. Count the customers as per shipment domain in descending order.
SELECT sd_domain, COUNT(*) AS customer_count
FROM shipment_details
GROUP BY sd_domain
ORDER BY customer_count DESC;

-- 5. Count the customer according to service type in descending order of count.
SELECT sd_type, COUNT(*) AS customer_count
FROM shipment_details
GROUP BY sd_type
ORDER BY customer_count DESC;
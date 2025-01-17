-- 9. Considering average payment amount based on customer type having payment mode as COD in descending order.
SELECT cust_type, AVG(payment_details.amount) AS avg_payment
FROM payment_details
JOIN customer ON payment_details.customer_id = customer.cust_id
WHERE payment_details.payment_mode = 'COD'
GROUP BY cust_type
ORDER BY avg_payment DESC;

-- 10. Calculate the average payment amount based on payment mode where the payment date is not null.
SELECT payment_mode, AVG(amount) AS avg_payment
FROM payment_details
WHERE payment_date IS NOT NULL
GROUP BY payment_mode;

-- 11. Calculate the average shipment weight based on payment_status where shipment content does not start with "H."
SELECT payment_status, AVG(sd_weight::numeric) AS avg_weight
FROM shipment_details
JOIN payment_details ON shipment_details.sd_id = payment_details.shipment_id
WHERE sd_content NOT LIKE 'H%'
GROUP BY payment_status;

-- 13. Calculate the total number of customers in each C_TYPE (Wholesale, Retail, Internal Goods).
SELECT cust_type, COUNT(*) AS customer_count
FROM customer
GROUP BY cust_type;

-- 15. List the clients who have made 'Card Payment' and have a 'Regular' service type.
SELECT customer.cust_name
FROM customer
JOIN payment_details ON customer.cust_id = payment_details.customer_id
JOIN shipment_details ON customer.cust_id = shipment_details.cust_id
WHERE payment_details.payment_mode = 'Card Payment' AND shipment_details.sd_type = 'Regular';

-- 21. Find the membership start and end dates for customers whose 'Current Status' is 'Not Delivered'.
SELECT customer.cust_id, membership.start_date, membership.end_date
FROM customer
JOIN membership ON customer.membership_m_id = membership.m_id
JOIN shipment_details ON shipment_details.cust_id = customer.cust_id
WHERE shipment_details.sd_status = 'Not Delivered';
-- 16. Calculate the average shipment weight for each shipment domain (International and Domestic).
SELECT sd_domain, AVG(sd_weight::numeric) AS avg_weight
FROM shipment_details
GROUP BY sd_domain;

-- 17. Identify the shipment with the highest charges and the corresponding client's name.
SELECT shipment_details.sd_id, shipment_details.sd_charge, customer.cust_name
FROM shipment_details
JOIN customer ON shipment_details.cust_id = customer.cust_id
ORDER BY shipment_details.sd_charge DESC
LIMIT 1;

-- 18. Count the number of shipments with the 'Express' service type that are yet to be delivered.
SELECT COUNT(*) AS express_shipments_count
FROM shipment_details
WHERE sd_type = 'Express' AND sd_status != 'Delivered';

-- 19. List the clients who have 'Not Paid' payment status and are based in 'CA'.
SELECT customer.cust_name, customer.cust_address
FROM customer
JOIN payment_details ON customer.cust_id = payment_details.customer_id
WHERE payment_details.payment_status = 'Not Paid' AND customer.cust_address LIKE '%CA%';
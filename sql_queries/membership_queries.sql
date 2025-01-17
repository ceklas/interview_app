-- 8. Finding C_ID, M_ID, and tenure for those customers whose membership is over 10 years.
SELECT customer.cust_id, membership.m_id, EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM membership.start_date) AS tenure
FROM customer
JOIN membership ON customer.membership_m_id = membership.m_id
WHERE EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM membership.start_date) > 10;

-- 14. Find the membership start and end dates for customers with 'Paid' payment status.
SELECT customer.cust_id, membership.start_date, membership.end_date
FROM customer
JOIN membership ON customer.membership_m_id = membership.m_id
JOIN payment_details ON payment_details.customer_id = customer.cust_id
WHERE payment_details.payment_status = 'Paid';
SELECT first_name, last_name, email
FROM users
WHERE city = 'Toshkent';

SELECT *
FROM users
WHERE signup_date > '2024-03-01'
  AND EXTRACT(MONTH FROM last_login) = 11
  AND EXTRACT(YEAR FROM last_login) = 2024;

SELECT region, COUNT(*) AS user_count
FROM users
GROUP BY region
ORDER BY user_count DESC;


SELECT COUNT(*) AS active_gmail_users
FROM users
WHERE email LIKE '%@gmail.com'
  AND status = 'active';


SELECT *
FROM users
ORDER BY signup_date DESC
LIMIT 5;

SELECT *
FROM users
WHERE signup_date < '2024-07-01';

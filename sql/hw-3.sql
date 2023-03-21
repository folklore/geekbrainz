-- 1

SELECT DISTINCT ON (firstname)
       firstname
FROM users
ORDER BY firstname;

-- 2

SELECT COUNT(1)
FROM profiles
WHERE gender = 'M'
  AND birthday < NOW() - '35 years'::interval;

-- 3

SELECT status,
       COUNT(1) AS requests_count
FROM friend_requests
GROUP BY status;

-- 4

SELECT initiator_user_id,
       COUNT(1) AS requests_count
FROM friend_requests
GROUP BY initiator_user_id
ORDER BY requests_count DESC
LIMIT 1

-- 5

SELECT title,
       id
FROM groups
WHERE LENGTH(title) = 5;

-- 5

SELECT title,
       id
FROM groups
WHERE title LIKE '____';

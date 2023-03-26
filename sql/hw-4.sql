-- 1

SELECT users.id, COUNT(ucs.user_id) AS groups_count
FROM users
LEFT JOIN users_communities AS ucs ON users.id = ucs.user_id
GROUP BY users.id
ORDER BY groups_count DESC;

-- 2

SELECT community_id, COUNT(user_id) AS users_count
FROM users_communities
GROUP BY community_id
ORDER BY users_count DESC;

-- 3

SELECT to_user_id, COUNT(from_user_id) AS messages_count
FROM messages
WHERE to_user_id = 1
GROUP BY to_user_id, from_user_id
ORDER BY messages_count DESC
LIMIT 1;

-- 4

SELECT COUNT(likes.id)
FROM likes
JOIN profiles ON likes.user_id = profiles.user_id
WHERE profiles.birthday < NOW() - '18 years'::interval;

-- 5

SELECT profiles.gender, COUNT(likes.id) AS likes_count
FROM likes
JOIN profiles ON likes.user_id = profiles.user_id
WHERE profiles.birthday < NOW() - '18 years'::interval
GROUP BY profiles.gender
ORDER BY likes_count DESC
LIMIT 1;

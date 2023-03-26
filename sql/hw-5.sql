CREATE OR REPLACE VIEW full_user_profile AS
  SELECT users.id, users.firstname, users.lastname, profiles.gender, profiles.birthday
  FROM users
  JOIN profiles ON profiles.user_id = users.id;


SELECT * FROM full_user_profile LIMIT 1;

     id | firstname | lastname  | gender |  birthday  
    ----+-----------+-----------+--------+------------
      1 | Лина      | Весёлкина | M      | 1966-12-24


DROP VIEW full_user_profile;

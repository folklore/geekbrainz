WITH getval(id) as
    (INSERT INTO users (firstname, lastname, email, password_hash, phone) VALUES ('Лина', 'Весёлкина', 'lv@m.t', 'vzx;clvgkajrpo9udfxvsldkrn24l5456345t', 1234567901) RETURNING id) 
INSERT into profiles (user_id, gender, birthday, hometown) VALUES ((SELECT id from getval), 'M', '1966-12-24', 'Москва');

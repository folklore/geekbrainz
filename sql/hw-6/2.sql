CREATE OR REPLACE PROCEDURE oblivion_proc(INOUT current_user_id int)
    LANGUAGE plpgsql
AS $$
BEGIN
    -- Удаляем исх. сообщения
    DELETE FROM messages WHERE from_user_id = current_user_id;
    -- Удаляем вход. сообщения
    DELETE FROM messages WHERE to_user_id = current_user_id;

    -- Удаляем исх. запросы на дружбу
    DELETE FROM friend_requests WHERE initiator_user_id = current_user_id;
    -- Удаляем вход. запросы на дружбу
    DELETE FROM friend_requests WHERE target_user_id = current_user_id;

    -- Удаляем собственные группы
    DELETE FROM communities WHERE admin_user_id = current_user_id;
    -- Удаляем связи собственных групп и членов групп
    DELETE FROM users_communities WHERE community_id = current_user_id;
    -- Удаляем членства в чужих группах
    DELETE FROM users_communities WHERE user_id = current_user_id;

    -- Удаляем медиа
    DELETE FROM media WHERE user_id = current_user_id;

    -- Удаляем лайки
    DELETE FROM likes WHERE user_id = current_user_id;

    -- Удаляем профайл
    DELETE FROM profiles WHERE user_id = current_user_id;
    -- Удаляем пользователя
    DELETE FROM users WHERE id = current_user_id;

    COMMIT;
END; $$;

-- Удаляем профайл
ALTER TABLE profiles 
    ADD CONSTRAINT fk_profiles_on_user_id
    FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON UPDATE RESTRICT
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED;

-- Удаляем исх. сообщения
ALTER TABLE messages 
    ADD CONSTRAINT fk_messages_on_from_user_id
    FOREIGN KEY (from_user_id)
    REFERENCES users(id)
    ON UPDATE RESTRICT
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED;

-- Удаляем вход. сообщения
ALTER TABLE messages 
    ADD CONSTRAINT fk_messages_on_to_user_id
    FOREIGN KEY (to_user_id)
    REFERENCES users(id)
    ON UPDATE RESTRICT
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED;

-- Удаляем исх. запросы на дружбу
ALTER TABLE friend_requests 
    ADD CONSTRAINT fk_friend_requests_on_initiator_user_id
    FOREIGN KEY (initiator_user_id)
    REFERENCES users(id)
    ON UPDATE RESTRICT
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED;

-- Удаляем вход. запросы на дружбу
ALTER TABLE friend_requests 
    ADD CONSTRAINT fk_friend_requests_on_target_user_id
    FOREIGN KEY (target_user_id)
    REFERENCES users(id)
    ON UPDATE RESTRICT
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED;

-- Удаляем собственные группы
ALTER TABLE communities 
    ADD CONSTRAINT fk_communities_on_admin_user_id
    FOREIGN KEY (admin_user_id)
    REFERENCES users(id)
    ON UPDATE RESTRICT
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED;

-- Удаляем связи собственных групп и членов групп
ALTER TABLE users_communities 
    ADD CONSTRAINT fk_users_communities_on_community_id
    FOREIGN KEY (community_id)
    REFERENCES communities(id)
    ON UPDATE RESTRICT
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED;

-- Удаляем членства в чужих группах
ALTER TABLE users_communities 
    ADD CONSTRAINT fk_users_communities_on_user_id
    FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON UPDATE RESTRICT
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED;

-- Удаляем медиа
ALTER TABLE media 
    ADD CONSTRAINT fk_media_on_user_id
    FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON UPDATE RESTRICT
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED;

-- Удаляем лайки
ALTER TABLE likes 
    ADD CONSTRAINT fk_likes_on_user_id
    FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON UPDATE RESTRICT
    ON DELETE CASCADE
    DEFERRABLE INITIALLY DEFERRED;

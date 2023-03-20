DROP TABLE IF EXISTS users;

CREATE SEQUENCE users_seq;

CREATE TABLE users (
    id BIGINT CHECK (id > 0) NOT NULL DEFAULT NEXTVAL ('users_seq') PRIMARY KEY, 
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    email VARCHAR(120) UNIQUE,
    password_hash VARCHAR(100),
    phone BIGINT CHECK (phone > 0) UNIQUE 
);

COMMENT ON COLUMN users.lastname IS 'Фамиль';

CREATE INDEX users_firstname_lastname_idx ON users(firstname, lastname);

DROP TABLE IF EXISTS profiles;

CREATE TABLE profiles (
    user_id BIGINT CHECK (user_id > 0) NOT NULL UNIQUE,
    gender CHAR(1),
    birthday DATE,
    created_at TIMESTAMP(0) DEFAULT NOW(),
    hometown VARCHAR(100)
);

ALTER TABLE profiles ADD CONSTRAINT fk_user_id
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT;

DROP TABLE IF EXISTS messages;

CREATE TABLE messages (
    id SERIAL,
    from_user_id BIGINT CHECK (from_user_id > 0) NOT NULL,
    to_user_id BIGINT CHECK (to_user_id > 0) NOT NULL,
    body TEXT,
    created_at TIMESTAMP(0) DEFAULT NOW(),

    FOREIGN KEY (from_user_id) REFERENCES users(id),
    FOREIGN KEY (to_user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS friend_requests;

DROP TYPE IF EXISTS enum_friend_request_status;

CREATE TYPE enum_friend_request_status AS ENUM('requested', 'approved', 'declined', 'unfriended');

CREATE TABLE friend_requests (
    initiator_user_id BIGINT CHECK (initiator_user_id > 0) NOT NULL,
    target_user_id BIGINT CHECK (target_user_id > 0) NOT NULL,
    status enum_friend_request_status,
    requested_at TIMESTAMP(0) DEFAULT NOW(),
    updated_at TIMESTAMP(0),

    PRIMARY KEY (initiator_user_id, target_user_id),
    FOREIGN KEY (initiator_user_id) REFERENCES users(id),
    FOREIGN KEY (target_user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS communities;

CREATE TABLE communities(
    id SERIAL,
    name VARCHAR(150),
    admin_user_id BIGINT CHECK (admin_user_id > 0) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (admin_user_id) REFERENCES users(id)
);

CREATE INDEX communities_name_idx ON communities(name);

DROP TABLE IF EXISTS users_communities;

CREATE TABLE users_communities(
    user_id BIGINT CHECK (user_id > 0) NOT NULL,
    community_id BIGINT CHECK (community_id > 0) NOT NULL,
  
    PRIMARY KEY (user_id, community_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (community_id) REFERENCES communities(id)
);

DROP TABLE IF EXISTS media_types;

CREATE TABLE media_types(
    id SERIAL,
    name VARCHAR(255),
    created_at TIMESTAMP(0) DEFAULT NOW(),
    updated_at TIMESTAMP(0),
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS media;

CREATE TABLE media(
    id SERIAL,
    media_type_id BIGINT CHECK (media_type_id > 0) NOT NULL,
    user_id BIGINT CHECK (user_id > 0) NOT NULL,
    body text,
    filename VARCHAR(255),     
    size INT,
    metadata JSON,
    created_at TIMESTAMP(0) DEFAULT NOW(),
    updated_at TIMESTAMP(0),

    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (media_type_id) REFERENCES media_types(id)
);

DROP TABLE IF EXISTS likes;

CREATE TABLE likes(
    id SERIAL,
    user_id BIGINT CHECK (user_id > 0) NOT NULL,
    media_id BIGINT CHECK (media_id > 0) NOT NULL,
    created_at TIMESTAMP(0) DEFAULT NOW()
);

ALTER TABLE likes 
ADD CONSTRAINT likes_fk 
FOREIGN KEY (media_id) REFERENCES media(id);

ALTER TABLE likes 
ADD CONSTRAINT likes_fk_1 
FOREIGN KEY (user_id) REFERENCES users(id);


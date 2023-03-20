
DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks(
    id SERIAL,
    description VARCHAR(150),
    user_id BIGINT CHECK (user_id > 0) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE INDEX idx_tasks_on_user_id ON tasks(user_id);

--

DROP TABLE IF EXISTS events;

CREATE TABLE events(
    id SERIAL,
    title VARCHAR(150),
    owner_id BIGINT CHECK (owner_id > 0) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (owner_id) REFERENCES users(id)
);

CREATE INDEX idx_events_on_title ON events(title);
CREATE INDEX idx_events_on_owner_id ON events(owner_id);

DROP TABLE IF EXISTS users_events;

CREATE TABLE users_events(
    user_id BIGINT CHECK (user_id > 0) NOT NULL,
    event_id BIGINT CHECK (event_id > 0) NOT NULL,
  
    PRIMARY KEY (user_id, event_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (event_id) REFERENCES events(id)
);

CREATE INDEX idx_events_on_foreign_keys ON users_events(user_id, event_id);


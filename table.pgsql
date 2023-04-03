DROP TABLE IF EXISTS plan CASCADE;
DROP TABLE IF EXISTS university CASCADE;
DROP TABLE IF EXISTS user_share CASCADE;

CREATE TABLE university (
    email TEXT PRIMARY KEY,
    pw TEXT,
    fontsize INT DEFAULT 12,
    reminder INT DEFAULT 24,
    color INT DEFAULT 8
);

CREATE TABLE plan (
    username TEXT REFERENCES university(email),
    lecture_name TEXT,
    assignment_name TEXT,
    due_date TIMESTAMP without time zone default (now() at time zone 'utc'),
    reminder INT DEFAULT 1,
    to_do INT DEFAULT 0,
    description TEXT DEFAULT '',
    sharer TEXT DEFAULT NULL,
    PRIMARY KEY (username, lecture_name, assignment_name, due_date)
);

CREATE TABLE user_share (
    username TEXT REFERENCES university(email),
    shared TEXT DEFAULT NULL,
    PRIMARY KEY(username, shared)
);
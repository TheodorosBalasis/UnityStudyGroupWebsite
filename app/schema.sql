CREATE TABLE credential(
    id SERIAL PRIMARY KEY,
    slack_id CHARACTER(9) NOT NULL
);
CREATE TABLE token(
    id SERIAL PRIMARY KEY,
    credential_id INTEGER REFERENCES credential(id) NOT NULL,
    token CHAR(30) NOT NULL,
    valid BOOLEAN NOT NULL
);
CREATE TABLE session_cookie(
    token INTEGER REFERENCES token(id),
    cookie CHARACTER(9),
    PRIMARY KEY (token, cookie)
);
CREATE TABLE resource(
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES credential(id) NOT NULL,
    title VARCHAR(200) NOT NULL,
    link VARCHAR(2500) NOT NULL,
    description VARCHAR(5000) NOT NULL
);
CREATE TABLE article(
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES credential(id) NOT NULL,
    title VARCHAR(200) NOT NULL,
    body VARCHAR(25000) NOT NULL
);
CREATE TABLE project(
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES credential(id) NOT NULL,
    title VARCHAR(200) NOT NULL,
    description VARCHAR(5000) NOT NULL
);
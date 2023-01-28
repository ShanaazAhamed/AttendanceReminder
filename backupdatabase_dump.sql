BEGIN TRANSACTION;
CREATE TABLE users
        (id     INT PRIMARY KEY     NOT NULL,
        in_t    TEXT                NOT NULL,
        out_t   INT                 NOT NULL,
        url     TEXT
        );
INSERT INTO "users" VALUES(1,'8:30AM','5:00PM','www.wss.com');
COMMIT;

BEGIN TRANSACTION;
CREATE TABLE users
        (id     INTEGER             PRIMARY KEY AUTOINCREMENT,
        in_t    TEXT                NOT NULL,
        out_t   TEXT                NOT NULL,
        url     TEXT
        );
INSERT INTO "users" VALUES(1,'8:30AM','5:00PM','www.wss.com');
INSERT INTO "users" VALUES(2,'8:30AM','5:00PM','www.wss.com');
INSERT INTO "users" VALUES(3,'8:30AM','5:00PM','www.wss.com');
INSERT INTO "users" VALUES(4,'8:30AM','5:00PM','www.wss.com');
INSERT INTO "users" VALUES(5,'8:30AM','5:00PM','www.wss.com');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('users',5);
COMMIT;

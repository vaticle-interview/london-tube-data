DROP TABLE IF EXISTS stations;
DROP TABLE IF EXISTS lines;
DROP TABLE IF EXISTS passes;

CREATE TABLE stations (
    `id` varchar(16) NOT NULL PRIMARY KEY,
    `name` varchar(64) NOT NULL
);

CREATE TABLE lines (
    `id` int(16) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` varchar(64) NOT NULL
); 

CREATE TABLE salaries (
    `station_id` varchar(16) NOT NULL,
    `line_id` int(16) NOT NULL,
    PRIMARY KEY (`station_id`, `line_id`),
    FOREIGN KEY (`station_id`) REFERENCES stations(`id`),
    FOREIGN KEY (`line_id`) REFERENCES lines(`id`)
);
DROP TABLE IF EXISTS passes;
DROP TABLE IF EXISTS stations;
DROP TABLE IF EXISTS trainlines;

CREATE TABLE stations (
    `id` varchar(16) NOT NULL PRIMARY KEY,
    `name` varchar(64) NOT NULL
);

CREATE TABLE trainlines (
    `id` int(16) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` varchar(64) NOT NULL
); 

CREATE TABLE passes (
    `station_id` varchar(16) NOT NULL,
    `line_id` int(16) NOT NULL,
    PRIMARY KEY (`station_id`, `line_id`),
    FOREIGN KEY (`station_id`) REFERENCES stations(`id`),
    FOREIGN KEY (`line_id`) REFERENCES trainlines(`id`)
);
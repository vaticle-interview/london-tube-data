TABLES = {}
TABLES['stations'] = (
    "CREATE TABLE `stations` ("
    "  `id` int(16) NOT NULL,"
    "  `name` varchar(64) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['lines'] = (
    "CREATE TABLE `lines` ("
    "  `id` int(16) NOT NULL,"
    "  `name` varchar(64) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['passes'] = (
    "CREATE TABLE `salaries` ("
    "  `station_id` int(16) NOT NULL,"
    "  `line_id` int(16) NOT NULL,"
    "  PRIMARY KEY (`station_id`,`line_id`)"
    "  FOREIGN KEY (`station_id`) "
    "     REFERENCES stations(`id`) ON DELETE CASCADE"
    "  FOREIGN KEY (`line_id`) "
    "     REFERENCES lines(`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

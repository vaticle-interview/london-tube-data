## How to use this application
0. Make sure there is a local MySQL server running.
1. Start the application.
2. Enter user credentials for the MySQL server.
3. You can now make queries, use -help to see all the possible commands.

# Dependencies
You might find the following links useful if you want to run this application
in a local environment.
1. MySQL Connector/Python for accessing the MySQL server
https://dev.mysql.com/doc/connector-python/en/
2. PyYAML for configuration
https://pypi.org/project/PyYAML/

## Engineering Decisions
# Programmng style
1. Snake case and single quotes (except for multi-line strings) are used throughout the whole application as per python conventions.

# Design
1. Configurations (including string literals) are stored in a separate config.yaml
file for better adaptability.
2. Other than foreign key, there is no extra constraint on the database schema. 
Because the user is not supposed to modify the database directly.

# Behavioural 
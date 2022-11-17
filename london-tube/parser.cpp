#include <stdlib.h>
#include <iostream>

#include <mysqlx/xdevapi.h>

using namespace mysqlx;

std::string prompt(string s) {
	std::cout << s;
	std::string input;
	std::cin >> input;
	return input;
}

int establishSession() {
	// establish a session
	string usr = prompt("Username:");
	string pwd = prompt("Password:");

	// Connect to MySQL Server on a network machine
	Session mySession(SessionOption::HOST, "localhost",
		SessionOption::PORT, 33060,
		SessionOption::USER, usr,
		SessionOption::PWD, pwd);

	// TODO: do something if the username & password combination is not valid

	std::cout << "successfully established session";

	// Get a list of all available schemas
    std::cout << "Available schemas in this session:" << std::endl;

	std::list<Schema> schemaList = mySession.getSchemas();

	// Loop over all available schemas and print their name
	for (Schema schema : schemaList) {
		std::cout << schema.getName() << std::endl;
	} 
}

void acceptQueries() {
	bool exit = false;
	while (true) {
		
	}

}

int main()
{
	//loaddata();
	establishSession();
	acceptQueries();

	return 0;
}


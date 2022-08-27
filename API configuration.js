// JavaScript source code
// Convert parameters from string to int 
p = p as int 
c = c as int 

// Initialize the list to store users information 
def usersInformation  = {}

// Get the list of user 
List<User> users = context.apiClient.identityAPI.getUsers(p*c, c,);
// Iterate over each user
for (user in users) {
	// Get user extra information (including email address)
	ContactData contactData = context.apiClient.identityAPI.getUserContactData(user.id, false)

	// Create a map with current user first name, last name and email address
	def userInformation = [firstName: user.firstName, lastName: user.lastName, email: contactData.email]

	// Add current user information to the global list
	usersInformation << userInformation
}

// Prepare the result
def result = [p: p, c: c, userInformation: usersInformation]

int startIndex = p*c
int endIndex = p*c + users.size() - 1

// Send the result as a JSON representation
return buildPagedResponse(responseBuilder, new JsonBuilder(result).toString(), startIndex, endIndex, context.apiClient.identityAPI.numberOfUsers)
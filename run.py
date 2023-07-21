

def isValidUserName(username):
    if username == "hello":
        return True
    
    return False

def isValidPassword(password):
    if password == "1234":
        return True
    
    return False

if isValidUserName("hello"):
    if isValidPassword("1234"):
        print("Test Success")

# After Added Calling Function.
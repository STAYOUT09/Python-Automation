def clean_username(username):
    username = "_".join(username.strip().lower().split())
    cleanedusername = ""
    prevchar=""
    for  char in username:
        if char.isalnum():
            cleanedusername += char
            prevchar = char
        elif char == "_" or char == " ":
            if prevchar != "_":
                cleanedusername += "_"
                prevchar = "_"
    return cleanedusername.strip("_")

username = input("Enter your username: ")
cleaned_username = clean_username(username)
print(f"Cleaned username: {cleaned_username}")
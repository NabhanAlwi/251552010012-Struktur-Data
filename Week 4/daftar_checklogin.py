user = {
    "lutfi": "lutfibadut",
    "fizz": "hafidzanginer",
    "jrul": "jrullbadut"
}

login_attempt = [
    ("lutfi", "lutfibadut"),
    ("fizz", "hafidzanginer"),
    ("jrul", "jrullbadut"),
    ("sudes", "sudessbadut") 
]

for username, password in login_attempt:
    if username in user and user[username] == password:
        print(f"Login {username} WELCOME!")
    else:
        print(f"login {username} GAGAL!")
user = {"nama":"lutfi", "umur": 28}

email = user.get("email", "email tidak ditemukan")
print(email)

user.setdefault("email", "lutfi@badut.com")

user.update({"umur": 29, "role": "cyber"})

age = user.pop("umur")

print(user.keys())
print(user.values())

user_copy = user.copy()
print(user_copy)

print(user)
print(user_copy)
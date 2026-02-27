user ={
    "lutfi": "lutfibadut",
    "fizz": "hafidz123",
    "jrul": "jrul123"  
}

username = (input("masukan username: "))
password = (input("masukan password: "))

if username in user and user[username]== password: 
    print("selmat datang!")
else:
    print("username atau password salah.") 
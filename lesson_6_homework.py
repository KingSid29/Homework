
char = input("Enter a character: ")

if len(char) == 1:
    if ("a" <= char <= "z") or ("A" <= char <= "Z"):
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
else:
    print("Please enter only a single character.")

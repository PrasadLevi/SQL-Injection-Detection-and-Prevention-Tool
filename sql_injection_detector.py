
print("SQL Injection Detection Tool")
print()

user_input = input("Enter text to analyze: ")

issues = 0

if "'" in user_input:
    print("Single quote detected")
    issues += 1

if "OR" in user_input.upper():
    print("OR keyword detected")
    issues += 1

if "SELECT" in user_input.upper():
    print("SELECT keyword detected")
    issues += 1

if "UNION" in user_input.upper():
    print("UNION keyword detected")
    issues += 1

if "DROP" in user_input.upper():
    print("DROP keyword detected")
    issues += 1

print()

if issues == 0:
    print("Risk Level: Low")
elif issues <= 2:
    print("Risk Level: Medium")
else:
    print("Risk Level: High")

print()
print("Security Recommendation:")
print("Use parameterized queries and validate user input.")


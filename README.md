SQL Injection Detection and Prevention Tool

Description

This project is a Python program that analyzes user input and checks for patterns that may indicate a SQL injection attempt. It helps users understand basic cybersecurity concepts and secure coding practices.

Features

Checks user input for suspicious patterns

Detects common SQL keywords

Assigns a risk level

Provides security recommendations

Technology Used

Python

Problem Statement

SQL injection is a common security vulnerability that can affect database-driven applications. This project helps identify suspicious input patterns and promotes awareness of secure coding practices.

How to Run the Program

1. Open the project folder in Visual Studio Code.

2. Open the terminal.

3. Run the following command:

python sql_injection_detector.py

Sample Run

Input:

admin' OR '1'='1

Output:

Single quote detected

OR keyword detected

Risk Level: Medium

Security Recommendation:

Use parameterized queries and validate user input.

Project Structure

SQL-Injection-Detection-and-Prevention-Tool

README.md

sql_injection_detector.py

Learning Outcomes

Python programming

Conditional statements

Input validation

SQL injection awareness

Secure coding practices

Future Improvements

Author

Prasad Levi

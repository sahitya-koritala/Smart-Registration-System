# Project Title 
Smart Regustration System 

#Description 
The program validates user inputs such as registration number, student ID, email ID, password, and referral code using conditional statements and strings.
The order of validation is done based on the last three digits of registration number.

# Features

- Handles multiple user inputs.
- Extracts last three digits of register number.
- Uses even/odd logic to decide the particular order.
- Validates student ID, email ID, password, and referral code.
- Prints output as APPROVED or REJECTED based on the conditions.

# Technologies Used

- Python
- Conditional statements
- String slicing and string functions

# How It Works

- The code accepts and take user inputs.
- The last three digits of the register number are taken.
- If the number is even, password validation is performed first.
- If the number is odd, student ID validation is performed first.
- The remainig validations are performed for email, password, and referral code.
- If all conditions are satisfied, the code prints APPROVED.
- If any condition is not satisfied, the code prints REJECTED.

# How to Run
- Open any IDE that supports Python.
- Save the code as a .py file.
- Run the code.
- Enter the necessary details when prompted.

  # Learning Outcomes
  From this challenge, I have learned how to take user inputs from the user and also using string slicing, indexing and the conditional statements and also how to use the basic string functions like length checking, counting the characters by using the count() and indexing to check the positions of characters. I also learnt how to use the basic functions such as isdigit().

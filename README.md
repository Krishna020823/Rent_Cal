# Rent Calculator

This project is a simple Python script to help you calculate the share of rent and utilities for each person living in a hostel or flat. It takes into account the rent, food expenses, electricity usage, and the number of people sharing the accommodation.

## How It Works

1. **User Inputs:**
    - Hostel/flat rent
    - Amount spent on food
    - Total electricity consumed (in units)
    - Charge per unit of electricity
    - Number of persons sharing the accommodation

2. **Calculation:**
    - The script calculates the total electricity bill by multiplying the units consumed by the charge per unit.
    - It then adds the rent, food expenses, and total electricity bill.
    - The total is divided equally among all persons to determine each person's share.

3. **Output:**
    - The script prints the amount each person needs to pay.

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the script using Python:

   ```powershell
   python Rent_Cal.py
   ```

3. Enter the required values when prompted.
4. The script will display each person's share.

## Example

```
Enter your hostel/flat rent = 10000
Enter the amount of food ordered = 3000
Enter the total of electricity spend in Units = 150
Enter the charge per unit = 10
Enter the number of persons living in room/flat = 4
Each person's share is: 4175
```

## Requirements
- Python 3.x

No external libraries are required.

## Author
- Your Name Here

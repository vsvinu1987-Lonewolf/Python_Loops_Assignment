# Name: Vinumon V S
# Roll Number: IITP_AIMLTN_2602558
# Assignment: Python Loops & Automation - Subjective Question

# ===== Task 1: Find Maximum and Minimum =====
print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

# Initialize max and min with the first element of the list
highest = temperatures[0]
lowest = temperatures[0]

for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

print(f"Highest Temperature: {highest}°C")
print(f"Lowest Temperature: {lowest}°C")


# ===== Task 2: Count Hot Days =====
print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
hot_days_count = 0

for temp in temperatures:
    if temp <= 30:
        continue  # Skip days that are 30 or below
    hot_days_count += 1

print(f"Hot Days (>30°C): {hot_days_count}")


# ===== Task 3: Alert System =====
print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
hot_days_before_alert = 0
day_counter = 0

for temp in temperatures:
    day_counter += 1
    
    if temp >= 40:
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day_counter}")
        break  # Stop the loop immediately
    
    if temp > 30:
        hot_days_before_alert += 1

print(f"Hot Days before alert: {hot_days_before_alert}")
import time


def monthly_water_bill(start_amt, current_amt):
    """Return billed amount from starting current read and prior amount."""
    # start_time = time.process_time_ns()
    water_base = 10.830
    water_first_3 = 1.320
    water_over_3 = 2.630
    sewer_charge = 9.010
    garbage_fee = 7
    recycling_fee = 2.5
    safe_drinking_water_fee = 1.000
    security_fee = 0.500
    total_bill = water_base + sewer_charge + garbage_fee + security_fee
    total_bill = total_bill + recycling_fee + safe_drinking_water_fee
    if (current_amt - start_amt) > 3:
        total_bill = total_bill + water_first_3 * 3
        total_bill = total_bill + (current_amt - start_amt - 3) * water_over_3
        total_bill = total_bill + sewer_charge * (current_amt - start_amt)
    else:
        total_bill = total_bill + water_first_3 * (current_amt - start_amt)
        total_bill = total_bill + sewer_charge * (current_amt - start_amt)
    # print(f"---{(time.process_time_ns() - start_time)} nanoseconds ---")
    return round(total_bill, 2)


def water_volume_charge(start_amt, current_amt, year, city_limits):
    """Return billed amount from starting current read and prior amount."""


def monthly_water_billed_by_gallon(start_amt, current_amt):
    start_time = time.process_time_ns()
    water_base = 10.830
    water_first_3 = 1.320
    water_over_3 = 2.630
    sewer_charge = 9.010
    garbage_fee = 7
    recycling_fee = 2.5
    safe_drinking_water_fee = 1.000
    security_fee = 0.500
    total_bill = water_base + sewer_charge + garbage_fee + security_fee
    total_bill = total_bill + recycling_fee + safe_drinking_water_fee
    if (current_amt - start_amt) > 3000:
        first_3k_water = water_first_3 * 3
        total_bill = total_bill + first_3k_water
        total_bill = total_bill + (current_amt - start_amt - 3000) / 1000 * water_over_3
        total_bill = total_bill + sewer_charge * (current_amt - start_amt) / 1000
    else:
        total_bill = total_bill + water_first_3 * (current_amt - start_amt) / 1000
        total_bill = total_bill + sewer_charge * (current_amt - start_amt) / 1000
    print(f"---{(time.process_time_ns() - start_time)} nanoseconds ---")
    return round(total_bill, 2)


print(monthly_water_bill(1432, 1437))
print(monthly_water_billed_by_gallon(1432000, 1437000))

print(round(monthly_water_bill(1432, 1437) - monthly_water_billed_by_gallon(1432000, 1436500), 2))

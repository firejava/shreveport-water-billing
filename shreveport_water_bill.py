"""Explore Shreveport water billing."""
import time


garbage_fee = 7.000
recycling_fee = 2.500
safe_drinking_water_fee = 1.000
security_fee = 0.500

tier1_2019 = 1.320
teir2_2019 = 2.630
tier3_2019 = 3.950
tier4_2019 = 4.470
commercial = 3.020
industrial = 3.020

meter_size_5_8_2019 = 7.540
meter_size_1_2019 = 10.830

sewer_charge = 9.010
sewer_rate_per_1000 = 9.010

outside_tier1_2019 = 2.640
outside_teir2_2019 = 5.260
outside_tier3_2019 = 7.900
outside_tier4_2019 = 8.940
outside_commercial = 6.040
outside_industrial = 6.040

outside_meter_size_5_8_2019 = 15.080
# rate unknown
# outside_meter_size_1_2019 = 10.830

outside_sewer_charge = 18.020
outside_sewer_rate_per_1000 = 18.020


def monthly_water_bill(start_amt, current_amt, meter_size):
    """Return billed amount from starting current read and prior amount."""
    # start_time = time.process_time_ns()
    if meter_size == 5 / 8:
        water_base = meter_size_5_8_2019
    elif meter_size == 1:
        water_base = meter_size_1_2019
    else:
        water_base = meter_size_1_2019
    total_bill = water_base + sewer_charge + garbage_fee + security_fee
    total_bill = total_bill + recycling_fee + safe_drinking_water_fee
    volume = current_amt - start_amt
    total_bill = total_bill + shreveport_2019_water_volume_rate(volume)
    total_bill = total_bill + shreveport_2019_sewer_charge(volume)
    # print(f"---{(time.process_time_ns() - start_time)} nanoseconds ---")
    return round(total_bill, 2)


def shreveport_2019_water_volume_rate(volume_of_water):
    """Return billed amount for volume of water."""
    if volume_of_water > 14:
        total_volume_water_charge = (
            tier4_2019 * (volume_of_water - 14)
            + 7 * tier3_2019
            + 4 * teir2_2019
            + 3 * tier1_2019
        )
    elif volume_of_water > 7:
        total_volume_water_charge = (
            tier3_2019 * (volume_of_water - 7)
            + 4 * teir2_2019
            + 3 * tier1_2019
        )
    elif volume_of_water > 3:
        total_volume_water_charge = (
            teir2_2019 * (volume_of_water - 3) + 3 * tier1_2019
        )
    else:
        total_volume_water_charge = tier1_2019 * volume_of_water
    return total_volume_water_charge


def shreveport_2019_sewer_charge(volume_of_water):
    """Return billed sewer amount for volume of water."""
    total_sewer_charge = volume_of_water * sewer_rate_per_1000
    return total_sewer_charge


def monthly_water_billed_by_gallon(start_amt, current_amt):
    """Return billed amount from starting current read and prior amount."""
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
        total_bill = (
            total_bill + (current_amt - start_amt - 3000) / 1000 * water_over_3
        )
        total_bill = (
            total_bill + sewer_charge * (current_amt - start_amt) / 1000
        )
    else:
        total_bill = (
            total_bill + water_first_3 * (current_amt - start_amt) / 1000
        )
        total_bill = (
            total_bill + sewer_charge * (current_amt - start_amt) / 1000
        )
    print(f"---{(time.process_time_ns() - start_time)} nanoseconds ---")
    return round(total_bill, 2)


print(monthly_water_bill(1432, 1437, 1))
print(monthly_water_billed_by_gallon(1432000, 1437000))

print(
    round(
        monthly_water_bill(1432, 1437, 1)
        - monthly_water_billed_by_gallon(1432000, 1436500),
        2,
    )
)

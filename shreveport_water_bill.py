"""Explore Shreveport water billing."""
import time


garbage_fee = 7.000
recycling_fee = 2.500
safe_drinking_water_fee = 1.000

#(Ord. No. 186, 2002, 11-26-02)
security_fee = 0.500

tier1_2019 = 1.320
teir2_2019 = 2.630
tier3_2019 = 3.950
tier4_2019 = 4.470
commercial = 3.020
industrial = 3.020

#Sec. 94-164. - Monthly water customer charge
#inside city water fees
#effective Oct 1, 2013 to Jan 31, 2015
meter_size_5_8_2013 = 4.80
meter_size_3_4_2013 = 5.53
meter_size_1_2013 = 6.24
meter_size_1_1_2_2013 = 9.98
meter_size_2_2013 = 14.06
meter_size_3_2013 = 29.87
meter_size_4_2013 = 51.65
meter_size_6_2013 = 101.69
meter_size_8_2013 = 151.69
meter_size_10_2013 = 205.77

#Sec. 94-164. - Monthly water customer charge
#inside city water fees
#effective Feb 1, 2015 to Dec 31, 2015
meter_size_5_8_2015 = 6.540
meter_size_3_4_2015 = 7.490
meter_size_1_2015 = 9.390
meter_size_1_1_2_2015 = 14.140
meter_size_2_2015 = 19.830
meter_size_3_2015 = 33.130
meter_size_4_2015 = 52.120
meter_size_6_2015 = 99.59
meter_size_8_2015 = 156.57
meter_size_10_2015 = 223.03


#Sec. 94-164. - Monthly water customer charge
#inside city water fees
#effective Jan 1, 2016 to Dec 31, 2019
meter_size_5_8_2016 = 7.540
meter_size_3_4_2016 = 8.640
meter_size_1_2016 = 10.830
meter_size_1_1_2_2016 = 16.300
meter_size_2_2016 = 22.860
meter_size_3_2016 = 38.200
meter_size_4_2016 = 60.090
meter_size_6_2016 = 114.820
meter_size_8_2016 = 180.510
meter_size_10_2016 = 257.130

#Sec. 94-164. - Monthly water customer charge
#inside city water fees
#effective Jan 1, 2020 to Dec 31, 2021
meter_size_5_8_2020 = 8.540
meter_size_3_4_2020 = 9.780
meter_size_1_2020 = 12.260
meter_size_1_1_2_2020 = 18.46
meter_size_2_2020 = 25.89
meter_size_3_2020 = 43.26
meter_size_4_2020 = 68.06
meter_size_6_2020 = 130.050
meter_size_8_2020 = 204.45
meter_size_10_2020 = 291.23

#Sec. 94-164. - Monthly water customer charge
#inside city water fees
#effective Jan 1, 2022
meter_size_5_8_2022 = 9.450
meter_size_3_4_2022 = 10.93
meter_size_1_2022 = 13.700
meter_size_1_1_2_2022 = 20.630
meter_size_2_2022 = 28.930
meter_size_3_2022 = 48.330
meter_size_4_2022 = 76.030
meter_size_6_2022 = 145.270
meter_size_8_2022 = 228.39
meter_size_10_2022 = 325.34


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
        water_base = meter_size_5_8_2016
    elif meter_size == 1:
        water_base = meter_size_1_2016
    else:
        water_base = meter_size_1_2016
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

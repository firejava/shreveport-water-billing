"""Explore Shreveport water billing."""
import time
import datetime

garbage_fee = 7.000
recycling_fee = 2.500
safe_drinking_water_fee = 1.000

# (Ord. No. 186, 2002, 11-26-02)
security_fee = 0.500

tier1_2019 = 1.320
teir2_2019 = 2.630
tier3_2019 = 3.950
tier4_2019 = 4.470
commercial = 3.020
industrial = 3.020

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


def monthly_water_bill(start_amt, current_amt, meter_sizes, bill_date):
    """Return billed amount from starting current read and prior amount."""
    # start_time = time.process_time_ns()
    water_base = shreveport_meter_charge(meter_sizes, bill_date)

    total_bill = water_base + sewer_charge + garbage_fee + security_fee
    total_bill = total_bill + recycling_fee + safe_drinking_water_fee
    volume = current_amt - start_amt
    total_bill = total_bill + shreveport_2019_water_volume_rate(volume)
    total_bill = total_bill + shreveport_2019_sewer_charge(volume)
    # print(f"---{(time.process_time_ns() - start_time)} nanoseconds ---")
    return round(total_bill, 2)


def shreveport_meter_charge(meters, bill_date):
    # rate chanages in dates in yyyy/mm/dd format
    d1 = datetime.datetime(2013, 10, 1)
    d2 = datetime.datetime(2015, 2, 1)
    d3 = datetime.datetime(2016, 1, 1)
    d4 = datetime.datetime(2020, 1, 1)
    d5 = datetime.datetime(2022, 1, 1)
    result_individual_meters = []
    if bill_date > d5:
        meter_rates_2022 = [
            9.450,
            10.93,
            13.700,
            20.630,
            28.930,
            48.330,
            76.030,
            145.270,
            228.39,
            325.34,
        ]
        if len(meter_rates_2022) == len(meters):
            for i in range(0, len(meter_rates_2022)):
                result_individual_meters.append(
                    meter_rates_2022[i] * meters[i]
                )
        else:
            raise Exception("Meter array not equal to rate array length")
    elif bill_date > d4:
        meter_rates_2020 = [
            8.540,
            9.780,
            12.260,
            18.46,
            25.89,
            43.26,
            68.06,
            130.050,
            204.45,
            291.23,
        ]
        if len(meter_rates_2020) == len(meters):
            for i in range(0, len(meter_rates_2020)):
                result_individual_meters.append(
                    meter_rates_2020[i] * meters[i]
                )
        else:
            raise Exception("Meter array not equal to rate array length")
    elif bill_date > d3:
        # focus on this
        meter_rates_2016 = [
            7.540,
            8.640,
            10.830,
            16.300,
            22.860,
            38.200,
            60.090,
            114.820,
            180.510,
            257.130,
        ]
        if len(meter_rates_2016) == len(meters):
            for i in range(0, len(meter_rates_2016)):
                result_individual_meters.append(
                    meter_rates_2016[i] * meters[i]
                )
        else:
            raise Exception("Meter array not equal to rate array length")

    elif bill_date > d2:
        meter_rates_2015 = [
            6.540,
            7.490,
            9.390,
            14.140,
            19.830,
            33.130,
            52.120,
            99.59,
            156.57,
            223.03,
        ]
        if len(meter_rates_2015) == len(meters):
            for i in range(0, len(meter_rates_2015)):
                result_individual_meters.append(
                    meter_rates_2015[i] * meters[i]
                )
        else:
            raise Exception("Meter array not equal to rate array length")
    elif bill_date > d1:
        meter_rates_2013 = [
            4.80,
            5.53,
            6.24,
            9.98,
            14.06,
            29.87,
            51.65,
            101.69,
            151.69,
            205.77,
        ]
        if len(meter_rates_2013) == len(meters):
            for i in range(0, len(meter_rates_2013)):
                result_individual_meters.append(
                    meter_rates_2013[i] * meters[i]
                )
        else:
            raise Exception("Meter array not equal to rate array length")
    else:
        raise Exception("Bill date should be after Oct. 10, 2013")

    base_charge_for_water_meter_size = sum(result_individual_meters)
    return round(base_charge_for_water_meter_size, 2)


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


date_example = datetime.datetime(2019, 10, 1)
date_example2 = datetime.datetime(2020, 10, 1)
date_example3 = datetime.datetime(2021, 10, 1)
date_example4 = datetime.datetime(2022, 10, 1)

print(
    monthly_water_bill(
        1432, 1437, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], date_example
    )
)
print(monthly_water_billed_by_gallon(1432000, 1437000))

print(
    round(
        monthly_water_bill(
            1432, 1437, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], date_example
        )
        - monthly_water_billed_by_gallon(1432000, 1436500),
        2,
    )
)

print("Water Bill in 2020")
print(
    monthly_water_bill(
        1432, 1437, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], date_example2
    )
)
print("Water Bill in 2021")
print(
    monthly_water_bill(
        1432, 1437, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], date_example3
    )
)
print("Water Bill in 2022")
print(
    monthly_water_bill(
        1432, 1437, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], date_example4
    )
)

import pytest  # noqa
import sys
import datetime
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")
from shreveport_water_bill import monthly_water_bill
from shreveport_water_bill import shreveport_2019_water_volume_rate
from shreveport_water_bill import shreveport_2019_sewer_charge


def test_monthly_water_bill():
    d1 = datetime.datetime(2019, 10, 1)
    d2 = datetime.datetime(2020, 10, 1)
    d3 = datetime.datetime(2022, 10, 1) 
    water_meters1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    water_meters2 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    assert monthly_water_bill(1432, 1437, water_meters2, d1) == 85.11
    assert monthly_water_bill(1437, 1443, water_meters2, d1) == 96.75
    assert monthly_water_bill(0, 5, water_meters2, d2) == 86.54
    assert monthly_water_bill(0, 5, water_meters2, d3) == 87.98
    assert monthly_water_bill(1, 2, water_meters1, d1) == 37.88


def test_shreveport_2019_water_volume_rate():
    assert shreveport_2019_water_volume_rate(5) == 3.96 + 5.26
    assert shreveport_2019_water_volume_rate(1) == 1.32


def test_shreveport_2019_sewer_charge():
    assert shreveport_2019_sewer_charge(5) == 45.05
    assert shreveport_2019_sewer_charge(1) == 9.01

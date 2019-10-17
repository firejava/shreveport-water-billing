import pytest # noqa
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")
from shreveport_water_bill import monthly_water_bill
from shreveport_water_bill import shreveport_2019_water_volume_rate
from shreveport_water_bill import shreveport_2019_sewer_charge


def test_monthly_water_bill():
    assert monthly_water_bill(1432, 1437, 1) == 85.11
    assert monthly_water_bill(1437, 1443, 1) == 96.75
    assert monthly_water_bill(1, 2, 5 / 8) == 37.88


def test_shreveport_2019_water_volume_rate():
    assert shreveport_2019_water_volume_rate(5) == 3.96 + 5.26
    assert shreveport_2019_water_volume_rate(1) == 1.32


def test_shreveport_2019_sewer_charge():
    assert shreveport_2019_sewer_charge(5) == 45.05
    assert shreveport_2019_sewer_charge(1) == 9.01

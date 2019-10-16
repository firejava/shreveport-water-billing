import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from shreveport_water_bill import monthly_water_bill


def test_monthly_water_bill():
    assert monthly_water_bill(1432, 1437) == 85.11
    assert monthly_water_bill(1437, 1443) == 96.75

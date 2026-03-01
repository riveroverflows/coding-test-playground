import json
from typing import *


def containsDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


nums = json.loads(input())
print(containsDuplicate(nums))

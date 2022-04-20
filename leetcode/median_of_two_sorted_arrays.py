from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    standard library
    Runtime: 158 ms
    Memory Usage: 14.1 MB
    :param nums1:
    :param nums2:
    :return:
    """
    import statistics
    return statistics.median(nums1 + nums2)
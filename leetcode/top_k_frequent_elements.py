from collections import Counter

def topKFrequent_low_memory(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    solution = []

    sorted_unique_values = sorted(set(nums))
    count_of_values = []
    for value in sorted_unique_values:
        count_of_value = nums.count(value)
        count_of_values.append(count_of_value)

    for i in range(k):
        print(f'count of values: {count_of_values}')
        print(f'sorted unique values: {sorted_unique_values}')
        highest_occurance = count_of_values.index(max(count_of_values))
        del count_of_values[highest_occurance]
        solution.append(sorted_unique_values[highest_occurance])
        del sorted_unique_values[highest_occurance]

    return solution


def topKFrequent(nums, k):
    frequency = Counter(nums)
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return [frequency[0] for frequency in sorted_frequency[:k]]

if __name__ == '__main__':
    input_arr = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6, 10]
    k = 10
    print(topKFrequent(input_arr, k))
class Solution_Brute_force:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        n = len(arr)
        count = 0

        # Generate all possible subarrays
        for start_index in range(n):
            current_sum = 0
            # Iterate through each subarray starting at start_index
            for end_index in range(start_index, n):
                current_sum += arr[end_index]
                # Check if the sum is odd
                if current_sum % 2 != 0:
                    count += 1

        return int(count % MOD)

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        n = len(arr)

        # Convert elements to 0 (even) or 1 (odd)
        for i in range(n):
            arr[i] %= 2

        # dp_even[i] represents the number of subarrays with an even sum ending
        # at index i. dp_odd[i] represents the number of subarrays with an odd
        # sum ending at index i
        dp_even, dp_odd = [0] * n, [0] * n

        # Initialization based on the last element
        # The last element is even
        if arr[n - 1] == 0:
            dp_even[n - 1] = 1
        else:
            # The last element is odd
            dp_odd[n - 1] = 1

        # Traverse the array in reverse
        for num in range(n - 2, -1, -1):
            if arr[num] == 1:
                # Odd element contributes to odd subarrays
                dp_odd[num] = (1 + dp_even[num + 1]) % MOD
                # Even element continues the pattern
                dp_even[num] = dp_odd[num + 1]
            else:
                # Even element contributes to even subarrays
                dp_even[num] = (1 + dp_even[num + 1]) % MOD
                # Odd element continues the pattern
                dp_odd[num] = dp_odd[num + 1]

        # Sum all the odd subarrays
        count = 0
        for odd_count in dp_odd:
            count += odd_count
            count %= MOD

        return int(count)

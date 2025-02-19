# https://leetcode.com/problems/construct-smallest-number-from-di-string/
class Solution2:
    def smallestNumber2(self, pattern: str) -> str:
        self.result = []

        # Start building the sequence by calling the helper function
        self.build_sequence(0, 0, pattern)
        # Reverse the final result
        return "".join(self.result[::-1])

    # Recursively build the sequence
    def build_sequence(
        self, current_index: int, current_count: int, pattern: str
    ) -> int:
        if current_index != len(pattern):
            if pattern[current_index] == "I":
                # If 'I', increment the count and move to the next index
                self.build_sequence(
                    current_index + 1, current_index + 1, pattern
                )
            else:
                # If 'D', keep the count and move to the next index
                current_count = self.build_sequence(
                    current_index + 1, current_count, pattern
                )

        self.result.append(str(current_count + 1))

        # Return the next count for the sequence
        return current_count + 1

# Brute force
class Solution:
    def check(self, number_sequence:str, pattern:str)-> bool:
        for index in range(len(pattern)):
            if (
                pattern[index] == "I"
                and number_sequence[index] > number_sequence[index+1] 
                ):
                return False
            elif (
                pattern[index] == "D"
                and number_sequence[index] < number_sequence[index +1]
                ):
                return False
        return True

    def smallestNumber(self, pattern:str)->str:
        pattern_length = len(pattern)

        number_sequences = "".join(str(num) for num in range(1, pattern_length+2))

        for permutation in permutations(number_sequences):
            permutation_str = "".join(permutation)
            if self.check(permutation_str, pattern):
                return permutation_str
        
        return ""
        

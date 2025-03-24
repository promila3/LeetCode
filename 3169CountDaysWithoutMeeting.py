# https://leetcode.com/problems/count-days-without-meetings/description/?envType=daily-question&envId=2025-03-24
# O n lg n , o n 
from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start day
        meetings.sort(key=lambda x: x[0])
        
        merged_meetings = []
        
        for meeting in meetings:
            if not merged_meetings or merged_meetings[-1][1] < meeting[0] - 1:
                merged_meetings.append(meeting)
            else:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], meeting[1])
        
        meet_days = 0
        for meeting in merged_meetings:
            meet_days += meeting[1] - meeting[0] + 1
        
        return days - meet_days

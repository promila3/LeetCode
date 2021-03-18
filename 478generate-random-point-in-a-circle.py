#https://leetcode.com/problems/generate-random-point-in-a-circle/
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def randPoint(self) -> List[float]:
        while True:
            x1 = random.uniform(self.x_center-self.radius, self.x_center+self.radius)
            y1 = random.uniform(self.y_center-self.radius, self.y_center+self.radius)
            dist = ((x1 - self.x_center) ** 2 + (y1 - self.y_center) ** 2) ** 0.5
            if dist <= self.radius:
                break
        return [x1,y1 ]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    def __add__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        total_height_inches = height_A_inches + height_B_inches

        output_feet = total_height_inches // 12

        output_inches = total_height_inches - (output_feet * 12)

        return Height(output_feet, output_inches)
    
    def __sub__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        subtract_height_inches = height_A_inches - height_B_inches

        output_feet = subtract_height_inches // 12

        output_inches = subtract_height_inches - (output_feet * 12)

        return Height(output_feet, output_inches)
    
    def __lt__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        return height_A_inches < height_B_inches
    
    def __le__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        return height_A_inches <= height_B_inches
    
    def __eq__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        return height_A_inches == height_B_inches
    
    def __gt__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        return height_A_inches > height_B_inches
    
    def __ge__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        return height_A_inches >= height_B_inches
    
    def __ne__(self, other):   
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches
        return height_A_inches != height_B_inches

print(Height(4, 6) > Height(4, 5))
print("-----------------------------")
print(Height(4, 5) >= Height(4, 5))
print("-----------------------------")
print(Height(5, 9) != Height(5, 10))

height_1 = Height(4, 10)
height_2 = Height(5, 6)
height_3 = Height(7, 1)
height_4 = Height(5, 5)
height_5 = Height(6, 7)
height_6 = Height(5, 6)

heights = [height_1, height_2, height_3, height_4, height_5, height_6]

heights = sorted(heights)
for height in heights:
    print(height)
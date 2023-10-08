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
    
person_C_height = Height(3, 9)
person_D_height = Height(5, 10)
height_sub = person_D_height - person_C_height

print("Subtracted height:", height_sub)
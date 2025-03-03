import math;

def main():
    print("Hypotenuse Calculator")
    try:
        # Prompt the user for the lengths of the two legs
        side1 = float(input("Enter Side 1: "))
        side2 = float(input("Enter Side 2: "))
        
        # Calculate the hypotenuse using the Pythagorean theorem
        hypotenuse = math.sqrt(side1**2 + side2**2)
        
        # Display the result
        print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
    except ValueError:
        print("Invalid input. Please enter numerical values for the lengths.")

if __name__ == "__main__":
    main()
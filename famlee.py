def calculate_triangle_area():
    try:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the perpendicular height of the triangle: "))
        
        if base <= 0 or height <= 0:
            print("Base and height must be positive numbers.")
            return
        
        area = 0.5 * base * height
        print(f"The area of the triangle is: {area:.2f}")
    
    except ValueError:
        print("Please enter valid numerical values.")

# Call the function
calculate_triangle_area()

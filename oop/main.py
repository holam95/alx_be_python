
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    # Create a list of shapes (Rectangle and Circle)
    shapes = [
        Rectangle(10, 5),  # Rectangle with length 10 and width 5
        Circle(7)          # Circle with radius 7
    ]

    # Loop through each shape and print its class name and area
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area():.2f}")

if __name__ == "__main__":
    main()

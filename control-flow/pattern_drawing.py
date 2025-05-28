# pattern_drawing.py

def main():
    size = int(input("Enter the size of the pattern: "))
    
    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")
        print()  # Move to next line after each row
        row += 1

if __name__ == "__main__":
    main()

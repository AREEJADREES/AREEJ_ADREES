import streamlit as st
import math

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, root
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

def main():
    st.title("Quadratic Equation Solver")

    a = st.number_input("Enter the value of a:", step=0.1)
    b = st.number_input("Enter the value of b:", step=0.1)
    c = st.number_input("Enter the value of c:", step=0.1)

    if st.button("Calculate Roots"):
        root1, root2 = quadratic_roots(a, b, c)
        st.success(f"Root 1: {root1}, Root 2: {root2}")

if __name__ == "__main__":
    main()

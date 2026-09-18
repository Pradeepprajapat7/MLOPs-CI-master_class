import streamlit as st


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


def fifth_power(n):
    return n ** 5


st.title("Power Calculator")
st.write("This app calculates the power of a number given a base and an exponent.")

n = st.number_input("Enter the base (n):", value=2, step=1)

square_result = square(n)
cube_result = cube(n)
fifth_power_result = fifth_power(n)

st.write(f"The square of {n} is: {square_result}")
st.write(f"The cube of {n} is: {cube_result}")
st.write(f"The fifth power of {n} is: {fifth_power_result}")
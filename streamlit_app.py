import streamlit
streamlit.title("My mom's new healthy Diner")
streamlit.header('Breakfast favorites')
streamlit.text(' 🥣 cereal')
streamlit.text(' 🥗 spinach')
streamlit.text(' 🥑🍞chai')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

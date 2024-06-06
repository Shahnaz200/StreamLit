#import streamlit as st
#st.header("st.button")

#if st.button("Say hello"):
    # st.write("Why hello there")
#else:
    # st.write("Goodbye")
     
     
     
     
     
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header("st.write")  
st.write("hello sreamlit")

#dict = {"raw":"1", "column": "1"}
#st.write(dict)

#df = pd.DataFrame({})

#st.write(df)   
#Create an Altair Chart: Use alt.Chart to create a scatter plot (mark_circle()) with the columns of dfmapped to different visual properties such as x, y, size, and color. Add tooltips to show data values on hover.
#Display the Altair Chart: Use st.write to display the created Altair chart.

df = pd.DataFrame(
     np.random.randn(5, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)



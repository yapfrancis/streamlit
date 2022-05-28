# Author: Prakash Sukhwal
# Aug 2021

import streamlit as st
# other libs
import numpy as np
import pandas as pd

# -- Set page config
apptitle = 'Solution Implementation'
st.set_page_config(page_title=apptitle, page_icon='random',	layout= 'wide', 
	initial_sidebar_state="expanded")
# random icons in the browser tab

# give a title to your app
st.title('Bank Loans')
st.balloons() 

# Let's add a sub-title
st.write("A loan application assessment app")
st.success("It is working!!")

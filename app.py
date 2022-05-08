import streamlit as st
from multiapp import MultiApp
from apps import home, parkinsonswebapp, diabetespredectionwebapp ,diabetes2 ,heartwebapp,mdpwebapp,bc,cardio# import your app modules here

app = MultiApp()

st.markdown("""

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Start  Checkup", mdpwebapp.main)
app.add_app("breast cancer classification", bc.main)
app.add_app("parkinson's  disease  prediction", parkinsonswebapp.main1)
app.add_app("diabetes  disease  prediction", diabetespredectionwebapp.main)
app.add_app("diabetes2",diabetes2.main)
app.add_app("heart disease", heartwebapp.main)
app.add_app("cardiovascular disease", cardio.main)



# The main app
app.run()

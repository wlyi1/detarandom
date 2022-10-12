import streamlit as st
import pandas as pd
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
from datetime import datetime as dt
from deta import Deta
import pandas as pd


#Data Sources
data = pd.read_csv('rand_aktivitas.csv')
image1 = Image.open('a2.png')
image2 = Image.open('a3a.png')
image3 = Image.open('dw.png')

st.image(image1)
st.image(image2)

list_rand = data.name
tgl_random = datetime.datetime.now()
today_rand = random.choice(list_rand)
path_font = "Quicksand-Regular.ttf"
path_font_2 = 'Quicksand-Bold.ttf'
font = ImageFont.truetype(path_font, 55)
font1 = ImageFont.truetype(path_font_2, 28)

img= ImageDraw.Draw(image3)
img.text((80,470), today_rand, font=font, fill=(0,0,0))
img.text((450,390), hari, font=font1, fill=(0,0,0))


# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["project_key"])

# Create a new database "example-db sss"
# If you need a new database, just use another name.
db = deta.Base("random1")

if st.button('Show'):
    st.image(image3)
    db.put({'name' : today_rand, 'age' : 90})

# Data to be written to Deta Base
with st.form("form"):
    name = st.text_input("Your name")
    age = st.number_input("Your age")
    submitted = st.form_submit_button("Store in database")


# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
if submitted:
    db.put({"name": name, "age": age})

st.write('Test Your Knowledge')
st.write('Test number 2')
st.write('test 3 commited')
st.wrtie('test 4 commit')
st.write('test 5 git command')
st.write('test66')
st.wrtie('susah amat sss')
st.write('buset')

"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items
st.write(db_content)
df = pd.DataFrame(db_content)
st.dataframe(df)



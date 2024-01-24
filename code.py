import streamlit as st
html, css, javascript, more = steamlit.tabs(["html","css","javascript", "more"])
with html:
  st.header("Types of text and stuff")
  st.code("<h1></h1> to <h5></h5> (bigger text to smaller text)")
  st.code("<p></p> is a paragraph text (automatecaly starts at a new line (<br>)")
  st.code("<pre></pre> is a paragraph text but it keeps its format")
  st.code("<a></a> is used to make a link")
  "Example:"
  st.code('<a href="https://www.yourlink.com" target="_none"(_none or _parent) title="This will pop up when your cursor is on the link">this is the name of the link</a>')
  "P.S: where it states the name of the link, you can add an image there so that if you click the image, it will send you to the link!"
  st.code("<img> is for an image")
  "Example:"
  st.code('<img src="yourimage.jpg" width="400" height="500 type="image/jpg">')
  st.code('<audio></audio> is used for audio')
  st.code('<audio controls(control stuff like volume) muted(volume is 0%) autoplay(plays automatically) loop(loops when finished)><source src="youraudio.mp3" type="audio/mpeg"></audio>')
  st.code('<video></video> is playing a video(has the same controls as audio and img)')
  "Example:"
  st.code('<video src="videoplaying.mp4" controls></video>')
with css:
st.header("What to do")
"Make a file and end it with a .css"
"Example"
image.load("Screenshot 2024-01-23 at 7.46.51 PM.png")
"Or use style in text"
mage
st.header("Highlight")

with javascript:
st.header("Not available yet")
  

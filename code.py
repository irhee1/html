import streamlit as st
html, css, javascript, more = st.tabs(["html","css","javascript", "more"])
with html:
  st.header("Format of an html")
  st.code('<html>')
  st.code('  <head>')
  st.code('  </head>')
  st.code('  <body>')
  st.code('  </body>')
  st.code('</html>')
  st.header("Types of text and stuff")
  "---"
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
  "Make a file and end it with a .css (option 1)"
  "Example"
  st.image("Screenshot 2024-01-23 at 7.44.54 PM.png")
  "Or use style in text (option 2)"
  st.image("Screenshot 2024-01-23 at 7.46.51 PM.png")
  st.header("Option 1")
  st.subheader("Add css")
  "in the body write this"
  "<head>"
  '<link rel="stylesheet" href="(name of .css).css">'
  "<head>"
  st.subheader("Edit body of html")
  "---"
  st.code("body{")
  st.code('margin: 0px(distance of text and images on ALL sides')
  st.code('background-color: (colors[example:tomato;] or rgb[example:rgb(0, 0, 0)]')
  st.code('border: 3px(wide) solid(types of borders:solid, dashed, dotted, double, groove, ridge, inset, outset, none)')
  st.code("display:flow-root(so images don't get out of the border)")
  st.code("}")
  st.subheader("Edit text like <p></p> or <h1></h1>")
  st.code('p{')
  st.code('color:color of the font')
  st.code('font-family: (types of fonts[example:"lucida console or "courier new"])')
  st.code('font-weight: bold')
  st.code('font-size: 50px')
  st.code('font-style:(styles[example:italic])')
  st.code('border: 3px border(look at body border(same idea)) rgb(100, 100, 100)(color of the border)')
  st.code('you can also do it in border-top and left and right and bottom')
  "Example:"
  st.code('border-top: 3px solid rgb(255, 255, 255);')
  st.code('border-left: 3px dotted rgb(0, 255, 0);')
  st.code('border-right: 3px dotted rgb(0, 255, 0);')
  st.code('border-bottom: 3px solid rgb(255, 255, 255);')
  st.code('border-radius: (how curvy the border is[example: 25px])')
  st.code('}')
  st.subheader("use id and classes")
  st.code('use #nameid for id="id"')
  "Example:"
  st.code('<p id="name"></p>')
  "In .Css file"
  st.code("#name{}")
  st.code('use .nameclass for class="class')
  "Example:"
  st.code('<p class="name"></p>')
  "In .Css file"
  st.code(".name{}")
  "Ps. make sure to know id can only be used once while class can be used multiple times"
  "Also you can use class and id at the SAME TIME"
  st.subheader("Make a shadow")
  "write this in html BODY!"
  st.code('<h1 id="addashadow">Text</h1>')
  "In .Css"
  st.code("#addashadow{text-shadow: px px px namecolor or rgb, ...(this process can be used multiple times}")
  "Make sure to write ; at the end of each"
with javascript:
  st.header("Not available yet")
with more:
  st.header("Not availiable yet")
  

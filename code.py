import streamlit as st
st.set_page_config(layout="wide")
html, css, javascript, more = st.tabs(["html","css","javascript", "more"])
with html:
  st.header("Format of an html")
  st.code("Type this to get the format: !(tab)")
  "If it doesn't work:"
  st.code('<html>')
  st.code('  <head>')
  st.code('  </head>')
  st.code('  <body>')
  st.code('  </body>')
  st.code('</html>')
  "write this to name you website(in head)"
  st.code('<title>NameofWeb</title>')
  st.header("Types of text and stuff")
  "---"
  st.code("<h1></h1> to <h5></h5> (bigger text to smaller text)")
  st.code("<p></p> is a paragraph text (automatecaly starts at a new line (<br>)")
  st.code("<pre></pre> is a paragraph text but it keeps its format")
  st.code("<hr> is used to make a line")
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
  "Make a simple and advanced list"
  st.code("<ul></ul> and <li></li> is for a list")
  "Example"
  st.code("<ul>")
  st.code('(tab) <li>Something<li>')
  st.code('<ul>')
  st.code('''
  <dl></dl>, <dt></dt>, and <dd></dd> can be used to also make a list
  \n#Example:
  \n<dl>
  \n<dt>topic</dt>
  \n<dd>facts facts factz</dd>
  \n</dl>
  ''')
  st.code('<button></buttton> is for a button')
  "Example:"
  st.code('<button>Name of this button</button>')
  "label"
  st.code('''
  <label></label> is use to help format inputs
  \n3Example:
  \n<label for="nameforid">something</label>
  ''')
  "Input"
  st.code('''
  <input> is for inputs
  \n#make sure to create a label
  \nExample:
  \n<input type=(types[text, reset, submit, password, email, tel, number, date, checkbox]) id="nameforyourid">
  ''')
  
with css:
  st.header("What to do")
  "Make a file and end it with a .css (option 1)"
  "Example"
  st.image("Screenshot 2024-01-23 at 7.44.54 PM.png")
  "Or use style in text (option 2)"
  st.image("Screenshot 2024-01-23 at 7.46.51 PM.png")
  st.header("Option 1")
  st.subheader("Add css")
  "in the head write this"
  "<head>"
  '<link rel="stylesheet" href="(name of .css).css">'
  "<head>"
  st.subheader("Edit body of html")
  "---"
  st.code("body{")
  st.code('margin: 0px(distance of text and images on ALL sides(you can use margin left, right, up, and down));')
  st.code('background-color: (colors[example:tomato;] or rgb[example:rgb(0, 0, 0);]')
  st.code('border: 3px(wide) solid(types of borders:solid, dashed, dotted, double, groove, ridge, inset, outset, none);')
  st.code("display:flow-root(so images don't get out of the border);")
  st.code("}")
  st.subheader("Edit text like <p></p> or <h1></h1>")
  st.code('p{')
  st.code('color:color of the font')
  st.code('font-family: (types of fonts[example:"lucida console"; or "courier new";])')
  st.code('font-weight: bold;')
  st.code('font-size: 50px;')
  st.code('font-style:(styles[example:italic;])')
  st.code('border: 3px border_name(look at body border(same idea)) rgb(100, 100, 100)(color of the border);')
  st.code('#you can also do it in border-top and left and right and bottom')
  "Example:"
  st.code('border-top: 3px solid rgb(255, 255, 255);')
  st.code('border-left: 3px dotted rgb(0, 255, 0);')
  st.code('border-right: 3px dotted rgb(0, 255, 0);')
  st.code('border-bottom: 3px solid rgb(255, 255, 255);')
  st.code('border-radius: (how curvy the border is[example: 25px]);')
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
  "Add css to a button"
  st.code('button{')
  st.code('font-size:px;')
  st.code('background-color:namecolor or rgbcolor;')
  st.code('color:coloragain;')
  st.code('border-raduis:px(how curvy it is)')
  st.code('}')
  "How to make a box"
  st.code('<div id="name"></div>')
  'In .Css file'
  st.code('.name{')
  st.code('width: px')
  st.code('height: px')
  st.code('background-color: color')
  st.code('box-shadow:px px px')
  st.code("}")
  'overflow (connect to a div or span)'
  st.code(''' #box{
  \nborder: 2px solid;
  \nheight: 100px;
  \noverflow: (visible:shows text, hidden:content that you don't see is hidden, scroll:shows a scroll, auto: shows a scroll if it's needed)
  \n}
  ''')
  '<div></div> and <span></span>:'
  st.code('''
  #div highlights a block while span only highlights unless you add (display: block;) to span{} 
  \n#You can also do (display:inline) to make it so that the text is in other lines of text(no width and height)
  \n#If you want the width and height included (display: incline-block)
  ''')
  "use float and margin to position your img and text"
  "example:"
  st.code('''
  #MARGIN
  p{
  margin: px or auto(makes it stuck in the middle);
  or
  margin-left: px or auto(makes it stuck in the left side);
  margin-right: px or auto(makes it stuck in the right side);
  margin-top: px;
  margin-bottom: px;
  #FLOAT
  img{
  float:left(puts image to the left) or right(puts image to the right);
  }
  ''')
  "edit box:"
  st.code('''Add padding: px; if you want there to be a distance between the letters and the border
  \nAdd box-sizing: border-box; if you want two boxes in the same row using float:left; or float:right;
  \nAdd text-align: center; to put the text right in the middle
  \nwrite in height: 100vh; if you want bg-color to take up all the space of the page
  \n if you write the thing above and write in min-height: 50%;, the boxes will take 50% of the page''')
  "Image as a background!"
  st.code('''
  body{
  \nbackground-image: url(background.png);
  \nbackground-repeat: no-repeat;
  \nbackground-position: center;
  \nbackground-attachment: fixed;
  \nbackground-size: cover;
  ''')
  "Make sure to write ; at the end of each"
with javascript:
  st.header("Add javascript")
  "Step 1: make a .js file"
  "Step 2: type this line to the body of the html to run the javascript"
  st.code('<script src="nameofyourjs.js"></script>')
  st.header("Beginner Javascript")
  'variables:'
  st.code('let num = 10(int) or "happy"(str) or True(boolean);')
  'or'
  st.code('let num;')
  st.code('num = value;')
  'write values'
  st.code('console.log("This will appear in the console");')
  st.code('document.write("This will show on the website")')
  st.code('alert("This will make an alert")')
  'input'
  st.code('let ask-the-user=prompt("I think im asking the user! ")')
  'if statements'
  st.code('if ([string or int] [== or > or <] "something"){')
  st.code('(tab) something()')
  st.code('}')
  'else if and elif:'
  st.code('(else if (str > 20){}) and else{}')
  'while loop'
  st.code('while (condition){do something}')
  'random number'
  st.code('let random-number = Math.floor(Math.random() * max (if only ); is after it, max-1) + min')
  'function'
  st.code('function nameoffunction{next line}')
  "document.getElementById('')"
  st.code('use document.getElementById().onclick = function for buttons or input')
  "Example"
  st.code('''
  #in html file
  \n<button id="idname">name</button>
  \n#in css file
  \ndocument.getElementById().onclick = function(){stuff} or nameoffunction()
  ''')
  st.code('''use variable = document.getElementById().value to get the stuff from a html input
  \n#Example (in html file):
  \n<label for="idname">Type something</label>
  \n<input type="text" id="idname">
  \n(in .js):
  \nlet text = document.getElementById("idname").value;
  ''')
  'p.s: list is same as python, except you need a #let'
  "p.s: make sure to add ; to the end of every line of code unless it is a if statement or a while loop"
with more:
  'Write stuff in js using id'
  'Example:'
  "in the body"
  st.code('<p id="selected-id"></p>')
  'make a .js file'
  'connect it to the html'
  st.code('<script src="nameofyourjs.js"></script>')
  'In the .js file:'
  st.code('document.getElementById("selected-id")[.innerHTML if replace or .textContent if new] = "Whatyouwanttowrite"')
  'button onclick'
  'in your html file'
  st.code('<button id ="name">name</button>')
  'in your js file'
  st.code('document.getElementById("name").onclick = function()')
  'make a table'
  st.code('''
  <table border="0-more" style="background-color:color;">
  \n<tr align="center style="background-color:color;">
  <th width="1-more">
  Stuff
  </th>
  ..repeat
  </tr>
  <tr(use same css used above)>
  <td>
  More stuff
  </td>
  </tr>
  ''')
  'favicon'
  'in head'
  st.code('<link rel="icon" type="image/jpg" href="imagename.jpg">')

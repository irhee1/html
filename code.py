import streamlit as st
st.set_page_config(layout="wide")
html, css, javascript= st.tabs(["html","css","javascript"])
with html:
  st.header("Format of an html")
  '---'
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
  st.code("""<h1></h1> to <h5></h5> (bigger text to smaller text)")
  \n<p></p> is a paragraph text (automatecaly starts at a new line (<br>)
  \n<pre></pre> is a paragraph text but it keeps its format
  \n<hr> is used to make a line
  \n<a></a> is used to make a link
  """)
  
  "Example:"
  st.code('<a href="https://www.yourlink.com" target="_none"(_none or _parent) title="This will pop up when your cursor is on the link">this is the name of the link</a>')
  "P.S: where it states the name of the link, you can add an image there so that if you click the image, it will send you to the link!"
  '---'
  'Add a favicon:'
  'In head'
  st.code('<link rel="icon" type="image/jpg" href="imagename.jpg">')
  '---'
  st.code("<img> is for an image")
  "Example:"
  st.code('<img src="yourimage.jpg" width="400" height="500 type="image/jpg">')
  '---'
  st.code('<audio></audio> is used for audio')
  st.code('<audio controls(control stuff like volume) muted(volume is 0%) autoplay(plays automatically) loop(loops when finished)><source src="youraudio.mp3" type="audio/mpeg"></audio>')
  '---'
  st.code('<video></video> is playing a video(has the same controls as audio and img)')
  "Example:"
  st.code('<video src="videoplaying.mp4" controls></video>')
  '---'
  "Make a simple and advanced list"
  st.code("<ul></ul> and <li></li> is for a list")
  "Example"
  st.code("<ul>")
  st.code('(tab) <li>Something<li>')
  st.code('<ul>')
  '---'
  'Advanced list:'
  st.code('''
  <dl></dl>, <dt></dt>, and <dd></dd> can be used to also make a list
  \n#Example:
  \n<dl>
  \n<dt>topic</dt>
  \n<dd>facts facts factz</dd>
  \n</dl>
  ''')
  '---'
  st.code('<button></buttton> is for a button')
  "Example:"
  st.code('<button>Name of this button</button>')
  '---'
  st.code('''
  <label></label> is use to help format inputs
  \n3Example:
  \n<label for="nameforid">something</label>
  ''')
  '---'
  'iframe is a web page on a website'
  st.code('''
  #Example:
  <iframe src="Website-name.com">
  ''')
  '---'
  "Input"
  st.code('''
  <input> is for inputs
  \n#make sure to create a label
  \nExample:
  \n<input type=(types[text, reset, submit, password, email, tel, number, date, checkbox]) id="nameforyourid">
  ''')
  '---'
with css:
  st.header("What to do")
  '---'
  "Make a file and end it with a .css (option 1)"
  "Example"
  st.image("Screenshot 2024-01-23 at 7.44.54 PM.png")
  "Or use style in text (option 2)"
  st.image("Screenshot 2024-01-23 at 7.46.51 PM.png")
  '---'
  st.header("Option 1")
  st.subheader("Add css")
  "in the head write this"
  "<head>"
  '<link rel="stylesheet" href="(name of .css).css">'
  "<head>"
  '---'
  st.subheader("Edit body of html")
  "---"
  st.code("body{")
  st.code('margin: 0px(distance of text and images on ALL sides(you can use margin left, right, up, and down));')
  st.code('background-color: (colors[example:tomato;] or rgb[example:rgb(0, 0, 0);]')
  st.code('border: 3px(wide) solid(types of borders:solid, dashed, dotted, double, groove, ridge, inset, outset, none);')
  st.code("display:flow-root(so images don't get out of the border);")
  st.code("}")
  '---'
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
  '---'
  st.subheader("use id and classes")
  st.code('use #nameid for id="id"')
  "Example:"
  st.code('<p id="name"></p>')
  "In .Css file"
  st.code("#name{}")
  st.code('use .nameclass for class="class')
  "Example:"
  st.code('<p class="name"></p>')
  '---'
  "In .Css file"
  st.code(".name{}")
  "Ps. make sure to know id can only be used once while class can be used multiple times"
  "Also you can use class and id at the SAME TIME"
  '---'
  st.subheader("Make a shadow")
  "write this in html BODY!"
  st.code('<h1 id="addashadow">Text</h1>')
  "In .Css"
  st.code("#addashadow{text-shadow: px px px namecolor or rgb, ...(this process can be used multiple times}")
  '---'
  "Add css to a button"
  st.code('button{')
  st.code('font-size:px;')
  st.code('background-color:namecolor or rgbcolor;')
  st.code('color:coloragain;')
  st.code('border-raduis:px(how curvy it is)')
  st.code('}')
  '---'
  "How to make a box"
  st.code('<div id="name"></div>')
  'In .Css file'
  st.code('.name{')
  st.code('width: px')
  st.code('height: px')
  st.code('background-color: color')
  st.code('box-shadow:px px px')
  st.code("}")
  '---'
  'overflow (connect to a div or span)'
  st.code(''' #box{
  \nborder: 2px solid;
  \nheight: 100px;
  \noverflow: (visible:shows text, hidden:content that you don't see below the border is hidden, scroll:shows a scroll, auto: shows a scroll if it's needed)
  \n}
  ''')
  '---'
  '<div></div> and <span></span> to a text:'
  st.code('''
  #div highlights a block while span only highlights unless you add (display: block;) to span{} 
  \n#You can also do (display:inline) to make it so that the text is in other lines of text(no width and height)
  \n#If you want the width and height included (display: incline-block)
  ''')
  '---'
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
  #float allows text to be in the same row as the img
  }
  ''')
  '---'
  "edit box:"
  st.code('''Add padding: px; if you want there to be a distance between the letters and the border
  \nAdd box-sizing: border-box; if you want two different boxes in the same row using float:left; or float:right;
  \nAdd text-align: center; to put the text right in the middle
  \nwrite in height: 100vh; if you want bg-color to take up all the space of the page
  \n if you write the thing above and write in min-height: 50%;, the boxes will take 50% of the page''')
  '---'
  'make a table'
  st.code('''
  #in html
  \n<table border="0-int" style="background-color:color;">
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
  '---'
  "Image as a background!"
  st.code('''
  body{
  \nbackground-image: url(background.png);
  \nbackground-repeat: no-repeat;
  \nbackground-position: center;
  \nbackground-attachment: fixed;
  \nbackground-size: cover;
  ''')
  '---'
  'position'
  st.code('''#position:; is used for positioning or adding features to boxes
  \nExample:
  \n#box{
  \nwidth:200px;
  \nheight:200px;
  \nbackground-color:rgb(200, 200, 255);
  \nposition: (relative:add pos to it using up, down, left, and right, fixed:doesn't take up space and follows scroll, absolute:pos related to another box, sticky:move along the scroll and takes up space)
  ''')
  '---'
  'pseudo-classes'
  st.code('''
  #link
  \na:link{ #link in no state
  \ncolor:green;
  \nfont-size:25px;
  \n}
  \na:hover{ #cursor is over the link
    \ncolor:lightgreen;
    \nfont-size:50px;
  \n}
  \na:active{ #clicking now
  }\n
  \na:visited{} # if has been visited
  \n#you can use hover and active for other stuff too
  \nli:not(:hover){} #if not hovered now
  \nli:nth-child([which element 'number', or odd(all in odd), or even, or 3n(for every 3rd (num can change)), or 3n+1(starts with one)]){} #choose css to specific num(goes in order)
  \n#shows if hovered
  \n#idname somethinginid{
  \ndisplay:none;}
  \n#idname:hover somethinginid{
  \ndisplay: block;}
  ''')
  '---'
  'pseudo-elements'
  st.code('''
  h1::first-letter{} #editting the first letter
  \np::first-line{} #editting the first line
  \np::selection{} #editing the text that's highlighted
  \nsomething::before{
  \ncontent:"hi";} #this will appear before each text
  \nsomething::after{
  \ncontent:"hello";} #this will appear after each text
  ''')
  'you can use id or class to pseudo-class and pseudo-elements'
  '---'
  'transform images or boxes'
  st.code('''
  #box{
  \ntransform: translateX(50px); move by x
  \ntransform: translateY(50px); #move by y
  \ntransform: translate(50px, 50px); #move by x and y
  \ntransform: rotateX(135deg); #rotate by x
  \ntransform: rotateY(135deg); #rotate by y
  \ntransform: rotateZ(135deg, 135deg); #rotate by Z (3rd dimension)
  \ntransform: scaleX(2); #widen the x 
  \ntransform: scaleY(2); #widen the y
  \ntransform: scale(2, 3); #widen the x and y
  \ntransform: skewX(180deg); #skew in x
  \ntransform: skewY(180deg); #skew in y
  \ntransform: skew(180deg, 180deg); #skew in x and y
  \n}
  ''')
  '---'
  'box and img animations'
  st.code('''
  #first step: make a div
  #in the html file
  <div id="box"></div>
  #second step: make your animation
  in .css file
  use percentage(%) to make parts of your animation (max of 100%)
  or use from and to to make parts move
  Example: 100%{transform: translateX(300px)} or from and to{transform: translateY(-300px)}
  Function you can add to animations (examples):
  ------
  all translates and other(right above this)
  opacity: 1 or 0
  background-color: color
  box-shadow: px px px clr
  #How to make you animatipn keyframe example:
  @keyframes animationname{
  0%{transform: translate(0px, 0px)}
  25%{transform: translate(200px, 0px)}
  50%{transform: translate(200px, 200px)}
  75%{transform: translate(0px, 200px)}
  }
  #third step: add animation in box
  #box{
  width:px;
  height:px;
  background-color:color;
  animation-name: animationname;
  animation-duration: 5s;
  }
  #OPTIONAL: fourth step: edit stuff
  addtobox{
  animation-direction: normal or alternate or reverse or altername reverse;
  animation-iteration-count: infinate or integer;
  animation-play-state: running or paused;
  animation-timing-function: ease-in-out(speeds and then slows) or linear(constant speed) or steps(int)(stop-motion effect)
  }
  ''')
  "Make sure to write ; at the end of each unless you are making a animation"
  '---'
with javascript:
  st.header("Add javascript")
  "Step 1: make a .js file"
  "Step 2: type this line to the body of the html to run the javascript"
  st.code('<script src="nameofyourjs.js"></script>')
  '---'
  st.header("Beginner Javascript")
  '---'
  'variables:'
  st.code('var num = 10(int) or "happy"(str) or True(boolean)')
  'or'
  st.code('var num;')
  st.code('num = value;')
  '---'
  'write values'
  st.code('console.log("This will appear in the console")')
  st.code('''document.write("This will show on the website")
you can also put html in document.write [example: document.write("<h1>This Works!</h1>")]
          ''')
  st.code('alert("This will make an alert")')
  '---'
  'set different value'
  st.code('''
  Number() allows a variable to be a int
  String() allows a variable to be a str
  Boolean() allows a variable to be a boolean
  ''')
  '---'
  'limited ranges'
  st.code('''
  for(var i = 20(value to i); i >= 1(will run if this is true); i+=increment or i-=decrement){}''')
  '---'
  'switch and case'
  st.code('''switch(var){
  case (num or str):
  something()
  break
  ...(repeat) 
  ''')  
  '---'
  'string manipulation'
  st.code('''
  var = variable.replaceAll('- (can be changed)', '/ (can be changed)') #replaces the '-' with '/'
  var = variable.padStart(15 (can be changed), "0 (can be changed)") #would add 0's in the start if the chars aren't 15
  var = variable.padEnd(15 (can be changed), "0 (can be changed)") "would add 0's in the end if the chars aren't 15
  var = variable.charAt(0 (can be changed)) #would show the first number (str)
  var = variable.indexOf('a' (can be changed)) #what is the first time it shows the letter 'a' (int)
  var = variable.lastIndexOf('a' (can be changed)) #what is the last shows the letter 'a' (int)
  var = variable.length() #how many chars there is in the str
  var = variable.trim() #removes all the spaces
  var = variable.toUpperCase() #all chars is uppercase (str)
  var = variable.toLowerCase() #all chars is lowercase (str)
  var = variable.startsWith('i' (can be changed)) #returns boolean if string starts with i
  var = variable.endsWith('b') #returns boolean if string ends with b
  var = variable.includes('e') #returns boolean if str includes e
  var = variable.slice(0 (can be changed), 1 (can be changed)) #returns the first letter of a string (str)
  ''')
  '---'
  'input'
  st.code('let ask-the-user=prompt("I think im asking the user! ")')
  '---'
  'if statements'
  st.code('if ([string or int] [== or > or <] "something"){')
  st.code('(tab) something()')
  st.code('}')
  '---'
  'else if and elif:'
  st.code('(else if (str > 20){}) and else{}')
  '---'
  'and (&&), or (||), or not(!)'
  st.code('''
  #Example:
  if (var == 0 && var == 1){}
  if (var <= 0 || var >= 30){}
  if (!var){}
  ''')
  '---'
  'while loop'
  st.code('while (condition){do something}')
  '---'
  'random number'
  st.code('let random-number = Math.floor(Math.random() * max (if only ); is after it, max-1) + min')
  '---'
  'function'
  st.code('function nameoffunction(){next line}')
  '---'
  "document.getElementById(''):"
  st.code('use document.getElementById().onclick = function for buttons or input')
  "Example"
  st.code('''
  #in html file
  \n<button id="idname">name</button>
  \n#in css file
  \ndocument.getElementById().onclick = function(){stuff} or nameoffunction()
  ''')
  'Write stuff in js using id'
  'Example:'
  "in the body"
  st.code('<p id="selected-id"></p>')
  'make a .js file'
  'connect it to the html'
  st.code('<script src="nameofyourjs.js"></script>')
  'In the .js file:'
  st.code('document.getElementById("selected-id")[.innerHTML if replace or .textContent if new] = "Whatyouwanttowrite"')
  st.code('''use variable = document.getElementById().value to get the stuff from a html input
  \n#Example (in html file):
  \n<label for="idname">Type something</label>
  \n<input type="text" id="idname">
  \n(in .js):
  \nlet text = document.getElementById("idname").value;
  ''')
  '---'
  st.code('''
  #how to set css in javascript
  something = document.getElementById('id or something'[example:'#box'])
  box.style.addcss[example:transform = 'rotateZ(135deg)';
  ''')
  '---'
  st.code('''
  #key buttons using addEventListener
  document.addEventListener('keydown', event =>{
  var = event.key (arrows: ArrowUp, ArrowDown, ArrowLeft, ArrowRight)
  })
  ''')
  '---'
  st.code('''
  #mouse events
  box = document.getElementById('box')
  box.addEventListener('click', event => {
  event.style.backgroundColor = 'color' [if box is clicked, this event occurs]
  })
  box.addEventListener('mouseover', event =>{
  [if mouse is hovered over the id, this event occurs]
  })
  box.addEventListener('mouseout', event => {
  [if mouse is not hovered over the id, this event occurs]
  })
  ''')
  "p.s: for EVERY .addEventListener, don't add it in a while loop, instead, put it before the while loop"
  '---'
  'canvas API'
  st.code('''
  #in the html write this
  <canvas id="canvasname" width="num" height="num"></canvas>
  #if you want to see the border, write this in a css file
  #canvasname{
  border: 1px solid black;
  }
  #write this in html
  canvas = document.getElementById('canvasname');
  context = canvas.getContext('2d')
  ---
  #draw a line
  context.beginPath()
  context.moveTo(0 (num), 0 (num)) #starting pos of line
  context.lineTo(750 (num), 500 (num)) #endind pos of line
  #p.s: line is based on width and height!
  context.stroke() #type to make a line 
  context.fill() #use this to fill in a shape using lineTo()
  ---
  #change color of fill
  context.fillStyle = 'color'
  context.strokeStyle = 'color'
  use context.stroke() and .fill() to make a shape with a border
  ---
  #change border thickness
  context.lineWidth = num
  ---
  #rectangle or square
  context.strokeRect(xpos(num), ypos(num), pxlength(num), pxwidth(num))
  #fill a rectangle
  context.fillRect(xpos(num), ypos(num), pxlength(num), pxwidth(num))
  #p.s: you can use .lineWidth and .fillStyle for rect
  #you don't need a beginPath and .stroke for rect
  ---
  #circle
  context.beginPath()
  context.arc(xpos, ypos, radius, sAngle, eAngle) #for a full circle write '0' for sAngle and '2 * Math.PI' for eAngle
  context.stroke(), context.fill() or both
  ---
  #text
  context.font = 'px font-name'
  context.fillText('text' (str), xpos (num), ypos (num))
  #p.s write values in int except for context.fillStyle, the first value of .fillText, and context.font
  safe fonts: ['arial', 'verdana', 'tahoma', 'trebuchet ms', 'times new roman', 'georgia', 'garamond', 'courier new'] #also usable for html and css
  ---
  #images in canvas
  context.drawImage("images/image.jpg", xpos, ypos)
  ---
  #clear entire screen
  context.clearRect(0, 0, (thecanvasid).width [example: canvas.width], (thecanvasid).height)
  ''')
  '---'
  'wait'
  st.code('''
  async function functionname() {
  functionstuff()
  #to wait
  await sleep(num)
  }
  functionname()
  #to make it actually wait type this:
  async function sleep(milliseconds) {
  return new Promise((resolve) => {setTimeout(resolve, milliseconds)
  })
  }
  #p.s: wait is in milliseconds
  ''')
  '---'
  'Get xpos and ypos'
  st.code('''
  window.addEventListener('mousemove', event  => {
  xpos = event.clientX
  ypos = event.clientY
  })
  ''')
  '---'
  st.code('''
#3d graphics on canvas
#in html
<canvas id='canvasid'></canvas>
<script src='code.js' type='module'></script>
#in javascript
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.118/build/three.module.js'
import { OrbitControls } from 'https://cdn.skypack.dev/three@0.129.0/examples/jsm/controls/OrbitControls.js'
import { GLTFLoader } from 'https://cdn.skypack.dev/three@0.129.0/examples/jsm/loaders/GLTFLoader.js'
const scene = new THREE.Scene() #to draw shapes
const camera = new THREE.PerspectiveCamera(50, window.innerWidth/window.innerHeight, 0.1, 1000) #how much you can see, aspect ratio
const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('canvasid')})
renderer.setPixelRatio(window.devicePixelRatio)
renderer.setSize(window.innerWidth, window.innerHeight) #width and height in px
renderer.render(scene, camera)
#change camera angle
#Example:
camera.position.setZ(100) or .setX or .setY
#image as background
const bg = new THREE.TextureLoader().load('nameofpicture.jpg')
scene.background = bg
#3d object
const geometry = new THREE.TorusGeometry(10, 4, 19) or THREE.BoxGeometry(2, 2, 2) or THREE.SphereGeometry(1, 5, 4)
const material = new THREE.MeshStandardMaterial() or .MeshBasicMaterial( wireframe:true )
const shape = new THREE.Mesh(geometry, material)
scene.add(shape)
#to see it
#option 1
function animate() {
requestAnimationFrame( animate )
renderer.render(scene, camera)
}
#option 2
#use a while loop, renderer.render, async function, and await sleep
#change placement of object
shape.position.set(1, 2, 3) #x, y, z
#light
const light = new THREE.AmbientLight(0xffffff)
scene.add(light)
#rotate image
shape.rotation.x or .y or .z = num || int
#helpers
const grid = new THREE.GridHelper(200, 50)
scene.add(grid) #grids
#controls
const controls = new OrbitControls(camera, renderer.domElement)
  ''')
"Test code (just in case it doesn't work):"
st.code('''
import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.118/build/three.module.js'
import { OrbitControls } from 'https://cdn.skypack.dev/three@0.129.0/examples/jsm/controls/OrbitControls.js'
const scene = new THREE.Scene()
const camera = new THREE.PerspectiveCamera(50, window.innerWidth/window.innerHeight, 0.1, 1000)
const renderer = new THREE.WebGLRenderer({canvas: document.getElementById('3d')})
renderer.setPixelRatio(window.devicePixelRatio)
renderer.setSize(window.innerWidth - 20, window.innerHeight - 20)
camera.position.setX(100)
renderer.render(scene, camera)
const geometry = new THREE.TorusGeometry(10, 4, 19)
const material = new THREE.MeshStandardMaterial({color: new THREE.Color(0, 0, 255)})
const shape = new THREE.Mesh(geometry, material)
scene.add(shape)
const pointlight = new THREE.PointLight(0xffffff)
pointlight.position.set(5, 5, 10, 100)
const light = new THREE.AmbientLight(0xffffff)
scene.add(light, pointlight)
const grid = new THREE.GridHelper(2000, 500)
scene.add(grid)
const controls = new OrbitControls(camera, renderer.domElement)
scene.background = new THREE.Color(0, 255, 255)
function animate() {
    requestAnimationFrame( animate )
    shape.rotation.z += 0.1
    renderer.render(scene, camera)
}
animate()
  ''')
  '---'
  'p.s: list is same as python, except you need a #let'
  "p.s: make sure to add ; to the end of every line of code unless it is a if statement or a while loop"
  "you might not need ; at the end"

  
  
  
  

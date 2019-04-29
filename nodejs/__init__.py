import os
from flask import Flask, render_template

DIR = os.path.dirname(__file__)
DIR += '/'

title = "<title>Node.js</title>"
b0 = "<h1>What is Node.js</h1> <ul> <li>JavaScript runtime environment built on Google's V8 JavaScript engine</li> <li>Allows us to run JavaScript on the server instead of the browser</li> <li> Used to build powerful, fast, and highly scalable apps</li> </ul>"
b1 = "<h1>History of Node.js</h1> <ul> <li>Developed in 2009</li> <li>Funded by Joyent (application virtualization and cloud computing), which is now a part of Samsung</li> <li>As of 2017, it has been downloaded 25 million times, more than 2,000 contributors</li> <li>Part of the Linux Foundation (stability in open source)</li> </ul>"
b2 = "<h1>Why Use Node.js?</h1> <ul> <li>Same language(JavaScript) used in frontend and backend</li> <li>The ever-growing NPM (Node Package Manager) gives developers many tools and modules to use</li> <li>Event driven, non-blocking I/O model</li> <li>Many companies use Node.js as it is great to gather data from different sources and consolidate it and push it to many clients in real time</li> </ul>"
b3 = "<h1>Non-Blocking I/O</h1> <ul> <li>Uses a single thread to handle multiple requests instead of waiting for one request to be completed before handling another request</li> <li>Can handle tens of thousands concurrent requests</li> </ul>"
b4 = "<h1>npm (Node.js package manager)</h1> <ul> <li>Used to install node programs/modules</li> <li>Modules get installed into node_modules folder</li> <li>Popular modules include: <ul> <li>Express - Web development framework</li> <li>pug - Template Engine</li> <li>Socket.io - Server side component for websockets</li> <li>MongoDB/Mongoose - Database</li> </ul> </li> <li>Node.js comes with pre installed modules known as core modules</li> </ul>"
b5 = "<h1>Core Modules in Node.js</h1> <ul> <li>http - contains classes, methods, and events to create Node.js http server</li> <li>url - contains methods for URL resolution and parsing</li> <li>querystring - contains methods to deal with query string</li> <li>path - contains methods to deal with file paths</li> <li>fs - contains classes, methods, and events to work with file I/O</li> <li>util - contains utility functions useful for programmers</li> </ul>"
b6 = "<h1>To Intialize a Project Using Node.js</h1> <p>$npm init</p> <ul> <li>It will prompt for: The project's name, version, description, etc.</li> <li>It will be stored in a package.json file that is generated in the current directory</li> </ul>"
b7 = "<h1>package.json file</h1> <ul> <li>Any projects using Node.js should have a package.json file</li> <li>Stores metadata specific to the project (ex: name, version, and etc.)</li> <li>It also saves the dependencies of the project</li> </ul>"
b8 = "<h1>To use npm and modules</h1> <p>$npm install module_name</p> <ul> <li>Installs module from npm. Add --save flag to save to dependencies in package.json</li> <li>Running just npm install will install the dependencies listed in the package.json</li> </ul> <p>var module = require(module_name);</p> <ul> <li>Installs module from npm. Add --save flag to save to dependencies in package.json</li> </ul>"

app = Flask(__name__)

@app.route("/")
def home():
    #return render_template(DIR + "templates/index.html")
    return title + b0 + b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8
    
if __name__ == "__main__":
    app.debug = True
    app.run()

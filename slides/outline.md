# Who is my audience?

I'm Bill, a supportive, friendly leader of Pythonistas.  I want to see you display growth and confidence.

[x] - A point about growth and confidence

I'm Kayla, an NSS student. I want to learn about the general Python community, get excited about what's possible.  I'm new to this, so I need to have code examples and more exotic syntax explained.

[ ] - Define any tech-y terms
[ ] - All exotic syntax is explained.
[ ] - Any new tools have links to them and a brief explanation.
[ ] - Give a high level overview of transpiled languages

I'm Sean, I'm a cynical developer who thinks the idea of Python in the browser is preposterous.  I want density of information to dig into, and acknowledgement of constraints.

[x] - Acknowledge that this is for hobby projects, not for production
[ ] - Hint at specific technically deep possibilities

I'm Amara, a data scientist.  I want to apply my Python skills to the frontend, but don't know how.  I'd like to be encouraged to get started and give this a shot with a fun example, and easy to imitate instructions.

[ ] - Include instructions on setting up any example code show.

# Goal
A person who listened to this talk will be encouraged to try writing a simple web app in Python, and know where to start.  Despite the challenges, they'll be excited about the possibilities.

# Components

No Free Lunch - There isn't a perfect Python to JS option yet
* Transcrypt - transcrypt.org - Python to JS, with a small, lean runtime -
  *
```bash
pip install transcrypt
# Transpile to ES6 with annotated source maps
transcrypt -b -m -e 6 -n -a python/app.py
```
  * Pros - Fast, small, focused on integrating with the existing JavaScript tooling, debuggable
  * Cons - Semantic differences are annoying and hard to anticipate.

  * Example - keyword arguments have to be explicitly enabled.

Which of these these three requires enabling operator overloading?
a)
```
print(1 + 2)
```
b)
```
print([1, 2, 3][-1])
```
c)
```
print("Hello {}!".format("PyNash"))
```

Options that improve performance but modify behavior are turned on by default.

* Brython - brython.info - A Python interpreter written in JS that runs alongside your code in the Browser.
  *
```bash
mkdir myproject && cd myproject
pip install brython
brython
```
  * Pros - Closer in behavior to Python.  More 3rd party and standard library support
  * Cons - Hard to debug, slow, the default `browser` experience is a mis-step.

```
```

* PyPy.js - pypyjs.org - PyPy is a fast, compliant alternative implementation of the Python language. PyPy.js adds support to generate a fast subset of JavaScript instead of machine code, and transpiles the intepreter to that same fast subset of JavaScript using Emscripten.
  * Illustrates the downsides of Python

* Summary
* Why Python Frontend
* Demo
  * What does the app do?
  * What is it created with?
  * Demo
* Outline options
  * Transcrypt
  * Brython

# Questions
What about Web Assembly? https://stackoverflow.com/questions/44761748/compiling-python-to-webassembly

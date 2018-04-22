# TodoMVC.py
Helping intrepid Pythonistas experiment in the browser.

Based of of [TodoMVC](http://todomvc.com/), this provides examples of different Python -> JS solutions in the browser.

## Oh God, Why?

I'm tantalized by the possibility of sharing code between the frontend and the backend, especially data validation logic that's useful in both client-side forms and server-side views.  There are also domains that Python is still better at - being able to deploy a version of your server-side machine learning model to the browser would be awesome.  Finally, being able to write web apps in the same language as server code could lower the barrier to entry for Python programmers to jump into the frontend. Despite many improvements, JavaScript [still](https://stackoverflow.com/questions/3127429/how-does-the-this-keyword-work#3127609) [has](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration#Arrays) [warts](https://github.com/getify/You-Dont-Know-JS/blob/master/this%20%26%20object%20prototypes/apA.md#class-gotchas) that discourage Pythonistas from learning it.

### A Word of Caution to this Tale
The [tools](http://immutable.js/) [and](http://webpack.js.org/) [frameworks](https://reactjs.org/) [available](http://vuejs.org/) to the JavaScript ecosystem are [absurdly](http://www.jsfuck.com/) [powerful](https://mozilla.github.io/pdf.js/) and [comprehensive](https://github.com/facebook/react-devtools) [JavaScript is quickly evolving](https://babeljs.io/) into a [pretty good](https://media.giphy.com/media/8kqrtQiz9YqnS/giphy.gif) language.  Even if you make the leap into Python on the frontend, be prepared to use JavaScript tools and interfaces.

## Frameworks

* [Brython](http://www.brython.info) + [Brython `browser`](http://www.brython.info/static_doc/en/browser.html)

## Roadmap

* Slides for presentation
* [Transcrypt + React](http://www.transcrypt.org/examples#react_demo)
* Example of sharing code on the client and server
* Updated version of [Python in the Browser](http://stromberg.dnsalias.org/~strombrg/pybrowser/python-browser.html) with a focus on active frameworks.
* Live site of examples
* (maybe?) PYX - JSX for Python.

## Contributing
Contributions are welcome!  Follow the spec and instructions in the original [TodoMVC](https://github.com/tastejs/todomvc/blob/master/app-spec.md) to create a new sub-site.  Using `setup.py` or a [`Pipfile`](https://docs.pipenv.org/) is encouraged, and your app wil likely live in `python/app.py` instead of `js/app.js`.

## License
[MIT](LICENSE.md) © Max Shenfield.

# monograph

[![Build Status](https://travis-ci.com/worldwise001/monograph.svg?branch=master)](https://travis-ci.com/worldwise001/monograph)


Monograph is a service to help you find and extract summaries and relationships between different research papers. Right now it's in an extremely experimental state.

Check back later for demos and example results.

## Backend Development

This project works best if run from a python3 venv environment:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To escape the venv:
```
deactivate
```

To run the development server:
```
python monograph.uwsgi
```

To run the production server:
```
uwsgi --ini uwsgi.ini --http-socket /tmp/monograph.sock
```

### Tests

Tests are handled via pytest:
```
pip install pytest
```

and then either
```
pytest
```
OR
```
python -m pytest
```

### Linters

You can run flake8 as follows:
```
pip install flake8
flake8
```

Similarly for mypy:
```
pip install mypy
mypy .
```

## Frontend Development

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

In the webapp/ directory, you can run:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

## Contributors
| Name               | Username                                          |
| ------------------ | ------------------------------------------------- |
| Sarah Harvey       | [worldwise001](https://github.com/worldwise001)
| Emil Harvey        | [emil-h-harvey](https://github.com/emil-h-harvey) |

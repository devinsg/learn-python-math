### Running the code with python framework
```bash
python3 --version

pip3 install
fastapi pip3 
install uvicorn
```

```new bash (Mac OS)
python3 --version
pip3 install pandas fastapi pydantic uvicorn
uvicorn main:app --reload
```

uvicorn main:app --reload http://127.0.0.1:8000/docs

### Learning videos
* Using Python on Windows: https://docs.python.org/3/using/windows.html

* Python Full Course for free: https://www.youtube.com/watch?v=ix9cRaBkVe0
* Python Full Course for Beginners: https://www.youtube.com/watch?v=Rq5gJVxz55Q

* Harvard CS50 (2026) – Full Computer Science University Course: https://www.youtube.com/watch?v=Rq5gJVxz55Q
* Harvard CS50’s Introduction to Programming with Python – Full University Course: https://www.youtube.com/watch?v=nLRL_NcnK-4

* Python for Beginners with Hands-On Projects: https://www.youtube.com/watch?v=oDOw5tB3Udw&t=3402s


### Building the code

This package produces the following:

* lib/* - intermediate-stage commonjs build artifacts
* dist/* - the bundled script, along with other resources
* deploy/* - all resources which should be uploaded to a CDN.

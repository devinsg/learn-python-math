## learning python framework

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

### Learning
* Using Python on Windows: https://docs.python.org/3/using/windows.html


### Building the code

This package produces the following:

* lib/* - intermediate-stage commonjs build artifacts
* dist/* - the bundled script, along with other resources
* deploy/* - all resources which should be uploaded to a CDN.

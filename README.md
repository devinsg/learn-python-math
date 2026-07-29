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

### Build options

gulp clean - TODO
gulp test - TODO
gulp serve - TODO
gulp bundle - TODO
gulp package-solution - TODO


### Steps for develop/deployment
- nvm use 8.11.1
- npm install -g yo gulp
- npm install -g @microsoft/generator-sharepoint

- gulp serve
- gulp build
- gulp bundle --ship
- gulp deploy-azure-storage (if deploy to Azure CDN instead of Office 365 CDN)
- gulp package-solution --ship


# FastAPI - CRUD - PYMONGO

A basic boilerplate for FastAPI crud using mongodb NoSql database.
<br/>
<br/>

## Screenshot

![USER API](/assets/ss/crud_view.png)
<br/>

## Installation

#### 1. Create python environment

```bash
  python3 -m venv fastapicrud_mongodb
  cd fastapicrud_mongodb
```

#### 2. Activate source 

```bash
  source bin/activate
```

#### 3. Clone the code on machine
```bash
  git clone https://github.com/shavejshaikh/fastapi_crud_pymongo.git
```

#### 4. Run Application
```bash
  uvicorn app.main:app --reload --port 8000
```

## Docker Instance
```bash
  docker build -t fastapi_img .
```

```bash
  docker run -d --name fastapi_mongodb_cont -p 8000:8000 fastapi_img
```

## Built with

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Python](https://www.python.org/)
- [Mongodb](https://www.mongodb.com/)

## Contact

Shavej Shaikh - [@github](https://github.com/shavejshaikh) [@linkedin](https://www.linkedin.com/in/shavejshaikh/)

Project Link - [https://github.com/shavejshaikh/fastapi_crud_pymongo](https://github.com/shavejshaikh/fastapi_crud_pymongo)
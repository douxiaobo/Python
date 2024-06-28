from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/name/{name}")
async def hello_name(name: str):
    return {"message": f"Hello {name}"}

@app.get("/nameandage/{name}/{age}")
async def hello_name_age(name: str, age: int):
    return {"message": f"Hello {name}, you are {age} years old"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# Last login: Tue Jun  4 16:37:44 on ttys000
# douxiaobo@192 helloworld_faskapi % code .
# douxiaobo@192 helloworld_faskapi % python3 -m venv faskapi
# douxiaobo@192 helloworld_faskapi % rm -r faskapi
# douxiaobo@192 helloworld_faskapi % python3 -m venv fastapi
# douxiaobo@192 helloworld_faskapi % source fastapi/bin/activate
# (fastapi) douxiaobo@192 helloworld_faskapi % pip3 install fastapi
# Collecting fastapi
#   Downloading fastapi-0.111.0-py3-none-any.whl.metadata (25 kB)
# Collecting starlette<0.38.0,>=0.37.2 (from fastapi)
#   Downloading starlette-0.37.2-py3-none-any.whl.metadata (5.9 kB)
# Collecting pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4 (from fastapi)
#   Downloading pydantic-2.7.3-py3-none-any.whl.metadata (108 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 109.0/109.0 kB 1.0 MB/s eta 0:00:00
# Collecting typing-extensions>=4.8.0 (from fastapi)
#   Downloading typing_extensions-4.12.1-py3-none-any.whl.metadata (3.0 kB)
# Collecting fastapi-cli>=0.0.2 (from fastapi)
#   Downloading fastapi_cli-0.0.4-py3-none-any.whl.metadata (7.0 kB)
# Collecting httpx>=0.23.0 (from fastapi)
#   Downloading httpx-0.27.0-py3-none-any.whl.metadata (7.2 kB)
# Collecting jinja2>=2.11.2 (from fastapi)
#   Using cached jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
# Collecting python-multipart>=0.0.7 (from fastapi)
#   Downloading python_multipart-0.0.9-py3-none-any.whl.metadata (2.5 kB)
# Collecting ujson!=4.0.2,!=4.1.0,!=4.2.0,!=4.3.0,!=5.0.0,!=5.1.0,>=4.0.1 (from fastapi)
#   Downloading ujson-5.10.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (9.3 kB)
# Collecting orjson>=3.2.1 (from fastapi)
#   Downloading orjson-3.10.3-cp312-cp312-macosx_10_15_x86_64.macosx_11_0_arm64.macosx_10_15_universal2.whl.metadata (49 kB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.7/49.7 kB 3.3 MB/s eta 0:00:00
# Collecting email_validator>=2.0.0 (from fastapi)
#   Downloading email_validator-2.1.1-py3-none-any.whl.metadata (26 kB)
# Collecting uvicorn>=0.12.0 (from uvicorn[standard]>=0.12.0->fastapi)
#   Downloading uvicorn-0.30.1-py3-none-any.whl.metadata (6.3 kB)
# Collecting dnspython>=2.0.0 (from email_validator>=2.0.0->fastapi)
#   Using cached dnspython-2.6.1-py3-none-any.whl.metadata (5.8 kB)
# Collecting idna>=2.0.0 (from email_validator>=2.0.0->fastapi)
#   Using cached idna-3.7-py3-none-any.whl.metadata (9.9 kB)
# Collecting typer>=0.12.3 (from fastapi-cli>=0.0.2->fastapi)
#   Downloading typer-0.12.3-py3-none-any.whl.metadata (15 kB)
# Collecting anyio (from httpx>=0.23.0->fastapi)
#   Downloading anyio-4.4.0-py3-none-any.whl.metadata (4.6 kB)
# Collecting certifi (from httpx>=0.23.0->fastapi)
#   Downloading certifi-2024.6.2-py3-none-any.whl.metadata (2.2 kB)
# Collecting httpcore==1.* (from httpx>=0.23.0->fastapi)
#   Downloading httpcore-1.0.5-py3-none-any.whl.metadata (20 kB)
# Collecting sniffio (from httpx>=0.23.0->fastapi)
#   Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
# Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx>=0.23.0->fastapi)
#   Downloading h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)
# Collecting MarkupSafe>=2.0 (from jinja2>=2.11.2->fastapi)
#   Using cached MarkupSafe-2.1.5-cp312-cp312-macosx_10_9_universal2.whl.metadata (3.0 kB)
# Collecting annotated-types>=0.4.0 (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi)
#   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
# Collecting pydantic-core==2.18.4 (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi)
#   Downloading pydantic_core-2.18.4-cp312-cp312-macosx_11_0_arm64.whl.metadata (6.5 kB)
# Collecting click>=7.0 (from uvicorn>=0.12.0->uvicorn[standard]>=0.12.0->fastapi)
#   Using cached click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
# Collecting httptools>=0.5.0 (from uvicorn[standard]>=0.12.0->fastapi)
#   Downloading httptools-0.6.1-cp312-cp312-macosx_10_9_universal2.whl.metadata (3.6 kB)
# Collecting python-dotenv>=0.13 (from uvicorn[standard]>=0.12.0->fastapi)
#   Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)
# Collecting pyyaml>=5.1 (from uvicorn[standard]>=0.12.0->fastapi)
#   Downloading PyYAML-6.0.1-cp312-cp312-macosx_11_0_arm64.whl.metadata (2.1 kB)
# Collecting uvloop!=0.15.0,!=0.15.1,>=0.14.0 (from uvicorn[standard]>=0.12.0->fastapi)
#   Downloading uvloop-0.19.0-cp312-cp312-macosx_10_9_universal2.whl.metadata (4.9 kB)
# Collecting watchfiles>=0.13 (from uvicorn[standard]>=0.12.0->fastapi)
#   Downloading watchfiles-0.22.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (4.9 kB)
# Collecting websockets>=10.4 (from uvicorn[standard]>=0.12.0->fastapi)
#   Downloading websockets-12.0-cp312-cp312-macosx_11_0_arm64.whl.metadata (6.6 kB)
# Collecting shellingham>=1.3.0 (from typer>=0.12.3->fastapi-cli>=0.0.2->fastapi)
#   Downloading shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
# Collecting rich>=10.11.0 (from typer>=0.12.3->fastapi-cli>=0.0.2->fastapi)
#   Downloading rich-13.7.1-py3-none-any.whl.metadata (18 kB)
# Collecting markdown-it-py>=2.2.0 (from rich>=10.11.0->typer>=0.12.3->fastapi-cli>=0.0.2->fastapi)
#   Downloading markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
# Collecting pygments<3.0.0,>=2.13.0 (from rich>=10.11.0->typer>=0.12.3->fastapi-cli>=0.0.2->fastapi)
#   Downloading pygments-2.18.0-py3-none-any.whl.metadata (2.5 kB)
# Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=10.11.0->typer>=0.12.3->fastapi-cli>=0.0.2->fastapi)
#   Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
# Downloading fastapi-0.111.0-py3-none-any.whl (91 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 92.0/92.0 kB 1.6 MB/s eta 0:00:00
# Downloading email_validator-2.1.1-py3-none-any.whl (30 kB)
# Downloading fastapi_cli-0.0.4-py3-none-any.whl (9.5 kB)
# Downloading httpx-0.27.0-py3-none-any.whl (75 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 75.6/75.6 kB 1.6 MB/s eta 0:00:00
# Downloading httpcore-1.0.5-py3-none-any.whl (77 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.9/77.9 kB 1.5 MB/s eta 0:00:00
# Using cached jinja2-3.1.4-py3-none-any.whl (133 kB)
# Downloading orjson-3.10.3-cp312-cp312-macosx_10_15_x86_64.macosx_11_0_arm64.macosx_10_15_universal2.whl (253 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 253.8/253.8 kB 1.5 MB/s eta 0:00:00
# Downloading pydantic-2.7.3-py3-none-any.whl (409 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 409.6/409.6 kB 1.6 MB/s eta 0:00:00
# Downloading pydantic_core-2.18.4-cp312-cp312-macosx_11_0_arm64.whl (1.8 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 1.7 MB/s eta 0:00:00
# Downloading python_multipart-0.0.9-py3-none-any.whl (22 kB)
# Downloading starlette-0.37.2-py3-none-any.whl (71 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.9/71.9 kB 1.4 MB/s eta 0:00:00
# Downloading typing_extensions-4.12.1-py3-none-any.whl (37 kB)
# Downloading ujson-5.10.0-cp312-cp312-macosx_11_0_arm64.whl (51 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 51.8/51.8 kB 1.3 MB/s eta 0:00:00
# Downloading uvicorn-0.30.1-py3-none-any.whl (62 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.4/62.4 kB 1.6 MB/s eta 0:00:00
# Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
# Downloading anyio-4.4.0-py3-none-any.whl (86 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 86.8/86.8 kB 1.8 MB/s eta 0:00:00
# Using cached click-8.1.7-py3-none-any.whl (97 kB)
# Using cached dnspython-2.6.1-py3-none-any.whl (307 kB)
# Downloading h11-0.14.0-py3-none-any.whl (58 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.3/58.3 kB 1.4 MB/s eta 0:00:00
# Downloading httptools-0.6.1-cp312-cp312-macosx_10_9_universal2.whl (146 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 146.4/146.4 kB 2.2 MB/s eta 0:00:00
# Using cached idna-3.7-py3-none-any.whl (66 kB)
# Using cached MarkupSafe-2.1.5-cp312-cp312-macosx_10_9_universal2.whl (18 kB)
# Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)
# Downloading PyYAML-6.0.1-cp312-cp312-macosx_11_0_arm64.whl (165 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 165.6/165.6 kB 1.3 MB/s eta 0:00:00
# Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
# Downloading typer-0.12.3-py3-none-any.whl (47 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 47.2/47.2 kB 1.4 MB/s eta 0:00:00
# Downloading uvloop-0.19.0-cp312-cp312-macosx_10_9_universal2.whl (1.4 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 2.0 MB/s eta 0:00:00
# Downloading watchfiles-0.22.0-cp312-cp312-macosx_11_0_arm64.whl (390 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 390.2/390.2 kB 1.8 MB/s eta 0:00:00
# Downloading websockets-12.0-cp312-cp312-macosx_11_0_arm64.whl (121 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.3/121.3 kB 2.3 MB/s eta 0:00:00
# Downloading certifi-2024.6.2-py3-none-any.whl (164 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 164.4/164.4 kB 1.9 MB/s eta 0:00:00
# Downloading rich-13.7.1-py3-none-any.whl (240 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 240.7/240.7 kB 1.9 MB/s eta 0:00:00
# Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
# Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 87.5/87.5 kB 2.5 MB/s eta 0:00:00
# Downloading pygments-2.18.0-py3-none-any.whl (1.2 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 1.9 MB/s eta 0:00:00
# Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
# Installing collected packages: websockets, uvloop, ujson, typing-extensions, sniffio, shellingham, pyyaml, python-multipart, python-dotenv, pygments, orjson, mdurl, MarkupSafe, idna, httptools, h11, dnspython, click, certifi, annotated-types, uvicorn, pydantic-core, markdown-it-py, jinja2, httpcore, email_validator, anyio, watchfiles, starlette, rich, pydantic, httpx, typer, fastapi-cli, fastapi
# Successfully installed MarkupSafe-2.1.5 annotated-types-0.7.0 anyio-4.4.0 certifi-2024.6.2 click-8.1.7 dnspython-2.6.1 email_validator-2.1.1 fastapi-0.111.0 fastapi-cli-0.0.4 h11-0.14.0 httpcore-1.0.5 httptools-0.6.1 httpx-0.27.0 idna-3.7 jinja2-3.1.4 markdown-it-py-3.0.0 mdurl-0.1.2 orjson-3.10.3 pydantic-2.7.3 pydantic-core-2.18.4 pygments-2.18.0 python-dotenv-1.0.1 python-multipart-0.0.9 pyyaml-6.0.1 rich-13.7.1 shellingham-1.5.4 sniffio-1.3.1 starlette-0.37.2 typer-0.12.3 typing-extensions-4.12.1 ujson-5.10.0 uvicorn-0.30.1 uvloop-0.19.0 watchfiles-0.22.0 websockets-12.0
# (fastapi) douxiaobo@192 helloworld_faskapi % pip3 install uvicorn
# Requirement already satisfied: uvicorn in ./fastapi/lib/python3.12/site-packages (0.30.1)
# Requirement already satisfied: click>=7.0 in ./fastapi/lib/python3.12/site-packages (from uvicorn) (8.1.7)
# Requirement already satisfied: h11>=0.8 in ./fastapi/lib/python3.12/site-packages (from uvicorn) (0.14.0)
# (fastapi) douxiaobo@192 helloworld_faskapi % uvicorn main:app --reload
# INFO:     Will watch for changes in these directories: ['/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/helloworld_faskapi']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [5089] using WatchFiles
# INFO:     Started server process [5091]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
# INFO:     127.0.0.1:63504 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:63504 - "GET /favicon.ico HTTP/1.1" 404 Not Found
# INFO:     127.0.0.1:63505 - "GET /name/microsoft HTTP/1.1" 200 OK
# INFO:     127.0.0.1:63512 - "GET /nameandage/microsoft/50 HTTP/1.1" 200 OK
# ^CINFO:     Shutting down
# INFO:     Finished server process [5091]
# INFO:     Stopping reloader process [5089]
# (fastapi) douxiaobo@192 helloworld_faskapi % 


# (fastapi) douxiaobo@192 helloworld_faskapi % uvicorn main:app --reload
# INFO:     Will watch for changes in these directories: ['/Users/douxiaobo/Documents/Coding/Practice in Coding/Python/helloworld_faskapi']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [5126] using WatchFiles
# INFO:     Started server process [5128]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
# INFO:     127.0.0.1:63618 - "GET /docs HTTP/1.1" 200 OK                   这个地方打不开
# INFO:     127.0.0.1:63619 - "GET /redoc HTTP/1.1" 200 OK                  这个地方打不开。
# INFO:     127.0.0.1:63620 - "GET /name/microsoft HTTP/1.1" 200 OK
# INFO:     127.0.0.1:63625 - "GET /docs HTTP/1.1" 200 OK
# ^CINFO:     Shutting down
# INFO:     Waiting for application shutdown.
# INFO:     Application shutdown complete.
# INFO:     Finished server process [5128]
# INFO:     Stopping reloader process [5126]
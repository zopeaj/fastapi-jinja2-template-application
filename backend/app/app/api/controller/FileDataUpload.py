from typing import Optional, List
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, StreamingResponse
import requests
import shutil

uploadfile = FastAPI()

some_file_path = ""

@uploadfile.post("/file/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@uploadfile.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@uploadfile.post("/files/")
async def create_file(file: Optional[bytes] = File(None)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}

@uploadfile.post("/uploadfile/datas/")
async def create_upload_file(file: Optional[UploadFile] = File(None)):
    if not file:
        return {"message": "No Upload file sent"}
    else:
        return {"filename": file.filename}


@uploadfile.post("/files/component/")
async def create_file(file: bytes = File(..., description="A file read as bytes")):
    return {"file_size": len(file)}

@uploadfile.post("/upload-file/")
async def create_upload_file(file: UploadFile = File(..., description="a file read as UploadFile")):
    return {"filename": file.filename}


@uploadfile.post("/multiple-files/")
async def create_file(files: List[bytes] = File(..., description="Multiple files as bytes upload")):
    return {"file_sizes": [len(file) for file in files]}

@uploadfile.post("/uploadfile-multiple/")
async def create_upload_file(files: List[UploadFile] = File(..., description="Multiple files as UploadFile")):
    return {"filenames": [file.filename for file in files]}

@uploadfile.get("/")
async def main():
    content = """
        <body>
            <form action="/multiple-files/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
            </form>
            <form action="/uploadfile-multiple/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
            </form>
        </body>
    """
    return HTMLResponse(content=content)

@uploadfile.post("/files/data")
async def create_file(file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


@uploadfile.get("/videos")
def main():
    def iterfile():
        with open(some_file_path, mode='rb') as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="video/mp4")


@uploadfile.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        with open(file.filename, 'wb') as f:
            while contents := file.file.read(1024 * 1024): # 1024 * 1024 bytes (i.e, 1MB)
                f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        with open(file.filename, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}

@app.post("/upload")
def upload(files: List[UploadFile] = File(...)):
    for file in files:
        try:
            contents = file.file.read()
            with open(file.filename, 'wb') as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}

@app.post("/upload")
def upload(files: List[UploadFile] = File(...)):
    for file in files:
        try:
            with open(file.filename, 'wb') as f:
                while contents := file.file.read(1024 * 1024):
                    f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}

@app.post("/upload")
def upload(files: List[UploadFile] = File(...)):
    for file in files:
        try:
            with open(file.filename, 'wb') as f:
                shutil.copyfileobj(file.file, f)
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        finally:
            file.file.close()

    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}



url = 'http://127.0.0.1:8000/upload'
files = [('files', open('images/1.png', 'rb')), ('files', open('images/2.png', 'rb'))]
resp = requests.post(url=url, files=files)
print(resp.json())


@app.post("/create_file/")
async def image(image: UploadFile = File(...)):
    print(image.file)
    # print('../'+os.path.isdir(os.getcwd()+"images"),"*************")
    try:
        os.mkdir("images")
        print(os.getcwd())
    except Exception as e:
        print(e)
    file_name = os.getcwd()+"/images/"+image.filename.replace(" ", "-")
    with open(file_name,'wb+') as f:
        f.write(image.file.read())
        f.close()
   file = jsonable_encoder({"imagePath":file_name})
   new_image = await add_image(file)
   return {"filename": new_image}




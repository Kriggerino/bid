from fastapi import FastAPI, File, UploadFile
from reader import get_docx_data, get_datasheets, get_datasheet_name, get_requirements, read_datasheets_specs, compare
import threading
app = FastAPI()




@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    global current_filepath
    try:
        with open(f'./documents/{file.filename}', "wb") as validation_file:
            current_filepath = f'./documents/{file.filename}'
            validation_file.write(file.file.read())
        return {"status": "Upload completed"}
    except Exception as e:
        return {"status": f"Upload failed: {e}"}


import concurrent.futures

@app.post("/queryfile/")
async def query_file(query: str):
    if not current_filepath:
        return {"Error": "No file uploaded / found"}

    docx_data = get_docx_data(f'{current_filepath}')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        requirements_future = executor.submit(get_requirements, docx_data)
        datasheets_future = executor.submit(get_datasheet_name, docx_data)

        requirements = requirements_future.result()
        datasheets = datasheets_future.result()

    if not datasheets:
        return {"Error": "No datasheets found"}

    downloaded_files = get_datasheets(datasheets)

    if not downloaded_files:
        return {"Error": "Downloading datasheets failed. Aborting operation"}

    specs = read_datasheets_specs(downloaded_files)

    return compare(datasheets_specs=specs, requirements=requirements, query=query)

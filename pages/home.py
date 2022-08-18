from fastapi.responses import HTMLResponse
import utils.text_reader as text_reader

def get_home_page_html():
    return HTMLResponse(content=text_reader.get_html_content("pages/index.html"), status_code=200)

# def get_aula_1():
#     def iterfile():
#         with open("aula1.mp4", mode="rb") as file_like:
#             yield from file_like
    
#     return StreamingResponse(iterfile(), media_type="video/mp4")
from fastapi.responses import HTMLResponse
# , StreamingResponse
import utils as utils

def get_home_page_html():
    return HTMLResponse(content=utils.get_html_content("index.html"), status_code=200)

# def get_aula_1():
#     def iterfile():
#         with open("aula1.mp4", mode="rb") as file_like:
#             yield from file_like
    
#     return StreamingResponse(iterfile(), media_type="video/mp4")
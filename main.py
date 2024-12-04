"""

Main 

"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import openSense

app = FastAPI()
app.include_router(openSense.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

def main():
    """
    Main function
    """
    __version__ = "1.0.0"
    print(__version__)

    


if __name__ == "__main__":
    main()

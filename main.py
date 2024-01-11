from furhat_remote_api import FurhatRemoteAPI
from src.flow import example, introduction


if __name__=='__main__':
    furhat = FurhatRemoteAPI("localhost")
    introduction.run(furhat)
    
    # Example flow
    # example.run(furhat)
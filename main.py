from furhat_remote_api import FurhatRemoteAPI
from src.flow import introduction


if __name__=='__main__':
    furhat = FurhatRemoteAPI("localhost")
    introduction.run(furhat)
    
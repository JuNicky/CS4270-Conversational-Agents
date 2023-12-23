from furhat_remote_api import FurhatRemoteAPI
from src.flow import init


if __name__=='__main__':
    furhat = FurhatRemoteAPI("localhost")
    init.run(furhat)
    
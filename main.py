from furhat_remote_api import FurhatRemoteAPI
from src.flow import introduction, example	


if __name__=='__main__':
    furhat = FurhatRemoteAPI("localhost")
    example.run(furhat)
    
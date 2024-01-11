from furhat_remote_api import FurhatRemoteAPI
from src.flow import introduction, example, recommendCocktails


if __name__=='__main__':
    furhat = FurhatRemoteAPI("localhost")
    recommendCocktails.run(furhat)
    
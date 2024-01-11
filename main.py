from furhat_remote_api import FurhatRemoteAPI
<<<<<<< HEAD
from src.flow import introduction, example, recommendCocktails
=======
from src.flow import example, introduction
>>>>>>> main


if __name__=='__main__':
    furhat = FurhatRemoteAPI("localhost")
<<<<<<< HEAD
    recommendCocktails.run(furhat)
    
=======
    introduction.run(furhat)
    
    # Example flow
    # example.run(furhat)
>>>>>>> main

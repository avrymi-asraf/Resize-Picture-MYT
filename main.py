from os import listdir, mkdir
from secrets import choice
from typing import List
from PIL import Image
from os.path import isfile, join , getsize, isdir
import sys 




ENDS = ("png", "jpg", "jpeg","webp")
MAXSIZE = (2000, 2000)
NAME_NEW_FOLDER = "pictures_for_MYT"


def allPictures(path: str,onlyGiggers: bool = True) -> List[str]:
    picture = [item for item in listdir(path) if item.endswith(ENDS)]
    if onlyGiggers:
        picture = list(filter(lambda x:(getsize(x)>1000000), picture))
    result = [path+"\\"+item for item in picture]
    return result


def resizeImages(listPic: List[str]) -> None:
    for image in listPic:
        with Image.open(image) as im:

            ##

            if im.size[1] >im.size[0]:
                print(f'{im.filename} is Narrow image, not suitable for uploading \n \
                    do you want change it? Y/N')
                choiceYouser = input()
                while( choiceYouser not in "YNny"):
                    choiceYouser = input("Wrong choice Type Y if you want to crop the image N if not")
                if choiceYouser in "Nn":
                    continue
                else:
                    im =im.resize((im.size[0], im.size[0]))
            
            ##

            im.thumbnail(MAXSIZE, Image.Resampling.LANCZOS)
            im.convert('RGB').save("".join(im.filename.split(".")[0]+/".jpg"),'JPEG')
                    
                        
def add_folder_to_path(path:str,newfolder:str)->str:
 pass
    


if __name__ == '__main__':
    if len(sys.argv)==2 and isdir(sys.argv[1]):
        listPic = allPictures(sys.argv[1],False)
        if len(listPic)>0:
            resizeImages(listPic)
        else: print("No images found in folder")
    else:
        print("There is an error in the amount of arguments, or the path is not a folder")
    


import pandas as pd
import csv
from functions import getTopTen

top = 10
searchItem = input("Enter hastag with # you want to search: ")
topTen = getTopTen(searchItem, top, './Parking_Data.csv', True)

#Create the file for top ten influencers
topTenFile = open(searchItem[1:] +'TopTen.txt' , 'w')
topTenFile.write("Top ten : User ID - Total number of tweets for that hashtag\n\n")
topTenFile.writelines(topTen)
topTenFile.close()
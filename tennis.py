import pandas as pd
from collections import defaultdict
import operator 

#This method reads the csv provided
def readcsv():
    df = pd.read_excel('FINALutrdatascienceinternship2019.xlsx', sheet_name='FINALutrdatascienceinternship20')
    win = df.groupby('winner1id')['winner1id'].count()
    loss = df.groupby('loser1id')['loser1id'].count()
    d1 = win.to_dict()
    d2 = loss.to_dict()
    print('Reading data from csv...')
    return d1,d2

#This method implements the algorithm and classify the players into three categories and assigns the Base Score
def classifyplayers(d1,d2):
    dd = defaultdict(list)
    for d in (d1, d2):
        for key, value in d.items():
            dd[key].append(value)
            summed = {key: sum(value) for (key, value) in dd.items()}
            summedcopy = summed
    for key, value in summedcopy.items():
        if value<=15:
            summedcopy[key]=15
        elif value>=15 and value <=30:
            summedcopy[key]=50
        elif value>30:
            summedcopy[key]=100
    print('Classifying players...')
    return summedcopy
    
#This method calculates the Player Points based upon the number of wins or losses
def calculatescore(totalgames,win ,loss):
    winsum = defaultdict(list)
    for i in (totalgames, win):
        for key, value in i.items():
            winsum[key].append(value)
            winsum1 = {key: sum(value) for (key, value) in winsum.items()}
    
    losssum = defaultdict(list)
    for j in (winsum1, loss):
        for key, value in j.items():
            losssum[key].append(value)
            finalsum = {key: winsum1[key] - loss.get(key, 0) for (key, value) in losssum.items()}
    sortedscore = sorted(finalsum.items(), key=operator.itemgetter(1), reverse=True)
    print('Generating scores...')
    return sortedscore

#This method calculates the Ranks based upon the final player points and imports the data as a csv
def generaterank(score):
    dfObj = pd.DataFrame(score, columns=['PlayerID','Score'])
    del dfObj['Score']
    dfObj.insert(1,'Rank', list(dfObj.index.values+1))
    dfObj.to_csv('Rank.csv', encoding='utf-8', index=False)
    print('Rank generated!') 
    
        
    
    
    

#################################################
def main():
    d1,d2 = readcsv()
    totalgames = classifyplayers(d1,d2)
    getscore = calculatescore(totalgames, d1, d2)
    generaterank(getscore)


################################################################
# Main Program

if __name__ == '__main__':
    main()



import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('RegionInfo.csv')


def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) Exit')
    Choice=input("")
    InorrectChoice=True
    while InorrectChoice:
        if Choice.isdigit():
            if int(Choice)==1 or int(Choice)==2 or int(Choice)==3:
                InorrectChoice=False
            else:
                print("You can choose only 1,2 or 3! Try again:")
                Choice=input("")
                InorrectChoice=True 
        else:
            print("Only digits! Try again:")
            Choice=input("")
            InorrectChoice=True 
    return int(Choice)

#prints all data from the file
def alldata():
    print(df)


def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']
    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    #concatenating results 
    result = pd.DataFrame(result)
    result.dropna(inplace=True)

    ave1=PropertyType(region, startdate, enddate, "Bungalow")
    ave1.plot(label="Bungalow",linestyle=":")
    ave2=PropertyType(region, startdate, enddate, "Semi-Detached")
    ave2.plot(label="Semi-Detached",linestyle="--")
    ave3=PropertyType(region, startdate, enddate, "Detached")
    ave3.plot(label="Detached")
    plt.show()
    
    
    if ave1.mean()>ave2.mean() or ave1.mean()>ave3.mean():
        print("Overall increase for Bungalow in chosen period of time was the biggest")
    elif ave2.mean()>ave1.mean() or ave2.mean()>ave3.mean():
        print("Overall increase for Semi-Detached in chosen period of time was the biggest")
    else:
        print("Overall increase for Detached in chosen period of time was the biggest")
    
    
    
#returns dataframe for specific property type     
def PropertyType(region, startdate, enddate, type):
    df1 = df.loc[:,startdate:enddate]
    df2 = df.loc[:,'Region':'Rooms']
    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    df3=df.loc[:, 'Property Type':'Rooms']
    result = pd.concat([result, df1], axis=1, join='inner').where(df2["Region"] == region).where(df3["Property Type"] == type)
    print(result)
    dfNumb=result.drop(["Region"],axis=1)
    dfNumb=dfNumb.drop(["Property Type"],axis=1)
    dfNumb=dfNumb.drop(["Rooms"],axis=1)
    dfNumb=dfNumb.mean()
    print(dfNumb)
    #concatenating results 
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    return dfNumb
    

x = mainmenu()
while x == 1 or x == 2:
    if x == 1:
        alldata()

    elif x == 2:
        while True:
            print()

            region = input("Please enter the name of the region you would like to check:")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                region_check(region, startdate, enddate)
                                break
                        break
                break
            else:
                print("Region not found")
    else:
        exit()
    x = mainmenu()
else:
    exit()


def strNums():
    print("Printing nums 1-1000 in a String: \n")
    mystr = ""
    for i in range(1, 1001):
        mystr = mystr+str(i)+","
    print(mystr[:-1])
strNums()


def Bing():
    mystr= "Binghamton"
    print("\n\nSlicing the string 'Binghamton': ")
    print(mystr[:3], mystr[4:6]+mystr[7], mystr[:2]+mystr[-3]+mystr[1]+mystr[-1]+mystr[3])
Bing()


def floatingP():
    print("\n\nSlicing string and converting numbers to floating point: ")
    results = "average: 0.8475"
    location= results.find(":")
    new_str = results[location+1:]
    new_str = float(new_str)
    print(new_str)
floatingP()

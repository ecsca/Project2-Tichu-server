# Create your views here.
from TichuDB.models import Player
from TichuDB.models import Room
from django.http import HttpResponse
from django.db.models import Max
from random import shuffle

def addId(request, cid, pwd):
    if(len(pwd)>20):
        return HttpResponse(",Password is too long,")
    elif(len(cid)>20):
        return HttpResponse(",ID is too long,")
    elif(len(pwd)<5):
        return HttpResponse(",Password is too short,")
    elif(Player.objects.filter(cID=cid)):
        return HttpResponse(",ID already exists,")
    newID = Player(cID = cid, password = pwd)
    newID.save()
    return HttpResponse(",success,")

def login(request, cid, pwd):
    user = Player.objects.filter(cID = cid, password = pwd)
    if (user):
        return HttpResponse(","+cid+",")
    return HttpResponse(",Wrong ID or password,")

def join(request, cid):
    n = 0
    eRoomDict = Room.objects.all().aggregate(Max('num'))
    if(eRoomDict['num__max']==None):
        newRoom = Room(User0 = cid)
        newRoom.save()
        return HttpResponse(","+str(newRoom.num)+","+str(0))
    eRoom = Room.objects.all().get(num = eRoomDict['num__max'])
    if(eRoom.User3!=""):
        newRoom = Room(User0 = cid)
        newRoom.save()
        return HttpResponse(","+str(newRoom.num)+","+str(0))
    num = 1
    if(eRoom.User1==""):
        Room.objects.filter(num = eRoom.num).update(User1=cid)
        num = 1
    elif(eRoom.User2==""):
        Room.objects.filter(num = eRoom.num).update(User2=cid)
        num = 2
    elif(eRoom.User3==""):
        Room.objects.filter(num = eRoom.num).update(User3=cid)
        num = 3
        Room.objects.filter(num = eRoom.num).update(start = True)
        D = range(101, 114) + range(201, 214)+ range(301,314) + range(401, 414) + range(501, 505)
        shuffle(D)
        a = ""
        for i in D:
            a+=str(i)+","
        Room.objects.filter(num = eRoom.num).update(Deck = a)
    return HttpResponse(","+str(eRoom.num)+","+str(num)+",")

def readyGame(request, Roomnum):
    eRoom = Room.objects.all().get(num = Roomnum)
    while(not eRoom.start):
        eRoom = Room.objects.all().get(num = Roomnum)
    return HttpResponse(","+eRoom.User0+",")

def startGame(request, Roomnum):
    Room.objects.all().filter(num = Roomnum).update(start = True)
    return HttpResponse(",Start,")

def readyTurn(request, Roomnum, unum, lastTurn):
    eRoom = Room.objects.all().get(num = Roomnum)
    t0 = eRoom.Flag0
    t1 = eRoom.Flag1
    t2 = eRoom.Flag2
    t3 = eRoom.Flag3
    while(t0 or t1 or t2 or t3):
        eRoom = Room.objects.all().get(num = Roomnum)
        t0 = eRoom.Flag0
        t1 = eRoom.Flag1
        t2 = eRoom.Flag2
        t3 = eRoom.Flag3
    if(lastTurn=="0"):
        flag = eRoom.Flag0
    elif(lastTurn=="1"):
        flag = eRoom.Flag1
    elif(lastTurn=="2"):
        flag = eRoom.Flag2
    elif(lastTurn=="3"):
        flag = eRoom.Flag3
    while(flag):
        eRoom = Room.objects.all().get(num = Roomnum)
        if(lastTurn=="0"):
            flag = eRoom.Flag0
        elif(lastTurn=="1"):
            flag = eRoom.Flag1
        elif(lastTurn=="2"):
            flag = eRoom.Flag2
        elif(lastTurn=="3"):
            flag = eRoom.Flag3
    if(unum=="0"):
        Room.objects.all().filter(num = Roomnum).update(wFlag0 = True)
    elif(unum=="1"):
        Room.objects.all().filter(num = Roomnum).update(wFlag1 = True)
    elif(unum=="2"):
        Room.objects.all().filter(num = Roomnum).update(wFlag2 = True)
    elif(unum=="3"):
        Room.objects.all().filter(num = Roomnum).update(wFlag3 = True)
    eRoom = Room.objects.all().get(num = Roomnum)
    t0 = eRoom.wFlag0
    t1 = eRoom.wFlag1
    t2 = eRoom.wFlag2
    t3 = eRoom.wFlag3
    while(not(t0 and t1 and t2 and t3)):
        eRoom = Room.objects.all().get(num = Roomnum)
        t0 = eRoom.wFlag0
        t1 = eRoom.wFlag1
        t2 = eRoom.wFlag2
        t3 = eRoom.wFlag3
    while(eRoom.thrown==""):
        eRoom = Room.objects.all().get(num = Roomnum)
    a = eRoom.thrown
    if(unum=="0"):
        Room.objects.all().filter(num = Roomnum).update(Flag0 = True)
    elif(unum=="1"):
        Room.objects.all().filter(num = Roomnum).update(Flag1 = True)
    elif(unum=="2"):
        Room.objects.all().filter(num = Roomnum).update(Flag2 = True)
    elif(unum=="3"):
        Room.objects.all().filter(num = Roomnum).update(Flag3 = True)
    return HttpResponse(","+eRoom.thrown+",")

def throw(request, Roomnum, unum, lastTurn, cards, fin):
    if(fin=="1"):
        if(unum=="0"):
            Room.objects.all().filter(num = Roomnum).update(fFlag0 = True)
        elif(unum=="1"):
            Room.objects.all().filter(num = Roomnum).update(fFlag1 = True)
        elif(unum=="2"):
            Room.objects.all().filter(num = Roomnum).update(fFlag2 = True)
        elif(unum=="3"):
            Room.objects.all().filter(num = Roomnum).update(fFlag3 = True)
    if(unum=="0"):
        Room.objects.all().filter(num = Roomnum).update(wFlag0 = True)
    elif(unum=="1"):
        Room.objects.all().filter(num = Roomnum).update(wFlag1 = True)
    elif(unum=="2"):
        Room.objects.all().filter(num = Roomnum).update(wFlag2 = True)
    elif(unum=="3"):
        Room.objects.all().filter(num = Roomnum).update(wFlag3 = True)

    eRoom = Room.objects.all().get(num = Roomnum)
    t0 = eRoom.wFlag0
    t1 = eRoom.wFlag1
    t2 = eRoom.wFlag2
    t3 = eRoom.wFlag3
    while(not(t0 and t1 and t2 and t3)):
        eRoom = Room.objects.all().get(num = Roomnum)
        t0 = eRoom.wFlag0
        t1 = eRoom.wFlag1
        t2 = eRoom.wFlag2
        t3 = eRoom.wFlag3
    eRoom = Room.objects.all().get(num = Roomnum)
    flag = True
    if(lastTurn=="0"):
        flag = eRoom.Flag0
    elif(lastTurn=="1"):
        flag = eRoom.Flag1
    elif(lastTurn=="2"):
        flag = eRoom.Flag2
    elif(lastTurn=="3"):
        flag = eRoom.Flag3
    while(flag):
        eRoom = Room.objects.all().get(num = Roomnum)
        if(lastTurn=="0"):
            flag = eRoom.Flag0
        elif(lastTurn=="1"):
            flag = eRoom.Flag1
        elif(lastTurn=="2"):
            flag = eRoom.Flag2
        elif(lastTurn=="3"):
            flag = eRoom.Flag3
    t0 = eRoom.Flag0
    t1 = eRoom.Flag1
    t2 = eRoom.Flag2
    t3 = eRoom.Flag3
    while(t0 or t1 or t2 or t3):
        eRoom = Room.objects.all().get(num = Roomnum)
        t0 = eRoom.Flag0
        t1 = eRoom.Flag1
        t2 = eRoom.Flag2
        t3 = eRoom.Flag3
    if(unum=="0"):
        Room.objects.all().filter(num = Roomnum).update(Flag0 = True)
    elif(unum=="1"):
        Room.objects.all().filter(num = Roomnum).update(Flag1 = True)
    elif(unum=="2"):
        Room.objects.all().filter(num = Roomnum).update(Flag2 = True)
    elif(unum=="3"):
        Room.objects.all().filter(num = Roomnum).update(Flag3 = True)
    Room.objects.all().filter(num = Roomnum).update(thrown = cards)
    eRoom = Room.objects.all().get(num = Roomnum)
    t0 = eRoom.Flag0
    t1 = eRoom.Flag1
    t2 = eRoom.Flag2
    t3 = eRoom.Flag3
    while(not(t0 and t1 and t2 and t3)):
        eRoom = Room.objects.all().get(num = Roomnum)
        t0 = eRoom.Flag0
        t1 = eRoom.Flag1
        t2 = eRoom.Flag2
        t3 = eRoom.Flag3
    Room.objects.all().filter(num = Roomnum).update(thrown = "")
    r = Room.objects.all().get(num = Roomnum)
    if(r.fFlag0==False):
        Room.objects.all().filter(num = Roomnum).update(Flag0=False)
    if(r.fFlag1==False):
        Room.objects.all().filter(num = Roomnum).update(Flag1=False)
    if(r.fFlag2==False):
        Room.objects.all().filter(num = Roomnum).update(Flag2=False)
    if(r.fFlag3==False):
        Room.objects.all().filter(num = Roomnum).update(Flag3=False)
    if(r.fFlag0==False):
        Room.objects.all().filter(num = Roomnum).update(wFlag0=False)
    if(r.fFlag1==False):
        Room.objects.all().filter(num = Roomnum).update(wFlag1=False)
    if(r.fFlag2==False):
        Room.objects.all().filter(num = Roomnum).update(wFlag2=False)
    if(r.fFlag3==False):
        Room.objects.all().filter(num = Roomnum).update(wFlag3=False)
#    if(unum=="0"):
#        Room.objects.all().filter(num = Roomnum).update(Flag0 = False)
#    elif(unum=="1"):
#        Room.objects.all().filter(num = Roomnum).update(Flag1 = False)
#    elif(unum=="2"):
#        Room.objects.all().filter(num = Roomnum).update(Flag2 = False)
#    elif(unum=="3"):
#        Room.objects.all().filter(num = Roomnum).update(Flag3 = False)
    return HttpResponse(",Success,")

def deal8(request, rnum, unum):
    d = Room.objects.all().get(num = rnum).Deck
    inum = int(unum)
    dList = d.split(",")
    counter = 0
    result =""
    for card in dList:
        if( ((inum)*14<= counter) and ((inum)*14+8 >counter)):
            result+=card
        counter+=1
    return HttpResponse(","+result+",")

def deal6(request, rnum, unum):
    d = Room.objects.all().get(num = rnum).Deck
    inum = int(unum)
    dList = d.split(",")
    counter = 0
    result =""
    for card in dList:
        if( ((inum)*14+8<= counter) and ((inum)*14+14 >counter)):
            result+=card
        counter+=1
    return HttpResponse(","+result+",")

def LTchu(request, rnum, unum, Tchu):
    if(unum=="0"):
        Room.objects.all().filter(num = rnum).update(lFlag0 = True, Tchu0 = int(Tchu))
    elif(unum=="1"):
        Room.objects.all().filter(num = rnum).update(lFlag1 = True, Tchu1 = int(Tchu))
    elif(unum=="2"):
        Room.objects.all().filter(num = rnum).update(lFlag2 = True, Tchu2 = int(Tchu))
    elif(unum=="3"):
        Room.objects.all().filter(num = rnum).update(lFlag3 = True, Tchu3 = int(Tchu))
    room = Room.objects.all().get(num = rnum)
    t0 = room.lFlag0
    t1 = room.lFlag1
    t2 = room.lFlag2
    t3 = room.lFlag3
    while(not (t0 and t1 and t2 and t3)):
        room = Room.objects.all().get(num = rnum)
        t0 = room.lFlag0
        t1 = room.lFlag1
        t2 = room.lFlag2
        t3 = room.lFlag3
    result = ""
    if(room.Tchu0 == 1):
        result+="1"
    else:
        result+="0"
    if(room.Tchu1 == 1):
        result+="1"
    else:
        result+="0"
    if(room.Tchu2 == 1):
        result+="1"
    else:
        result+="0"
    if(room.Tchu3 == 1):
        result+="1"
    else:
        result+="0"
    return HttpResponse(","+result)


def sTchu(request, rnum, unum, Tchu):
    if(unum=="0"):
        Room.objects.all().filter(num = rnum).update(sFlag0 = True, Tchu0 = int(Tchu))
    elif(unum=="1"):
        Room.objects.all().filter(num = rnum).update(sFlag1 = True, Tchu1 = int(Tchu))
    elif(unum=="2"):
        Room.objects.all().filter(num = rnum).update(sFlag2 = True, Tchu2 = int(Tchu))
    elif(unum=="3"):
        Room.objects.all().filter(num = rnum).update(sFlag3 = True, Tchu3 = int(Tchu))
    room = Room.objects.all().get(num = rnum)
    t0 = room.sFlag0
    t1 = room.sFlag1
    t2 = room.sFlag2
    t3 = room.sFlag3
    while(not (t0 and t1 and t2 and t3)):
        room = Room.objects.all().get(num = rnum)
        t0 = room.sFlag0
        t1 = room.sFlag1
        t2 = room.sFlag2
        t3 = room.sFlag3
    result = ""
    if(room.Tchu0 == 2):
        result+="1"
    else:
        result+="0"
    if(room.Tchu1 == 2):
        result+="1"
    else:
        result+="0"
    if(room.Tchu2 == 2):
        result+="1"
    else:
        result+="0"
    if(room.Tchu3 == 2):
        result+="1"
    else:
        result+="0"
    return HttpResponse(","+result)

def exCard(request, rnum, unum, card):
    result=""
    if(unum=="0"):
        Room.objects.all().filter(num=rnum).update(eCard0 = card, eFlag0=True)
    elif(unum=="1"):
        Room.objects.all().filter(num=rnum).update(eCard1 = card, eFlag1=True)
    elif(unum=="2"):
        Room.objects.all().filter(num=rnum).update(eCard2 = card, eFlag2=True)
    elif(unum=="3"):
        Room.objects.all().filter(num=rnum).update(eCard3 = card, eFlag3=True)
    eRoom = Room.objects.all().get(num = rnum)
    while(not (eRoom.eFlag1 and eRoom.eFlag2 and eRoom.eFlag3 and eRoom.eFlag0)):
        eRoom = Room.objects.all().get(num = rnum)
    if(unum=="0"):
        result+=eRoom.eCard1[0:3]
        result+=eRoom.eCard2[0:3]
        result+=eRoom.eCard3[0:3]
    elif(unum=="1"):
        result+=eRoom.eCard0[0:3]
        result+=eRoom.eCard2[3:6]
        result+=eRoom.eCard3[3:6]
    elif(unum=="2"):
        result+=eRoom.eCard0[3:6]
        result+=eRoom.eCard1[3:6]
        result+=eRoom.eCard3[6:]
    elif(unum=="3"):
        result+=eRoom.eCard0[6:]
        result+=eRoom.eCard1[6:]
        result+=eRoom.eCard2[6:]
    return HttpResponse(","+result)

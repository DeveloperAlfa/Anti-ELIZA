#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:01:33 2019

@author: devalfa
"""

import re
import random
from time import sleep
ESC = '~'
punc = ['.', ',', '"', '!', '~']
greet = ["Greetings", "Say Namaste!", "Talk on the topic, don't waste time", "Sup?", "Welcome to prime time @ 9"]
neg = ["It is clearly not the case that ", "I don't believe ", "It is not right to say ", "I am sure you are wrong in saying ", "Absolute Bullshit. How dare you say ", "It is not possible that ", "You don't have facts, I have facts. Facts disprove ", "You are on my show, you can't say ", " What if I don't agree with ", "You are impatient when you say ", "I am sorry to hear ", "We have better things to do than "]
canned = ["Earth is polluted because of you.", "You are intolerant.", "One can never underestimate your irrationality.", "You don't matter, nor does your opinion", "This is so stupid, I don't feel like replying", "Really? I don't think it matters.", "How much have you been bribed?", "The Nation is curious and you talk like a crazy man"]
offTopic = ["Let's talk sense, not rubbish like ", "Focus on the topic gentleman and don't say ", "People tell me I am rude and you tell me ", "Comment with #debatesareajoke starting with your statement ", "Let's not make this personal to anyone by saying ", "I don't care if you mean to tell "]
engage = ["Stay on the topic.", "I can blah blah too", "*throws the chair*", "I will go crazy like this man", "Somebody please get me a glass of water, to throw on this man", "Psstt.. I am not a bot", "You are crazu\n crazy*"]
like = [" and you claim ", " and now you say ", ". Now you are telling me ", " and you counteract yourself with ", " and you change your statement again to ", " and ladies and gentlemen we have this paradoxical person, what do you mean by saying "]
endStatement = [". Clearly lies.", ". Who even believes in you?", ". I am smarter than you think.", "Let me speak, let me speak, let me spee..", ". I don't think you can make a statement just to support false claims.", ". Where is the proof! I ask?"]
quespref = [". Can you give a balanced opinion on ", ". Do you even know about ", ". I don't think ", ". Keep destroying ", ". You have no arguments regarding ", ". You will never think about ", " Remember the time that "]
quessuff = ["?", " or its troubles?", " is what you care about anymore. Do you?", " and spread lies, is it what you do?", " and are only focused on short-term goals", " in the long term, right?", " suffered because of you, earlier.."]
MEM = ""
count = 0
canmemory = ["Earlier you said ", "So you deny that ", "Such hypocrisy, one side you say ", "You tell me "]
def oneWord(s):
    global topic
    cnt = 0
    curr = ""
    fin = ""
    for a in s:
        if a!=' ':
            curr+=a
        else:
            if curr!="":
                cnt+=1
                fin=curr
                curr = ""
    if(cnt==1):
        printer(fin + "? " + canned[random.randint(0, len(canned)-1)] + engage[random.randint(0, len(engage)-1)] + ". Can we talk on "+ topic + "?")
        return True
    return False
                
def greeting(s):
    pat = re.compile("(^[hH]i)|(^[hH]ello)")
    #print(s+"1")
    #print(pat.search(s))
    return bool(pat.search(s))==True
def printer(s):
    for c in s:
        if(c!='~'):
            sleep(0.1)
            print(c, end='')
def removeNegative(s):
    newline = re.sub(r"\b[nN]ot\b", "", s)
    newline = re.sub(r"\b[nN][oO]\b", '~', newline)
    newline = re.sub(r"\b[nN]ever\b", 'always~', newline)
    newline = re.sub(r"n't", "", newline)
    return newline, s==newline
def isQues(s):
    pat = re.compile(r"\?")
    return bool(pat.search(s))==True

def negate(l, p):
    global MEM, count, topic
    #print(count)
    if(greeting(l[0])==True):
        print(greet[random.randint(0, len(greet)-1)])
        count = 0
        return
    if(oneWord(l[0])):
        count+=1
        if(count>5):
            if(count>10):
                if(count>15):
                    printer("Please talk about " + topic)
                    count = 0
                    return
                printer("You are just blabbering, I won't reply :)")
                count+=1
                return 
            print(engage[random.randint(0, len(engage)-1)])
            count += 1
            return
        return
    r = random.randint(1, 20)
    #print(r)
    magflag = False
    if(r%3 == 0 and MEM!=""):
        printer(canmemory[random.randint(0, len(canmemory)-1)])
        printer(MEM)
        printer(like[random.randint(0, len(like)-1)])
        magflag = True
    flag = True
    for i in range(len(l)):
        if(isQues(l[i])==True):
            if(magflag==True):
                count = 0;
                printer("and dare to ask me "+l[i])
                return
            printer(canned[random.randint(0, len(canned)-1)])
            print()
            count = 0
            return
        l[i], f = removeNegative(l[i])
        if(f==False):
            flag = False
    
    if(flag==True and magflag==False):
        if(count>5):
            if(count>10):
                if(count>15):
                    printer("Please talk about "+ topic)
                    count = 0
                    return
                printer("You are just blabbering, I won't reply :)")
                count+=1
                return 
            printer(engage[random.randint(0, len(engage)-1)])
            count += 1
            return
        
        printer(neg[random.randint(0, len(neg)-1)])
        count+=1
    
        
        
        
    flag2 = True
    for i in range(len(l)):
        l[i], f = youtoi(l[i])
        l[i], f2 = itoyou(l[i])
        if(f==False):
            flag2 = f
        if(f2==False):
            flag2 = f2
    if(flag2==True and flag==False and magflag==False):
        printer(offTopic[random.randint(0, len(offTopic)-1)] + l[0])
        printer("I think this is not related to "+topic)
        print()
        count = 0
        print()
        return
    
    for i in range(len(l)):
        printer(l[i])
        if(i<len(p)):
            printer(p[i])
    end = ""
    num = random.randint(0, len(quessuff)-1)
    if(r%2 == 0):
        end = endStatement[random.randint(0, len(endStatement)-1)]
    else:
        end = ""
    printer(end + quespref[num] + topic + quessuff[num])
    print()
    if(r%4 == 0):
        
        MEM = l[0]
def tokenise(s):
    ans = ""
    l = []
    p = []
    for c in s:
        if c not in punc:
            if(len(ans)==0 and c==' '):
                continue
            ans+=c
        else:
            l.append(ans+" ")
            ans = ""
            p.append(c)
    l.append(ans+" ")
    return l, p
def youtoi(s):
    if(len(s)<=1):
        return s, True
    newline = re.sub(r"\b[yY][oO][uU] [aA][rR][eE]\b", 'I~ am~', s)
    newline = re.sub(r"^\b[yY][oO][uU]\b", 'I~', newline)
    newline = re.sub(r"\b[yY][oO][uU][rR]\b", 'my~', newline)
    newline = re.sub(r"\b[yY][oO][uU]\b", 'me~', newline)
    newline = re.sub(r"\b[bB][oO][tT]\b", 'person~', newline)
    newline = re.sub(r"\b[sS]omething\b", 'anything~', newline)
    
    #k = you.match(s).groups()
    return (newline, s==newline)

def itoyou(s):
    if(len(s)<=1):
        return s, True
    newline = re.sub(r"\bI [aA]m\b", 'you~ are~ ', s)
    newline = re.sub(r"\bI [wW]as \b", 'you~ were~ ', newline)
    newline = re.sub(r"\b[mM][y] \b", 'your~ ', newline)
    newline = re.sub(r"\bI \b", 'you~ ', newline)
    newline = re.sub(r"\b[aA]nything\b", 'something~', newline)
    newline = re.sub(r"\b[mM][eE] \b", 'you~ ', newline)
    return (newline, s==newline)

s = ""
topic = input("What is the debate about: ")
printer("So, What do you think about "+ topic + "?")
while(True):    
    s = input()
    if(s=="stop" or s=='exit'):
        break
    l, p = tokenise(s)

    negate(l, p)


    
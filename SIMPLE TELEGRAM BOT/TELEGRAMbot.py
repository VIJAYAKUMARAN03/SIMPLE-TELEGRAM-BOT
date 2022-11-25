
from flask import Flask
from flask import request
from flask import Response
from datasets import search_data
from googlesearch import search
import requests
from nltk.corpus import wordnet

#url to setup webhook
#https://api.telegram.org/bot5700587553:AAGDj5OHCBj8vjgbHWt3BLt47WRA-VmKhEE/setWebhook?url=<url from ngrok>
 
TOKEN = "5700587553:AAGDj5OHCBj8vjgbHWt3BLt47WRA-VmKhEE"
                                                                                                       
name="VIJI BOT" 

owner = "VIJAYAKUMARAN"

iam = """HI I'm VIJI !
I am a simple chatter bot, 
I'll greet you with some quotes if you greet me!
You can use me to search : 
    1. meaning for a word.(meaning of 'word')
    2. synonym for a word.(synonym of 'word')
    3. antonym for a word.(antonym of 'word')
    4. You can use me to get google link of anything by typing (google - 'word')
    5. I am also used to get dataset ...
        Yesh! you can use me to get dataset link by typing (dataset - 'word')
    6. Also you can use me to perform some binary mathematical operations 
        (No. operator No.) (e.g. 5 + 3)
        FOR,
        Addtion use (+)
        Substraction use (-)
        Multiplication use (*)or(x)
        Division use (/)
        power use (^).
    7. If your input is not related in anyone of the above then I'll act as a Echoo Bot :)."""


app = Flask(__name__)

def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r

    
def tel_send_image(chat_id,pic):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': pic
    }
 
    r = requests.post(url, json=payload)
    return r
 
def tel_send_document(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
 
    payload = {
        'chat_id': chat_id,
        "document": "https://www.pdfdrive.com/download.pdf?id=159388377&h=776e46b8a1d1209f8a9d7e617a26c450&u=cache&ext=pdf",
 
    }
 
    r = requests.post(url, json=payload)
 
    return r
    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
       
        chat_id,txt = parse_message(msg)
        txt=txt.lower()
        txt_lst=list(txt.split())
        
        if txt == "hi":
            tel_send_message(chat_id,"Hello!!\n"+iam)
            
        elif "who are you" in txt:
            tel_send_message(chat_id,iam)
            
        elif "what you can do" in txt:
            tel_send_message(chat_id,iam)
            
        elif "google -" in txt:
            L1 = txt_lst[2:]
            Searchword=' '.join(L1)
            link="Here's your search,\n"
            for j in search(Searchword,stop=3):
                link=link+j+"\n\n"
            tel_send_message(chat_id,link)
            
        elif "dataset -" in txt:
            L1 = txt_lst[2:]
            St=' '.join(L1)
            tel_send_message(chat_id, search_data(St))
            
        elif "meaning of" in txt:
            d=wordnet.synsets(txt_lst[2])
            reply=("Meaning of "+txt_lst[2]+" is \n"+d[0].definition())
            tel_send_message(chat_id,reply)
            
        elif "synonym of" in txt:
            d=wordnet.synsets(txt_lst[2])
            reply=("Synonym of "+txt_lst[2]+" is \n"+d[0].lemmas()[0].name()) 
            tel_send_message(chat_id,reply)
            
        elif "antonym of" in txt:
            d=wordnet.synsets(txt_lst[2])
            try: 
                reply=("Antonym of "+txt_lst[2]+" is \n"+d[0].lemmas.antonyms()[0].name())  
            except:
                reply=("Sorry, Antonym of "+txt_lst[2]+" is None :(")
            tel_send_message(chat_id,reply)
        
        elif "life book" in txt:
            tel_send_document(chat_id)
            tel_send_message(chat_id,"I recommend this book to you to learn and live a good Life!!")
            
        elif "book" in txt:
            tel_send_document(chat_id)
            tel_send_message(chat_id,"I recommend this book to you to learn and live a good Life!!")
            
        elif "your name" in txt:
            tel_send_message(chat_id,f"My name is  {name}")
            
        elif "your owner" in txt:
            tel_send_message(chat_id,f"My owner is {owner} who is a 2nd year student in Kongu Engineering College")
            
        elif "morning" in txt:
            tel_send_image(chat_id,"https://www.digitalkhabar.in/wp-content/uploads/amazing-good-morning-images.jpg")
        
        elif "afternoon" in txt:
            tel_send_image(chat_id,"https://i.pinimg.com/736x/f8/02/4e/f8024e7d3c7832352b2629ce7da4e646.jpg")
            
        elif "evening" in txt:
            tel_send_image(chat_id,"https://i.pinimg.com/736x/a4/1a/7e/a41a7eec6ef7e69f8482179907785100.jpg")
            
        elif "night" in txt:
           tel_send_image(chat_id,"https://cdn.quotesgram.com/img/64/49/1449261242-good-night-quotes.jpg")
           
        elif(len(txt_lst)==3):
            if(txt_lst[1] =="+" or  txt_lst[1]=="-" or txt_lst[1] == "*" or txt_lst[1]=="/"or txt_lst[1]=="^" or txt_lst[1]=='x' or txt_lst[1] == 'X'):
                try:
                    a=float(txt_lst[0])
                    b=float(txt_lst[2])
                    if(txt_lst[1]=="+"):
                        result=a+b
                    elif(txt_lst[1]=="-"):
                        result=a-b
                    elif(txt_lst[1]=="*" or txt_lst[1]=='x' or txt_lst[1] == 'X'):
                        result=a*b
                    elif(txt_lst[1]=="/"):
                        result=a/b
                    elif(txt_lst[1]=="^"):
                        result=a**b
            
                    tel_send_message(chat_id, txt + " = " +str(result))
                except:
                    tel_send_message(chat_id, txt)
            else:
                tel_send_message(chat_id, txt)
     
        else:
            tel_send_message(chat_id,txt)
       
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
   app.run(port=500,threaded=True,debug=True)
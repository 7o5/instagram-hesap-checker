from bs4 import BeautifulSoup as bs
import requests
import time

user_agent = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

def check(username):
    base_url = 'https://www.instagram.com/'
    profile_url = base_url + username

    r = requests.get(profile_url, headers=user_agent)

    if r.status_code == 200:
        html = bs(r.content, 'html5lib')
        if html.title != None:
            return True


def users():
    try:
        usernames = []
        with open('username.txt','r') as file:
            for user in file:
                usernames.append(user.strip())
        return usernames
    except FileNotFoundError:
        print("Dosyanızı 'username.txt' oluşturun.")

if __name__ == "__main__":
    start_time = time.time()
    
    for username in users():
        if check(username) == None:
            print(f"[BOŞTA] {username}")
            with open('bostakiler.txt','a') as bostakiler:
                bostakiler.write(f'{username}\n')            
        else:
            print(f"[DOLU] {username}")

    end_time = time.time()
    print(f"\nGeçen Süre: {end_time-start_time}")
    input("Programı kapatmak için Enter'a basın >> ")

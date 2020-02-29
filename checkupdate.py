import time,requests,os

print('Checking update...')
with open("fortnite.py", encoding='utf-8') as f:
    current = f.read().replace('“','"').replace('”','"')
github = requests.get("https://raw.githubusercontent.com/hallo239j/fortnitepy-bot/master/fortnite.py").text.replace('“','"').replace('”','"')
if current != github:
    print('Update found! Downloading...')
    os.remove("fortnite.py")
    print('Deleting old file...')
    with open("fortnite.py", 'w') as f:
        f.write(github)
    print('Done! Starting bot...')
elif current == github:
    print('No update!')
os.chdir(os.getcwd())
os.execv(os.sys.executable,['python','fortnite.py'])

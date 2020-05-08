import bs4
import requests, sys, pyperclip

# #reading from commandline/system
# sys.argv

# #to check if search is prompted from sys
# if len(sys.argv)>1:
#     urls=''.join(sys.argv[1:]) #storing address to be searched 

# #checking if search is prompted through copy on clipboard
# else:
#     urls=pyperclip.paste()     #storing address to be searched 

res=requests.get('https://www.amazon.in/s?k=shoes&ref=nb_sb_noss_2', headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
})
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, 'html.parser')

#selUrl='div.s-result-item:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3) > span:nth-child(2)'
elems=soup.select('div.sg-col-4-of-24:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)> span:nth-child(1)')

print(elems[0].text.strip())

#div.sg-col-4-of-24:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3) > span:nth-child(2)
#div.sg-col-4-of-24:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3) > span:nth-child(1)
#div.sg-col-4-of-24:nth-child(2) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)

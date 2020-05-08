import requests,sys ,pyperclip

#reading from commandline/system
sys.argv

#to check if search is prompted from sys
if len(sys.argv)>1:
    urls=''.join(sys.argv[1:]) #storing address to be searched 

#checking if search is prompted through copy on clipboard
else:
    urls=pyperclip.paste()     #storing address to be searched 

res=requests.get(urls)
res.raise_for_status()

#saving the data into text file named save
playFile=open('save.txt','wb')
for chunk in res.iter_content(1000000):
    playFile.write(chunk)

playFile.close()
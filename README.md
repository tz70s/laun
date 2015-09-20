# Laun
#### A useless lazy tool

![image](https://github.com/tz70s/Laun/blob/master/Shots/snapshot.jpg)

I'm inspired to do files exchange by my way via dropbox, because my usbs got disappeared very often.</br>
This is a weak command line tool I think.</br>
</br>
The program is still developing.</br>
So, the access token I hidden it,  you can generate it by your self.</br>

```Python
#oauth auth
authorize_url = flow.start()
#go to this url
print (authorize_url)
#copy and paste the authorization code
code = raw_input("Enter the authorization code").strip()
access_token, user_id = flow.finish(code)

#now the client generated
client = dropbox.client.DropboxClient(access_token)

```

### Reference
```Bash
Dropbox python api documentation
```


### Usage
```Bash
# clone
git clone https://github.com/tz70s/Laun.git

# usage doc
./Laun -h 
# list file
./Luan -l
# upload file
./Luan -u [file...] or [*]
# download file
./Luan -d [-r (remove from dropbox)][file...]
# remove file from dropbox
./Luan -r [file...]

# if file have special characters, use '\' before char
```

# Laun
#### A useless lazy tool

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

Reference : ```Dropbox python api documentation```


Usage
```Bash
./Laun -h 
```

#! /usr/bin/env python
'''
Tzu Chiao Yeh authored in 2015/09/18
Any suggestion: su3g4284zo6y7@gmail.com
'''

import dropbox
import os
import sys
import json

class ConnectError(BaseException(" error")):pass


# set app_key
#app_key = ''
# set app_secret
#app_secret = ''

#flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)



def command():
	#command usage docs

	docs = '''
	help : -h
	list files : -l 
	upload : -u [file ...]
	download : -d [-r (remove from dropbox)][file ...]
	'''

	mapping = ['-h','-u','-d','-r','-l']
	flags = ''

	#command usage

	if len(sys.argv[1:]) < 1:
		print ("Please input flags")
		print('Usage')
		print(docs)
		sys.exit() 

	if sys.argv[1:] == 0:
		print("Wrong input")
		sys.exit()
	if sys.argv[1] not in mapping:
		print("Please input the flag")
		print(docs)
		sys.exit()
	if sys.argv[1].lower() == '-h':
		print('Usage')
		print(docs)
		sys.exit()
	elif sys.argv[1].lower() == '-u':
		flags = 'u'
	elif sys.argv[1].lower() == '-d':
		flags = 'd'
		if sys.argv[2].lower() == '-r':
			flags = 'dr'
	elif sys.argv[1].lower() == '-r':
		flags = 'r'
	elif sys.argv[1].lower() == '-l':
		flags = 'l'


	if flags == 'u':
		try:
			file_name = sys.argv[2:]
			for fn in file_name:
				if fn not in os.listdir('.'):
					print("File is not exist")
					sys.exit()
				elif fn == '*':
					file_name = os.listdir('.')
					break
		except KeyError as err:
			print(err)
			print("Please type the file name")

	elif flags[0] == 'd':
		try:
			if len(flags)==1:
				file_name = sys.argv[2:]
			else:
				file_name = sys.argv[3:]
		except KeyError as err:
			print(err)
			print("Please type the file name")

	elif flags == 'r':
		try:
			file_name = sys.argv[2:]
		except KeyError as err:
			print(err)
			print("Please type the file name")

	elif flags == 'l':
		file_name = None


	#print(file_name)
	return file_name, flags


def getlist(client):
	#get file list
	data = client.metadata('/')
	rt = ""
	rt += "path: / \n"
	for cont in data[u'contents']:
		#print "\t" + cont[u'path'].lstrip('/')
		rt += "\t" + cont[u'path'].lstrip('/') + '\n'
	return rt

def inlist(client , file):
	data = client.metadata('/')
	for cont in data[u'contents']:
		if file == cont[u'path'].lstrip('/'):
			return True
		else:
			continue
	return False

def Laun():
	'''
	authorize_url = flow.start()
	print ("Go to ",authorize_url)
	code = raw_input("Enter the authorization code").strip()
	access_token, user_id = flow.finish(code)
	'''
	try:
		client = dropbox.client.DropboxClient('')
	except ConnectError as err:
		print(err)
		sys.exit()
	#print("linked account: ", client.account_info())

	file_name, flags = command()

	if flags == 'u':
		print("Uploading ...")
		for fn in file_name:
			if inlist(client, fn):
				print "\t"+fn + " had existed"
				continue
			fp = open(fn,'rb')
			response = client.put_file(fn, fp)
		print("Uploaded")
		#print 'uploaded', response
	elif flags.startswith('d'):
		print("Downloading ...")
		for fn in file_name:
			if not inlist(client, fn):
				continue
			fp = client.get_file(fn)
			out = open(fn,'wb')
			out.write(fp.read())
			out.close()
			if len(flags) > 1:
				client.file_delete(fn) 
		print("Downloaded")
	elif flags == 'r':
		for fn in file_name:
			if not inlist(client, fn):
				continue
			client.file_delete(fn)
		print("Removed")

	elif flags == 'l':
		print getlist(client)


Laun()

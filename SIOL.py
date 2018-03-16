import sys
import os 
import shutil
version = "Standard Input-Output Language V0.2-ALPHA"
keywords = ['quit', 'query', '--version']
ACTIVE_FILE = None
ACTIVE_PATH = os.getcwd()

def ERROR_MSG():
	print("Malformed query!")

def ERROR_FILE():
	print("No file loaded!")

def ERROR_INSERT():
	print("Inserting at end of file requires readln command!")

def ERROR_DIR():
	print("Specified directory already exists!")

def ERROR_REMOVE():
	print("Specified file does not exist!")

def ERROR_ACCESS():
	print("Cannot remove directory that contains active file!")

def ERROR_TEXT():
	print("Malformed text!")

def update_file(file):
	global ACTIVE_FILE
	ACTIVE_CPY = open(ACTIVE_FILE.name, ACTIVE_FILE.mode)
	ACTIVE_FILE.close()
	return ACTIVE_CPY

def transact(query):
	words = query.split(' ', 2)
	if (keyword == word[0] for keyword in keywords): 
		return keyword_act(words)
	else:
		return ERROR_MSG()

def keyword_act(words):
	if words[0] == 'quit':
		if ACTIVE_FILE:
			ACTIVE_FILE.close()
		sys.exit()
	elif words[0] == 'query':
		if len(words) != 3:
			return ERROR_MSG()
		else:
			advanced_transact(words)
	elif words[0] == '--version':
		print(version)
	elif words[0] == 'select':
		return select_transact(words)
	else:
		return ERROR_MSG()

def advanced_transact(words):
	global ACTIVE_FILE
	global ACTIVE_PATH
	if words[1] == 'file':
		if words[2].startswith('.'):
			file_info = words[2].split(' ', 1)
			try:
				ext = file_info[0]
				name = file_info[1]
			except:
				return ERROR_MSG()
			if os.path.isfile('{0}.{1}'.format(name, ext[1:])):
				try:
					file = open('{0}.{1}'.format(name, ext[1:]), 'a+')
					ACTIVE_FILE = file
				except:
					return ERROR_MSG()
			else:
				file = open('{0}.{1}'.format(name, ext[1:]), 'w')
				ACTIVE_FILE = file
		else:
			name = words[2]
			if os.path.isfile('{0}.txt'.format(name)):
				try:
					file = open('{0}.txt'.format(name), 'a+')
					ACTIVE_FILE = file
				except:
					return ERROR_MSG()
			else:
				file = open('{0}.txt'.format(name), 'w')
				ACTIVE_FILE = file
	elif words[1] == 'writeln':
		if not ACTIVE_FILE:
			return ERROR_FILE()
		line = words[2]
		ACTIVE_FILE.write('{0}\n'.format(line))
		ACTIVE_FILE = update_file(ACTIVE_FILE)
	elif words[1] == 'readln':
		if not ACTIVE_FILE:
			return ERROR_FILE()
		ACTIVE_FILE_CPY = open(ACTIVE_FILE.name, 'r')
		if words[2] == 'all':
			for line in ACTIVE_FILE_CPY:
				line = line[:-1]
				try:
					print(line)
				except:
					return ERROR_TEXT()
			return
		try:
			line_num = int(words[2])
		except:
			return ERROR_MSG()
		if line_num < 1:
			return ERROR_MSG()
		i = 1
		while i < line_num:
			ACTIVE_FILE_CPY.readline()
			i+=1
		dest = ACTIVE_FILE_CPY.readline()
		if dest.endswith('\n'):
			dest = dest[:-1]
		try:
			print(dest)
		except:
			return ERROR_TEXT()
	elif words[1] == 'deleteln':
		if not ACTIVE_FILE:
			return ERROR_FILE()
		if words[2] == 'all':
			new_name = ACTIVE_FILE.name 
			old_mode = ACTIVE_FILE.mode
			ACTIVE_FILE.close()
			os.remove(new_name)
			NEWFILE = open(new_name, old_mode)
			ACTIVE_FILE = NEWFILE
			return
		try:
			line_num = int(words[2])
		except:
			return ERROR_MSG()
		if line_num < 1:
			return ERROR_MSG()
		NEWFILE = open(ACTIVE_FILE.name, 'r')
		lines = NEWFILE.readlines()
		NEWFILE.close()
		NEWFILE = open(ACTIVE_FILE.name, 'w')
		i = 1
		for line in lines:
			if i == line_num:
				i+= 1
			else:
				NEWFILE.write(line)
				i+= 1
		NEWFILE.close()
		ACTIVE_FILE = open(ACTIVE_FILE.name, ACTIVE_FILE.mode)
	elif words[1] == 'insertln':
		if not ACTIVE_FILE:
			return ERROR_FILE()
		insert_info = words[2].split(' ', 1)
		try:
			line_num = int(insert_info[0])
		except:
			return ERROR_MSG()
		NEWFILE = open(ACTIVE_FILE.name, 'r')
		lines = NEWFILE.readlines()
		if line_num > len(lines):
			return ERROR_INSERT()
		NEWFILE.close()
		NEWFILE = open(ACTIVE_FILE.name, 'w')
		i = 1
		for line in lines:
			if i == line_num:
				NEWFILE.write(insert_info[1] + "\n")
				NEWFILE.write(line)
				i+=1
			else:
				NEWFILE.write(line)
				i+=1
		NEWFILE.close()
		ACTIVE_FILE = open(ACTIVE_FILE.name, ACTIVE_FILE.mode)
	elif words[1] == 'get':
		if words[2] == 'dir':
			print(ACTIVE_PATH)
		elif words[2] == 'file':
			if not ACTIVE_FILE:
				return ERROR_FILE()
			print(ACTIVE_FILE.name) 
		else:
			return ERROR_MSG()
	elif words[1] == 'ls':
		if words[2] == 'dir':
			dirs = os.listdir(ACTIVE_PATH)
			for directory in dirs:
				print(directory)
		else:
			return ERROR_MSG()
	elif words[1] == 'cd':
		dirs = os.listdir(ACTIVE_PATH)
		targetdir = words[2]
		if targetdir in dirs:
			os.chdir('{0}\{1}'.format(ACTIVE_PATH, targetdir))
			ACTIVE_PATH = os.getcwd()
		else:
			return ERROR_MSG()
	elif words[1] == '..':
		if words[2] == 'dir':
			os.chdir(os.path.split(ACTIVE_PATH)[0])
			ACTIVE_PATH = os.getcwd()
		else:
			return ERROR_MSG()
	elif words[1] == 'mkdir':
		dir_name = words[2]
		if not os.path.exists(dir_name):
			os.makedirs(dir_name)
		else:
			return ERROR_DIR()
	elif words[1] == 'remove':
		target = words[2]
		if os.path.exists(target):
			if os.path.isfile(target):
				try:
					os.remove('{0}/{1}'.format(ACTIVE_PATH, target))
				except PermissionError:
					return ERROR_ACCESS()
				except:
					return ERROR_REMOVE()
			elif os.path.isdir(target):
				try:
					shutil.rmtree('{0}/{1}'.format(ACTIVE_PATH, target))
				except PermissionError:
					return ERROR_ACCESS()
				except:
					return ERROR_REMOVE()
		else:
			return ERROR_REMOVE()
	elif words[1] == 'close':
		if not ACTIVE_FILE:
			return ERROR_FILE()
		elif words[2] == 'file':
			ACTIVE_FILE.close()
			ACTIVE_FILE = None
		else:
			return ERROR_MSG()
	elif words[1] == 'print':
		msg = words[2]
		print(msg)
	else:
		return ERROR_MSG()

def select_transact(words):
	global ACTIVE_FILE
	if words[1] == 'count':
		return count_transact(words)

def count_transact(words):
	global ACTIVE_FILE
	if words[2] == 'words':
		if not ACTIVE_FILE:
			return ERROR_FILE()
		else:
			count = 0
			ACTIVE_FILE_CPY = open(ACTIVE_FILE.name, 'r')
			lines = ACTIVE_FILE_CPY.readlines()
			for line in lines:
				count += len(line.split())
			return print(count) 
	elif words[2] == 'chars':
		if not ACTIVE_FILE:
			return ERROR_FILE()
		else:
			count = 0
			ACTIVE_FILE_CPY = open(ACTIVE_FILE.name, 'r')
			lines = ACTIVE_FILE_CPY.readlines()
			for line in lines:
				count += sum(char != '\n' for char in line)
			return print(count)
	elif words[2] == 'chars/spaces':
		if not ACTIVE_FILE:
			return ERROR_FILE()
		else:
			count = 0
			ACTIVE_FILE_CPY = open(ACTIVE_FILE.name, 'r')
			lines = ACTIVE_FILE_CPY.readlines()
			for line in lines:
				count += sum(char != ' ' and char != '\n' for char in line)
			return print(count)
	elif words[2] == 'lines':
		if not ACTIVE_FILE:
			return ERROR_FILE()
		else:
			count = 0
			ACTIVE_FILE_CPY = open(ACTIVE_FILE.name, 'r')
			lines = ACTIVE_FILE_CPY.readlines()
			return print(len(lines))
	elif len(words[2].split()) > 1:
		if not ACTIVE_FILE:
			return ERROR_FILE()
		identifier = words[2].split(' ', 1)
		if identifier[0] == 'character' and len(identifier) == 2:
			target = identifier[1]
			if len(target) > 1:
				return ERROR_MSG()
			count = 0
			ACTIVE_FILE_CPY = open(ACTIVE_FILE.name, 'r')
			lines = ACTIVE_FILE_CPY.readlines()
			for line in lines:
				count += sum(char == target for char in line)
			return print(count)
		elif identifier[0] == 'word' and len(identifier) == 2:
			target = identifier[1].strip()
			count = 0
			ACTIVE_FILE_CPY = open(ACTIVE_FILE.name, 'r')
			lines = ACTIVE_FILE_CPY.readlines()
			for line in lines:
				if target in line.split():
					count+=1
			return print(count) 
		elif identifier[0] == 'phrase' and len(identifier) == 2:
			target = identifier[1].strip()
			if len(target.split()) <=1:
				return ERROR_MSG()
			count = 0
			ACTIVE_FILE_CPY = open(ACTIVE_FILE.name, 'r')
			lines = ACTIVE_FILE_CPY.readlines()
			for line in lines:
				if target in line:
					count+=1
			return print(count)
	else:
		ERROR_MSG()



def main():
	global ACTIVE_FILE
	query = input("prompt>> ")
	transact(query) 
	main()
if __name__= '__main__':
	main()

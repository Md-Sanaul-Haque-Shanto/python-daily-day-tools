import os, time

target = 'C:\\Users\\broadcast-media\\Desktop\\python\\file-remover\\'

for x in os.listdir(target):
	if x.endswith('.json'):
		print('Deleting Files:', x)
		os.unlink(target + x)
		time.sleep(2)
		print('Files Deleted')
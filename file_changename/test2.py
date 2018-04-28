#只访问子文件夹中的重命名
import os
def rename(Path):
	file_dir=Path
	for root, dirs, files in os.walk(file_dir):
		for d in dirs:
			filelist = os.path.join(root, d)
			filelist1=os.listdir(filelist)
			for file in filelist1:#遍历子文件夹下的所有文件
				Olddir=os.path.join(filelist,file);#原来的文件路径
				if os.path.isdir(Olddir):#如果是文件夹则跳过
					continue
				filename=os.path.splitext(file)[0]#文件名
				filetype=os.path.splitext(file)[1]#文件扩展名
				change=str(int(filename[-4:])+250)
				newfilename=filename.replace(filename[-4:],change)
				Newdir=os.path.join(filelist,newfilename+filetype)#新的文件路径
				os.rename(Olddir,Newdir)#重命名		
		for f in files:
			pass
	print ('rename success')
if __name__ == '__main__':
	path="C:\\Python\\test"
	rename(path) 
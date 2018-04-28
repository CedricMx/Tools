#无文件夹
import os
import shutil
def rename(Path):
	path=Path
	filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
	filelist=sorted(filelist)
	print (filelist)
	print('-'*80)

	loadnum = 1
	for files in filelist[::-1]:#遍历所有文件
		Olddir=os.path.join(path,files)#原来的文件路径
		if os.path.isdir(Olddir):#如果是文件夹则跳过
			continue
		filename=os.path.splitext(files)[0]#文件名
		filetype=os.path.splitext(files)[1]#文件扩展名
		change=str(int(filename[-4:])+250)
		newfilename=filename.replace(filename[-4:],change)
		Newdir=os.path.join(path,newfilename+filetype)#新的文件路径
		os.rename(Olddir,Newdir)#重命名
		print ('[' + str(loadnum) + ' / 59]')
		loadnum += 1
	print('rename success !!')
if __name__ == '__main__':
	path="\\\\192.168.2.230\\Main\\Project2016\\TMZ\\Shots\\TMZ_001_004\\TMZ_001_004_0010\\Minicomp\\TMZ_001_004_0010_Minicomp_v280\\footage\\TMZ_001_004_0010_LAYER0"
	rename(path)

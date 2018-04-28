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
	total_num = len(filelist)
	for files in filelist[::-1]:#遍历所有文件
		Olddir=os.path.join(path,files)#原来的文件路径
		if os.path.isdir(Olddir):#如果是文件夹则跳过
			continue
		filename=os.path.splitext(files)[0]#文件名
		filetype=os.path.splitext(files)[1]#文件扩展名
		newfilename=filename.replace('LAYER2','LAYER3')
		Newdir=os.path.join(path,newfilename+filetype)#新的文件路径
		os.rename(Olddir,Newdir)#重命名
		print ('[' + str(loadnum) + '/' + str(total_num) + ']')
		loadnum += 1
	print('rename success !!')
if __name__ == '__main__':
	path="\\\\192.168.2.230\\Main\\Project2016\\TMZ\\Shots\\TMZ_005\\TMZ_005_0020\\Minicomp\\TMZ_005_0020_Minicomp_v033\\footage\\TMZ_005_0020_LAYER3"
	rename(path)

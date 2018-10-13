import xlrd


#读取百度百科解释并导入全局变量wordlist代表百度百科及其解释
data = xlrd.open_workbook('baidu.xls')
table_name = data.sheets()[0]
nrows = table_name.nrows
wordlist = []
for i in range(nrows):
	if i==0:
		continue
	wordlist.append(table_name.row_values(i))

	
#读取wiki百科解释并导入全局变量wikilist代表维基百科及其解释
data1 = xlrd.open_workbook('wiki.xls')
table_name1 = data1.sheets()[0]
nrows1 = table_name1.nrows
wordlist1 = []
for i in range(nrows1):
	if i==0:
		continue
	wordlist1.append(table_name1.row_values(i))
	

#百度百科与词条对应的函数
def baiduli(i,files,list1):
	for names in list1 :
		if names[1] == i:
			files.write('\n 百度百科解释：')
			print('successfully add baidu baike %s' % (i))
			return files.write(names[2])
	return print('fail to find %s in baidu baike' % (i))

#wiki百科词条对应函数
def wikili(i,files,list1):
	for names in list1:
		if names[1] == i:
			files.write('\n wiki百科解释: \n')
			print('successfully add wiki baike %s' %(i))
			return files.write(names[2])
	return print('fail to find %s in wiki baike' % (i))
	
#print(wordlist)
#开始处理
for i in range(184,999):
	try:
		f = open("w%s.txt" % (i) ,encoding = 'utf-8' )             # 打开文件对象
	except :
		print('fail to open txt w%s' %(i))
		continue
	line = f.readline()             #  readline()方法读取文件的行	
	while line:						#处理行
		name = ''					#设置词条的名字
		for var in line:				#如果行中有表示词条名称的符号 '〔'，则表示是一个单独的词条
			name += var
			if var == '〔' :
				try:
					w = open("%s.txt" %(name[:-1]), 'w', encoding = 'utf-8')  		#建立一个新的txt并命名为词条名
					w.write(line)														#将此行写入一个新的txt文件
					print( 'successfully write file %s.txt' % (name[:-1]) )                # 提示成功
					baiduli(name[:-1],w,wordlist)									#检查百度百科中是否有此词条
					wikili(name[:-1],w,wordlist1)									#检查wiki百科中是否有此词条
					w.close()				
				except:
					print( 'fail to write file %s.txt' %(name[:-1]))
		line = f.readline()								#读取一个新的行
	f.close()


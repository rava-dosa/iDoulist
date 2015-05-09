# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - output

output_list = ['http://book.douban.com/subject/1139336/', 
               'http://book.douban.com/subject/25724948/']

def output_CLI(output_doulist):
	print 'iDoulist: your input doulist link contains: ', output_list

def output_file(output_doulist):
	file_target = file('iDoulist.md', 'w')
	file_target.write('iDoulist: your input doulist link contains: \n')
	for i in output_list:
		file_target.write(i + '\n')
	print 'iDoulist: your input Doulist is exported as iDoulist.md'
	file_target.close()

output_file(output_list)

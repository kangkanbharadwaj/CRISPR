import os.path
from collections import Counter

class create_encoding(object):
	
	def create_encoded_file(self, source_path="", dest_path=""):
		
		fo2 = open(dest_path, "a")
		
		if os.path.exists(source_path):
			
			fo1 = open(source_path, "r")
			result = []

			for line in fo1:
				result.append(line.split())

			for pos, line in enumerate(result):
				for items in line:				
					if items.startswith('>'):

									crispr_id = items
									tmp_list1=[]
									tmp_list2=[]
									string1 = ""
									string2 = ""
									string3 = ""

									tmp_list1 =  result[pos+1]
									tmp_list2 = tmp_list1[-3:]

									if len(tmp_list2)>=3:
											string1 = tmp_list2[0]
											string2 = tmp_list2[1]
											string3 = tmp_list2[2]

											length1 = len(string1)
											length2 = len(string2)
											length3 = len(string3)

											len_of_str = max(length1, length2, length3)-1
											if len_of_str>=17:
													count1 = 1
													count2 = 1
													position_no_1 = 0
													position_no_2 = -5
													first_threshold = 8
													second_threshold = len_of_str-7

													fo2.write(crispr_id)
													fo2.write("\n")

													for i in range(0, 8):
															tmp_list3=[]
															block_no=1

															if i>3:
																	block_no=2
																	count1=count1+1

															if count1==2:
																	position_no_1=0 

															if string1[i]==string2[i]==string3[i]:
																	position_no_1=position_no_1+1
																	fo2.write(string1[i])
																	fo2.write(str(block_no))
																	fo2.write("N")
																	fo2.write(str(position_no_1))                         	                 

															else:
																	tmp_list3.append(string1[i])
																	tmp_list3.append(string2[i])
																	tmp_list3.append(string3[i])
																	position_no_1=position_no_1+1

																	common_char= [ite for ite, it in Counter(tmp_list3).most_common(1)]

																	fo2.write(common_char[0])
																	fo2.write(str(block_no))
																	fo2.write("Y")
																	fo2.write(str(position_no_1))

													for i in range(first_threshold, second_threshold):
																	tmp_list4=[]
																	tmp_list4.append(string1[i])
																	tmp_list4.append(string2[i])
																	tmp_list4.append(string3[i])

																	common_char= [ite for ite, it in Counter(tmp_list4).most_common(1)]
																	fo2.write(common_char[0])
																	fo2.write('3')
																	fo2.write("XX")


													for i in range(len_of_str, len_of_str-8, -1):
															tmp_list3=[]
															block_no=4

															if i<=(len_of_str-4):
																	block_no=5
																	count2=count2+1

															if count2==2:
																	position_no_2=-5


															if string1[i]==string2[i]==string3[i]:
																	position_no_2=position_no_2+1
																	fo2.write(string1[i])
																	fo2.write(str(block_no))
																	fo2.write("N")
																	fo2.write(str(position_no_2))
															else:
																	tmp_list3.append(string1[i])
																	tmp_list3.append(string2[i])
																	tmp_list3.append(string3[i])
																	position_no_2=position_no_2+1

																	common_char= [ite for ite, it in Counter(tmp_list3).most_common(1)]

																	fo2.write(common_char[0])
																	fo2.write(str(block_no))
																	fo2.write("Y")
																	fo2.write(str(position_no_2))

													fo2.write("\n")
			fo1.close()
			fo2.close()
		else:
			print "There is no file for processing, kindly enter the required file"

# 创建列表，各元素用逗号隔开，放在方括号内，列表可以存储混合类型的数据
objectlist = ["石榴", 1, "香蕉", "橙子", "梨子"]
objectlist[0] = "苹果"  # 修改列表第1个元素的值，注意列表索引号从0开始
del objectlist[1]  # 删除列表第2个元素
objectlist.append("猕猴桃")  # 在列表尾部添加一个数据元素"猕猴桃"
print(objectlist)  # 输出列表

input("运行完毕，请按回车键退出...")

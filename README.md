# iDoulist 爱豆列
## 简述
- 我们观察到在豆瓣进行图书豆列管理时的一些问题:
  1. 不能实现在指定豆列中找书,当豆列很长(如开智书单)时尤其麻烦
  2. 无法比较几个豆列是否重叠
  3. 无法导出豆列(及书籍信息)到文件永久保存
- 我们认为这些问题都可以通过人工重复劳动来解决,但繁琐并耗时,不是长久之计.对于开智群友更是时间的巨大浪费.
- 所以 iDoulist 被设计来解决豆列的这些问题, 帮助我们更加方便地使用豆瓣的大量书籍信息.

## 作品功能说明:
- 功能0: 导出豆列内容
    - input: 豆列链接
    - output: 豆列中内容(.md/CLI feedback) 
- 功能1: 对比两个/多个豆列内容
    - 应用场景: `开智群的哪些书我没有看过?`
    - 输入: 两个豆列链接 A B
    - 输出: AB的交/并,(A-B)等
- 功能2: 导入内容到豆列
    - 输入: 功能0导出的数据格式 + 目标豆列链接
    - 输出: 添加内容后的豆列内容
- 功能n ...

## 如何安装使用: 
- 在 OS X 10.10.4 测试
- Python 2.7.9
- 下载整个文件夹后, 安装jinja2，运行 function0_MVP.py 即可实现功能0
  - 如果不想安装 jinja2, 可运行 function0_MYP_plain.py
- 功能2 输出到豆列: 
  - 需要安装 [PyAutoGUI](http://pyautogui.readthedocs.org/en/latest/install.html). 
  - In OS X, 依次安装 pyobjc-core, pyobjc 及 PyAutoGUI
  - 运行 iDoulist_MVP.py
  - 正确输出到豆列, 需要在当前屏幕中有一个豆瓣页面, 并显示出"添加内容"按钮
  - 运行过程中由于 PyAutoGUI 会进行鼠标键盘操作, 不建议同时进行任何其它操作.
  - 长豆列的导入可能会需要几分钟甚至几十分钟
  - 如需停止, 可把鼠标移动到屏幕左上角, 或进入 terminal 按 Ctrl-C
  - 目前原型测试仅在 Chrome (42.0.2311.152) 中进行

## 成员
- [Frank Hu](https://github.com/Frank-the-Obscure), [教程](https://www.gitbook.com/book/frank-the-obscure/pythoncamp0/details)
- [Iris Lee](https://github.com/nicetag), [教程?](?)
- [huhu zhu](https://github.com/huhu8), [教程](https://github.com/huhu8/pythoncamp0)
- [zshaolin](https://github.com/zshaolin), [教程](https://github.com/zshaolin/pythoncamp0)
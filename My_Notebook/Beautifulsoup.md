Beautiful Soup 将复杂 HTML 文档转换成一个复杂的树形结构,每个节点都是 Python 对象,所有对象可以归纳为 4 种: Tag , NavigableString , BeautifulSoup , Comment .

Tag：通俗点讲就是 HTML 中的一个个标签，像上面的 div，p。每个 Tag 有两个重要的属性 name 和 attrs，name 指标签的名字或者 tag 本身的 name，attrs 通常指一个标签的 class。
NavigableString：获取标签内部的文字，如，soup.p.string。
BeautifulSoup：表示一个文档的全部内容。
Comment：Comment 对象是一个特殊类型的 NavigableString 对象，其输出的内容不包括注释符号.
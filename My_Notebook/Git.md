#三个区域
![](https://git-scm.com/book/en/v2/images/areas.png)
#基础操作

## 撤销操作

#### 修改最后一次的提交 
#### `--amend`
`git commit --amend` 
<br>
#### 取消已经暂存的文件
` git reset HEAD <file>`
适用情况：已经add添加到暂存区后
<br>
#### 取消对文件的修改
` git checkout -- <file>`
文件被上个版本的此文件覆盖。（慎用，因为文件没有提交过，所以无法恢复）
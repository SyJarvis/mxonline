# git代码提交



**第二步：** 进入本地项目文件，cmd进入命令框，输入

```
git init
```

会在本地项目文件中，生成一个.git的文件

**第三步：** 添加文件到仓库

```
git add .
```

**第四步：** 提交的文件注释说明，最好说明一下，否则有时候会出错

```
git commit -m '注释说明'
```

**第五步：** 将本地仓库关联到GitHub上的仓库里去

```
git remote add origin 仓库链接地址
```

**第六步：** 首次提交要git pull 一下

```
git pull origin master
```

**第七步：** 将代码提交到GitHub上

```
git push -u origin master
```



```
git status
git add .
git commit -m 'project initialized'
git push
```

git add -A 提交所有变化 
git add -u 提交被修改(modified)和被删除(deleted)文件，不包括新文件(new) 
git add . 提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件 





git config --global --unset http.proxy  

git config --global --unset https.proxy
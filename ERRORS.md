Django报错：ModuleNotFoundError: No module named 'widgets'

Greedhand. 2019-08-14 21:41:54  1303  收藏 1
分类专栏： Django
版权
from widgets import UEditorWidget,AdminUEditorWidget
会显示：ModuleNotFoundError: No module named ‘widgets’
原因：直接采用“pip install DjangoUeditor”安装的DjangoUeditor，是基于Python 2.7的，对Python3的不兼容。导致不能import widgets.py文件。
解决办法：在github下载兼容python3的DjangoUeditor,将DjangoUeditor放入到自己运行的虚拟坏境中，或者修改widgets.py
下载地址为：https://github.com/twz915/DjangoUeditor3.git


错误
```
ERRORS:
auth.User.groups: (fields.E304) Reverse accessor for 'User.groups' clashes with reverse accessor for 'UserProfile.groups'.
```
解决：
在setting.py中添加
### User表指定 app名.模型类名
AUTH_USER_MODEL = "users.UserProfile"


TemplateDoesNotExist at /index.html
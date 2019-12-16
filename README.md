
# Python3
-----

## Github.com Operation

Git tools is very important for Github, so introduce the command here first.
```markdown
    git config --global user.name "Your name"	
    git config --global user.email "Your email"
    ssh-keygen -t rsa -C "Your email"	
    eval
    ssh-agent -s
    ssh-add /c/users/admin/.ssh/id_rsa_name
    &&
    eval $(ssh-agent -s)
    ssh-add /c/users/admin/.ssh/id_rsa_name
    git clone https://github.com/Your name/reponsitions.git
    git add .
    git commit -m "commentary"
    git push
```
## Python install and Operating
Download it from *[python.org](https://www.python.org/downloads/)* for Windows and install, it's easy. In Linux so.
```markdown
    python -m pip install --upgrade pip
    python -m pip install 'your package'
```
Please create and modify the Source file *pip.ini*.Increase the download speed.
```markdown
    mkdir c:\users\username\pip
    touch c:\users\username\pip\pip.ini
    echo "
    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    [install]
    trusted-host = https://pypi.tuna.tsinghua.edu.cn" >> c:\users\username\pip\pip.ini
```
Making your Python file like *yourfilename.py* in IDE you like. Then implement it.
IDE:

*Sublime,Notepad++,Markdownpad2,Geany,Vim,Emacs,Jetbrain*,everyone of them can.

Implement statement:
```markdown
    python yourfilename.py
```
For example: make a name *test.py* and modify the content in it.
```markdown 
    print("Hello,Python!!!")
```     
save and exit the *test.py* file.
in the command line:
```markdown
    python test.py
```
 the output is:
```markdown  
    Hello,Python!!!
```      





# Deploy and Test

Deploy applications, and then run tests for checking deploy is succeed.

## required

- python2.7 `pyenv install 2.7.10 && cd fabric-template && pyenv local 2.7.10`  
- fabric `pip install fabric`  

## Execute

Deploy then run tests

```
$ fab -H hogehoge0001,aaaaa0001 deploy:node/sample.json
```

Deploy only

```
$ fab -H hogehoge0001,aaaaa0001 deploy:node/sample.json,skip_test=True
```

Test only

```
$ fab -H hogehoge0001,aaaaa0001 test:node/sample.json
```

## Architecture

```
.
|- deploy
|    |- base.py  .... Abstruct class
|    |- sample.py
|    `- hoge.py
|- node
|    |- sample.json
|    `- hoge.json
`- fabfile.py   ..... entrypoint 
```

With upper commands, fabfile.py is called as fabric default rule.  
So ease tune implementation by editing fabfile.py if you needed.


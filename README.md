# excel2json
Python script to parse excel files into json output

## Run script

```
$ python excelreader.py  /path/to/excel/file.xls
```


## Execute from PHP and wait for output

```
$command = escapeshellcmd('python excelreader.py  /path/to/excel/file.xls 2>&1 &');
$output = shell_exec($command);
```

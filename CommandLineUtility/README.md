# CommandLineUtility
This program uses argparse module and accepts 3 arguments:
- --x <Value1>
- --y <Value2>
- --o <add|sub|mul|div>

## Output (Positive Cases)
```
PS C:\TRY\Python\CommandLineUtility> python .\CommandLineUtility.py --x 4 --y 7 --o add
11.0
PS C:\TRY\Python\CommandLineUtility> python .\CommandLineUtility.py --x 4 --y 7 --o sub
-3.0
PS C:\TRY\Python\CommandLineUtility> python .\CommandLineUtility.py --x 4 --y 7 --o mul
28.0
PS C:\TRY\Python\CommandLineUtility> python .\CommandLineUtility.py --x 4 --y 7 --o div
0.571428571429
```
## Output (Negative Case)
If you run it like this, it'll print help message:
```
PS C:\TRY\Python\CommandLineUtility> python .\CommandLineUtility.py 3 5 add
usage: CommandLineUtility.py [-h] [--x X] [--y Y] [--o O]
CommandLineUtility.py: error: unrecognized arguments: 3 5 add
```
# pyjvmtools

## usage

usage: pyjvmtools.py [-h] -pid PID [-lockid LOCKID] [-v]

A tool to print jvm lock info.

optional arguments:
  -h, --help      show this help message and exit
  -pid PID        specify a jvm process id which you want to print lock info.
  -lockid LOCKID  specify a lockid to filter information.
  -v, --verbose   increase output verbosity

## example
```bash
$ python pyjvmtools.py -pid 1234
total log line count = 881 , total lockCount =  10
        <0    > 0x00000006e02d42f0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        <1    > 0x00000006e07d6718 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        <2    > 0x00000006e0025cd0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        <3    > 0x00000006e00249a0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        <4    > 0x00000006e0028fe0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        <5    > 0x00000006e0851a68 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        <6    > 0x00000006e002d770 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        <7    > 0x00000006d99a0770 waited num    10 , run num     0. There had unlocked lock and make deadlock.
        <8    > 0x00000006e07b24c8 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        <9    > 0x00000006e08519c0 waited num     5 , run num     0. There had unlocked lock and make deadlock.

$ python pyjvmtools.py -pid 1234  -lockid 0x00000006e08519c0
total log line count = 881 , total lockCount =  10
        <0    > 0x00000006e08519c0 waited num     5 , run num     0. There had unlocked lock and make deadlock.

$ python pyjvmtools.py -pid 1234  -lockid 0x00000006e08519c0 -v
total log line count = 881 , total lockCount =  10
        <0    > 0x00000006e08519c0 waited num     5 , run num     0. There had unlocked lock and make deadlock.
          index                     daemon                Tid    Nid           Condtion ThreadName
        ---------------------------------------------------------------------------------------------------------
        [    0]                     daemon 0x00007fbf5800d800 0x7f5e 0x00007fc0351bd000 ThriftClientPoolGcThreads-4
        [    1]                     daemon 0x00007fbfac001800 0x7eed 0x00007fc0357c3000 ThriftClientPoolGcThreads-3
        [    2]                     daemon 0x00007fbf58010000 0x7eec 0x00007fc0366d2000 ThriftClientPoolGcThreads-2
        [    3]                     daemon 0x00007fbf74072800 0x7eea 0x00007fc0362ce000 ThriftClientPoolGcThreads-1
        [    4]                     daemon 0x00007fbf7405d000 0x7ee9 0x00007fc0353bf000 ThriftClientPoolGcThreads-0

```
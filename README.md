# pyjvmtools

A tools to analysis lock info by reading thread dump info through `jstack` output.

There are two way to execute the command.

1. Specify pid argument to the pyjvmtools, let it to execute jstack and get the output.

2. Specify thread dump file path argument to the pyjvmtools, let it to analysis the file content.

## usage

usage: pyjvmtools.py [-h] (-pid PID | -file FILE) [-lockid LOCKID] [-v]

A tool to print jvm lock info.

optional arguments:
  -h, --help      show this help message and exit
  -pid PID        specify a jvm process id which you want to print lock info.
  -file FILE      specify a thread dump file path which you want to print lock
                  info.
  -lockid LOCKID  specify a lockid to filter information.
  -v, --verbose   increase output verbosity


## example
```bash
$ python pyjvmtools.py  -pid 31624
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

$ python pyjvmtools.py -pid 31624  -lockid 0x00000006e08519c0
total log line count = 881 , total lockCount =  10
<0    > 0x00000006e08519c0 waited num     5 , run num     0. There had unlocked lock and make deadlock.

$ python pyjvmtools.py -pid 31624  -lockid 0x00000006e08519c0 -v
total log line count = 881 , total lockCount =  10
<0    > 0x00000006e08519c0 waited num     5 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        |  index|   daemon|                 Tid|     Nid|                     State| ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |     YES | 0x00007fbf5800d800 | 0x7f5e |  TIMED_WAITING (parking) | ThriftClientPoolGcThreads-4
        [    1] |     YES | 0x00007fbfac001800 | 0x7eed |        WAITING (parking) | ThriftClientPoolGcThreads-3
        [    2] |     YES | 0x00007fbf58010000 | 0x7eec |        WAITING (parking) | ThriftClientPoolGcThreads-2
        [    3] |     YES | 0x00007fbf74072800 | 0x7eea |        WAITING (parking) | ThriftClientPoolGcThreads-1
        [    4] |     YES | 0x00007fbf7405d000 | 0x7ee9 |        WAITING (parking) | ThriftClientPoolGcThreads-0

$ python pyjvmtools.py  -pid 31624   -v
total log line count = 881 , total lockCount =  10
<0    > 0x00000006e02d42f0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |     YES | 0x00007fbf74b94000 | 0x7ef3 |        WAITING (parking) | file-worker-heartbeat-cancel-0

mbl@mbl-ThinkPad-T450:/software/projects/AllIdeaProjects/PycharmProjects/pyjvmtools$ python pyjvmtools.py  -file "/home/mbl/a.txt" -v
total log line count = 881 , total lockCount =  10
<0    > 0x00000006e02d42f0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |     YES | 0x00007fbf74b94000 | 0x7ef3 |        WAITING (parking) | file-worker-heartbeat-cancel-0

<1    > 0x00000006e07d6718 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |     YES | 0x00007fbf741a9800 | 0x7eeb |        WAITING (parking) | file-worker-heartbeat-0

<2    > 0x00000006e0025cd0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |     YES | 0x00007fbf5800f800 | 0x7dbf |        WAITING (parking) | UserGroupMappingCachePool-0

<3    > 0x00000006e00249a0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |      N0 | 0x00007fbfbc001800 |  0xbeb |  TIMED_WAITING (parking) | qtp1544057083-6119

<4    > 0x00000006e0028fe0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |     YES | 0x00007fc0c474c800 | 0x7bbe |        WAITING (parking) | FileSystemMaster-2

<5    > 0x00000006e0851a68 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |      N0 | 0x00007fc0c4956000 | 0x7c2d |        WAITING (parking) | pool-9-thread-4

<6    > 0x00000006e002d770 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |     YES | 0x00007fc0c4827800 | 0x7bc5 |  TIMED_WAITING (parking) | org.eclipse.jetty.server.session.HashSessionManager@636ccda7Timer

<7    > 0x00000006d99a0770 waited num    10 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |     YES | 0x00007fbf7420b800 |  0x20a |        WAITING (parking) | NettyChannelPoolGcThreads-9
        [    1] |     YES | 0x00007fbf8c004800 |  0x1d7 |        WAITING (parking) | NettyChannelPoolGcThreads-8
        [    2] |     YES | 0x00007fbfc4009000 |  0x1bd |        WAITING (parking) | NettyChannelPoolGcThreads-7
        [    3] |     YES | 0x00007fbfb4002800 |  0x18d |  TIMED_WAITING (parking) | NettyChannelPoolGcThreads-6
        [    4] |     YES | 0x00007fbf80001000 |  0x145 |        WAITING (parking) | NettyChannelPoolGcThreads-5
        [    5] |     YES | 0x00007fbf8c003800 | 0x7f8a |        WAITING (parking) | NettyChannelPoolGcThreads-4
        [    6] |     YES | 0x00007fbfb4001800 | 0x7f7c |        WAITING (parking) | NettyChannelPoolGcThreads-3
        [    7] |     YES | 0x00007fbf8c002800 | 0x7f5f |        WAITING (parking) | NettyChannelPoolGcThreads-2
        [    8] |     YES | 0x00007fbf8c001800 | 0x7ef2 |        WAITING (parking) | NettyChannelPoolGcThreads-1
        [    9] |     YES | 0x00007fbf7423e000 | 0x7eee |        WAITING (parking) | NettyChannelPoolGcThreads-0

<8    > 0x00000006e07b24c8 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |      N0 | 0x00007fbfe4001800 | 0x7c2e |        WAITING (parking) | Scheduler-1583209588

<9    > 0x00000006e08519c0 waited num     5 , run num     0. There had unlocked lock and make deadlock.
        _____________________________________________________________________________________________ 
        | index     daemon                  Tid      Nid                     State ThreadName 
        --------------------------------------------------------------------------------------------- 
        [    0] |     YES | 0x00007fbf5800d800 | 0x7f5e |  TIMED_WAITING (parking) | ThriftClientPoolGcThreads-4
        [    1] |     YES | 0x00007fbfac001800 | 0x7eed |        WAITING (parking) | ThriftClientPoolGcThreads-3
        [    2] |     YES | 0x00007fbf58010000 | 0x7eec |        WAITING (parking) | ThriftClientPoolGcThreads-2
        [    3] |     YES | 0x00007fbf74072800 | 0x7eea |        WAITING (parking) | ThriftClientPoolGcThreads-1
        [    4] |     YES | 0x00007fbf7405d000 | 0x7ee9 |        WAITING (parking) | ThriftClientPoolGcThreads-0

```
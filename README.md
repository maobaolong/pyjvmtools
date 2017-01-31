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
$ python pyjvmtools.py  -pid 31624
total log line count = 881 , total lockCount =  10
<0    > 0x00000006e02d42f0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
<1    > 0x00000006e07d6718 waited num     1 , run num     0. There had unlocked lock and make deadlock.
<2    > 0x00000006e0025cd0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
<3    > 0x00000006d99fa418 waited num    10 , run num     0. There had unlocked lock and make deadlock.
<4    > 0x00000006e00249a0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
<5    > 0x00000006e0028fe0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
<6    > 0x00000006e0851a68 waited num     1 , run num     0. There had unlocked lock and make deadlock.
<7    > 0x00000006e002d770 waited num     1 , run num     0. There had unlocked lock and make deadlock.
<8    > 0x00000006e07b24c8 waited num     1 , run num     0. There had unlocked lock and make deadlock.
<9    > 0x00000006e08519c0 waited num     5 , run num     0. There had unlocked lock and make deadlock

$ python pyjvmtools.py -pid 31624  -lockid 0x00000006e08519c0
total log line count = 881 , total lockCount =  10
<0    > 0x00000006e08519c0 waited num     5 , run num     0. There had unlocked lock and make deadlock.

$ python pyjvmtools.py -pid 31624  -lockid 0x00000006e08519c0 -v
total log line count = 881 , total lockCount =  10
<0    > 0x00000006e08519c0 waited num     5 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]      YES 0x00007fbf5800d800 0x7f5e 0x00007fc0351bd000 ThriftClientPoolGcThreads-4
        [    1]      YES 0x00007fbfac001800 0x7eed 0x00007fc0357c3000 ThriftClientPoolGcThreads-3
        [    2]      YES 0x00007fbf58010000 0x7eec 0x00007fc0366d2000 ThriftClientPoolGcThreads-2
        [    3]      YES 0x00007fbf74072800 0x7eea 0x00007fc0362ce000 ThriftClientPoolGcThreads-1
        [    4]      YES 0x00007fbf7405d000 0x7ee9 0x00007fc0353bf000 ThriftClientPoolGcThreads-0

$ python pyjvmtools.py  -pid 31624   -v
<0    > 0x00000006e02d42f0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]      YES 0x00007fbf74b94000 0x7ef3 0x00007fc035cc8000 file-worker-heartbeat-cancel-0

<1    > 0x00000006e07d6718 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]      YES 0x00007fbf741a9800 0x7eeb 0x00007fc035bc7000 file-worker-heartbeat-0

<2    > 0x00000006e0025cd0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]      YES 0x00007fbf5800f800 0x7dbf 0x00007fc036fdb000 UserGroupMappingCachePool-0

<3    > 0x00000006d99fa418 waited num    10 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]      YES 0x00007fbf7420b800  0x20a 0x00007fc036ad6000 NettyChannelPoolGcThreads-9
        [    1]      YES 0x00007fbf8c004800  0x1d7 0x00007fc0359c5000 NettyChannelPoolGcThreads-8
        [    2]      YES 0x00007fbfc4009000  0x1bd 0x00007fc0356c2000 NettyChannelPoolGcThreads-7
        [    3]      YES 0x00007fbfb4002800  0x18d 0x00007fc0354c0000 NettyChannelPoolGcThreads-6
        [    4]      YES 0x00007fbf80001000  0x145 0x00007fc036eda000 NettyChannelPoolGcThreads-5
        [    5]      YES 0x00007fbf8c003800 0x7f8a 0x00007fc0358c4000 NettyChannelPoolGcThreads-4
        [    6]      YES 0x00007fbfb4001800 0x7f7c 0x00007fc0367d3000 NettyChannelPoolGcThreads-3
        [    7]      YES 0x00007fbf8c002800 0x7f5f 0x00007fc035dc9000 NettyChannelPoolGcThreads-2
        [    8]      YES 0x00007fbf8c001800 0x7ef2 0x00007fc0376e2000 NettyChannelPoolGcThreads-1
        [    9]      YES 0x00007fbf7423e000 0x7eee 0x00007fc036bd7000 NettyChannelPoolGcThreads-0

<4    > 0x00000006e00249a0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]       N0 0x00007fbf3c001800 0x5880 0x00007fc034673000 qtp1544057083-7542

<5    > 0x00000006e0028fe0 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]      YES 0x00007fc0c474c800 0x7bbe 0x00007fc0377e3000 FileSystemMaster-2

<6    > 0x00000006e0851a68 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]       N0 0x00007fc0c4956000 0x7c2d 0x00007fc035fcb000 pool-9-thread-4

<7    > 0x00000006e002d770 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]      YES 0x00007fc0c4827800 0x7bc5 0x00007fc0371dd000 org.eclipse.jetty.server.session.HashSessionManager@636ccda7Timer

<8    > 0x00000006e07b24c8 waited num     1 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]       N0 0x00007fbfe4001800 0x7c2e 0x00007fc0369d5000 Scheduler-1583209588

<9    > 0x00000006e08519c0 waited num     5 , run num     0. There had unlocked lock and make deadlock.
        --------------------------------------------------------------------------------------------- 
        | index   daemon                Tid    Nid           Condtion ThreadName
        --------------------------------------------------------------------------------------------- 
        [    0]      YES 0x00007fbf5800d800 0x7f5e 0x00007fc0351bd000 ThriftClientPoolGcThreads-4
        [    1]      YES 0x00007fbfac001800 0x7eed 0x00007fc0357c3000 ThriftClientPoolGcThreads-3
        [    2]      YES 0x00007fbf58010000 0x7eec 0x00007fc0366d2000 ThriftClientPoolGcThreads-2
        [    3]      YES 0x00007fbf74072800 0x7eea 0x00007fc0362ce000 ThriftClientPoolGcThreads-1
        [    4]      YES 0x00007fbf7405d000 0x7ee9 0x00007fc0353bf000 ThriftClientPoolGcThreads-0

```
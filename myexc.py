#!/usr/bin/env python

import os, socket, errno, types, tempfile

class NetworkError(IOError):
    pass

class FileError(IOError):
    pass

def updArgs(args, newarg=None):
    if isinstance(args, IOError):
        myargs = []
        myargs.extend([arg for arg in args])
    else:
        myargs = list(args)

    if newarg:
        myargs.append(newarg)

    return tuple(myargs)

def fileArgs(thefile, mode, args):
    if args[0] == errno.EACCES and \
            'access' in dir(os):
        perms = ''
        permd = {'r': os.R_OK, 'w': os.W_OK,
            'x': os.X_OK}
        pkeys = permd.keys()
        pkeys.sort()
        pkeys.reverse()

        for eachPerm in 'rwx':
            if os.access(thefile, permd[eachPerm]):
                perms += eachPerm
            else:
                perms += '-'

        if isinstance(args, IOError):
            myargs = []
            myargs.extend([arg for arg in args])
        else:
            myargs = list(args)

        myargs[1] = "'%s' %s (perms: '%s')"% \
            (mode, myargs[1], perms)

        myargs.append(args.filename)

    else:
        myargs = args

    return tuple(myargs)

def myconnect(sock, host, port):
    try:
        sock.connect((host, port))

    except socket.error, args:
        myargs = updArgs(args)  # conv inst2tuple
        if len(myargs) == 1:  # no #s on some errs
            myargs = (errno.ENXIO, myargs[0])

        raise NetworkError, \
            updArgs(myargs, host + ': ' + str(port))

def myopen(thefile, mode='r'):
    try:
        fo = open(thefile, mode)
    except IOError, args:
        raise FileError, fileArgs(thefile, mode, args)

    return fo

def testfile():

    thefile = tempfile.mktemp()
    f = open(thefile, 'w')
    f.close()

    for eachTest in ((0, 'r'), (0100, 'r'),
            (0400, 'w'), (0500, 'w')):
        try:
            os.chmod(thefile, eachTest[0])
            f = myopen(thefile, eachTest[1])

        except FileError, args:
            print "%s: %s"% \
                (args.__class__.__name__, args)
    else:
        print thefile, "opened ok... perm ignored"
        f.close()

    os.chmod(thefile, 0777)# enable all perms
    os.unlink(thefile)

def testnet():
    s = socket.socket(socket.AF_INET,
        socket.SOCK_STREAM)

    for eachHost in ('deli', 'www'):
        try:
            myconnect(s, eachHost, 8080)
        except NetworkError, args:
            print "%s: %s"% \
                (args.__class__.__name__, args)

if __name__ == '__main__':
    testfile()
    testnet()

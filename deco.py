#!usr/bin/env python

def testit(func, *nkwargs, **kwargs):

    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception, e:
        result = (False, str(e))
    return result

def open():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '_'*20
        for eachvVal in vals:
            retval = testit(eachFunc, eachvVal)
            if retval[0]:
                print '%s(%s)= ' % (eachFunc.__name__, \
                    'eachvVal'),retval[1]
            else:
                print '%s(%s)= FAILED:' % (eachFunc.__name__, \
                    'eachvVal'),retval[1]

if __name__ == '__main__':
    open()

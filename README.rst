reduce
------
* The function reduce(func, seq) continually applies the function func() to the sequence seq.
::

    It returns a single value

* Info
::

    At first the first two elements of seq will be applied to func,
    i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]

    In the next step func will be applied on the previous result and the third element of the list
    i.e. func(func(s1, s2),s3)
    The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]

    Continue like this until just one element is left and return this element as the result of reduce()


def depth_1(f):
    def depth_with_message(*args):
        print "entering function"
        f(*args)
        print "leaving function"
    return depth_with_message
    
def depth_2(f):
    vars = {"depth": 0, "name": f.__name__}
    def depth_with_message(*args):
        print "enter %s: %s" % (vars['name'], vars['depth'])
        vars['depth'] += 1
        f(*args)
        vars['depth'] -= 1
        print "leave %s: %s" % (vars['name'], vars['depth'])
    return depth_with_message
    
def depth_3(arg):
    def depth_3_args(f):
        vars = {"depth": 0, "class": arg, "name": f.__name__}
        def depth_with_message(*args):
            print "enter %s.%s: %s" % (vars['class'], vars['name'], vars['depth'])
            vars['depth'] += 1
            f(*args)
            vars['depth'] -= 1
            print "leave %s.%s: %s" % (vars['class'], vars['name'], vars['depth'])
        return depth_with_message
    return depth_3_args

def depth_4(cls):
    for name, value in cls.__dict__.iteritems():
        if callable(value):
            d = depth_4_helper(cls.__name__, value)
            setattr(cls, name, d)
    return cls
    
def depth_4_helper(arg, f):
    vars = {"depth": 0, "class": arg, "name": f.__name__}
    def depth_with_message(*args):
        print "enter %s.%s: %s" % (vars['class'], vars['name'], vars['depth'])
        vars['depth'] += 1
        f(*args)
        vars['depth'] -= 1
        print "leave %s.%s: %s" % (vars['class'], vars['name'], vars['depth'])
    return depth_with_message
    
from hermes import common



if __name__ == "__main__":
    test = u'a�'
    val = common.safe_str(test)
    print val
    print common.safe_unicode(val)
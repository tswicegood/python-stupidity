# this file is now expliticly known as "foobar.barfoo"
import pkg_resources
pkg_resources.declare_namespace(__name__)

def non_base_barfoo():
    print "I'm non_base_barfoo"


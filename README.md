Setuptools Command to Run Tests in a TeamCity-compatible Manner
========================

If you use python setuptools (setup.py) and run your project in TeamCity, you want to be able to see
which tests failed and which tests got executed. This code does exactly that.

# This project is DEPRECATED and not any longer supported

Usage
-----

Instead of running:

    python setup.py test

use:

    python setup.py --command-packages teamcity_test teamcity_test

which does exactly the same, but uses [TeamCity build script interaction](http://confluence.jetbrains.net/display/TCD7/Build+Script+Interaction+with+TeamCity)
to communicate with the TeamCity build agent. This code is just an extension of the nice teamcity-messages module available under
http://confluence.jetbrains.net/display/TW/Python+Unit+Test+Reporting

Installation
------------

    python setup.py install

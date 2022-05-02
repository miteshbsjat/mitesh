MITESH => Modestly Integrated To Every SHell
============================================

.. |MiteSh| image:: images/Sun_Shell.png
  :width: 360
  :alt: Modestly Integrated To Every SHell

Introduction
************

``MiteSh`` is a very simple wrapper over `subprocess <https://docs.python.org/3/library/subprocess.html>`_ :) .
It enables us to run any POSIX shell (one-liner) in python and provides output line by line through generator.
This is inspired by perl's backtick operator \`\`.

``MiteSh`` is:

- **tiny:** The current source code has 164 lines of code (with about 35% documentation) and 114 lines of test.
- **written in pure Python:**   MiteSh neither needs an external server nor any dependencies from PyPI.
- **works on Python 3.6+ and PyPy3:** MiteSh works on all modern versions of Python and PyPy.
- **powerfully extensible:** You can easily extend ``MiteSh`` to more shells, currently tested with 
  - sh
  - bash
  - zsh


Supported Python Versions
*************************

MiteSh has been tested with Python 3.6+ and PyPy3.


Supported Operating Systems
***************************

``MiteSh`` should run on all \*NIX Operating Systems. Like:

- GNU/Linux
- UNIX \*BSD
- Mac OS (Darwin)


Examples
********
 
 **More examples can be found in** ``tests/test_mitesh.py``

Run Hello World
~~~~~~~~~~~~~~~

.. code-block:: python

    >>> from mitesh import MiteSh
    >>> for line in MiteSh("echo Hello World").execute():
    ...     print(line)
    ... 
    Hello World


Get Number of CPU Cores in Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> for line in MiteSh("cat /proc/cpuinfo | grep \"cpu cores\" | uniq | cut -d: -f2 | sed 's/ //g'").execute():
    ...     print(line)
    ... 
    6

The above command was run on ``Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz``


Using Different Shell
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> for line in MiteSh("echo hello", sh_type="sh").execute():
    ...     print(line)
    ... 
    hello
    >>> for line in MiteSh("ps", sh_type="sh").execute():
    ...     print(line)
    ... 
        PID TTY          TIME CMD
    51839 pts/5    00:00:00 bash
    91559 pts/5    00:00:00 python3
    102811 pts/5    00:00:00 sh
    102812 pts/5    00:00:00 ps
    >>> for line in MiteSh("ps", sh_type="zsh").execute():
    ...     print(line)
    ... 
        PID TTY          TIME CMD
    51839 pts/5    00:00:00 bash
    91559 pts/5    00:00:00 python3
    103035 pts/5    00:00:00 zsh
    103036 pts/5    00:00:00 ps
 

Tests
*****

.. code-block:: shell

    $ python3 -m unittest tests/test_mitesh.py 
    ...........
    ----------------------------------------------------------------------
    Ran 11 tests in 0.038s

    OK


Acknowledgement
***************

I would like to dedicate this package to my Mentor CNB and my Friend `Venkatesh Pitta <https://github.com/venkateshpitta>`_, without their inspiration and support, this would not be possible.
Also, I would like to thank God, my Teachers, my Parents, my Wife and Daughter to stand with me all the times. 


Contributing
************

Whether reporting bugs, discussing improvements and new ideas or writing
extensions: Contributions to ``MiteSh`` are welcome! Here's how to get started:

1. Check for open issues or open a fresh issue to start a discussion around
   a feature idea or a bug
2. Fork `the repository <https://github.com/miteshbsjat/mitesh/>`_ on Github,
   create a new branch off the ``master`` branch and start making your changes
   (known as `GitHub Flow <https://guides.github.com/introduction/flow/index.html>`_)
3. Write a test which shows that the bug was fixed or that the feature works
   as expected
4. Send a pull request and bug the maintainer until it gets merged and
   published 

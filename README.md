LLNW salt port for FreeBSD
==========================

* Upstream:  http://svn.FreeBSD.org/ports/head/sysutils/pysalt
* FreshPorts:  http://www.freshports.org/sysutils/pysalt/
* Our Port differences:  https://github.com/llnw/salt-build-freebsd/compare/upstream...LLNW

Building the port:
------------------
* `make -DBATCH install clean`

Port maintenance:
-----------------

* Alter DISTVERSION, DISTVERSIONSUFFIX in Makefile
* Update the distinfo checksums:  `make makesum`

Repo maintanance:
-----------------

* Repo and branch **upstream** should be from

    ```git svn clone https://svn.FreeBSD.org/ports/head/sysutils/py-salt salt-build-freebsd```
* `git svn rebase` to update local branch **upstream** (follows ports svn HEAD)
* Use standard git merge to maintain other local branches

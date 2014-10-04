--- setup.py.orig	2014-10-03 13:10:27.000000000 -0700
+++ setup.py	2014-10-03 23:27:43.010093118 -0700
@@ -666,13 +666,13 @@
                                     '*.flo'
                                     ]
                                 },
-                'data_files': [('share/man/man1',
+                'data_files': [('man/man1',
                                 ['doc/man/salt-cp.1',
                                  'doc/man/salt-call.1',
                                  'doc/man/salt-minion.1',
                                  'doc/man/salt-unity.1',
                                  ]),
-                               ('share/man/man7',
+                               ('man/man7',
                                 ['doc/man/salt.7',
                                  ]),
                                ],

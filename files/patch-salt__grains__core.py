--- salt/grains/core.py.orig	2014-10-03 23:23:07.591112328 -0700
+++ salt/grains/core.py	2014-10-03 23:23:34.663110325 -0700
@@ -1232,7 +1232,8 @@
     '''
     # Provides:
     #   path
-    return {'path': os.environ['PATH'].strip()}
+    return {'path': os.environ['PATH'].strip() +
+            ':/usr/local/bin:/usr/local/sbin'}
 
 
 def pythonversion():

--- salt/grains/core.py.orig	2014-09-16 16:31:27.506893540 -0700
+++ salt/grains/core.py	2014-09-16 16:36:12.310876906 -0700
@@ -1230,7 +1230,7 @@
     '''
     # Provides:
     #   path
-    return {'path': os.environ['PATH'].strip()}
+    return {'path': os.environ['PATH'].strip() + ':/usr/local/bin:/usr/local/sbin'}
 
 
 def pythonversion():

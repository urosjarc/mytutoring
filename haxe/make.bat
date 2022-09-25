@echo off

SET "JDK=C:\Program Files\Java\jdk-17.0.2\bin"
set "PATH=%JDK%;%PATH%"

haxelib install minimingw
haxelib install hxjava
haxelib install hxcpp
haxelib install hxnodejs

py make.py
haxe build.hxml
timeout /t 30

#!/usr/bin/tclsh

set arch "noarch"
set base "naviserver-mod_nsconf-1.0"

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb naviserver-mod_nsconf.spec]
exec >@stdout 2>@stderr {*}$buildit


#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-ftpserver
Version  : 1.0.0.m2
Release  : 2
URL      : https://github.com/apache/ftpserver/archive/1.0.0-M2.tar.gz
Source0  : https://github.com/apache/ftpserver/archive/1.0.0-M2.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftplet-api/1.0.0-M2/ftplet-api-1.0.0-M2.pom
Source2  : https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftplet-api/1.0.0/ftplet-api-1.0.0.jar
Source3  : https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftplet-api/1.0.0/ftplet-api-1.0.0.pom
Source4  : https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftpserver-core/1.0.0-M2/ftpserver-core-1.0.0-M2.pom
Source5  : https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftpserver-core/1.0.0/ftpserver-core-1.0.0.jar
Source6  : https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftpserver-core/1.0.0/ftpserver-core-1.0.0.pom
Source7  : https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftpserver-deprecated/1.0.0-M2/ftpserver-deprecated-1.0.0-M2.jar
Source8  : https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftpserver-deprecated/1.0.0-M2/ftpserver-deprecated-1.0.0-M2.pom
Source9  : https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftpserver-parent/1.0.0-M2/ftpserver-parent-1.0.0-M2.pom
Source10  : https://repo.maven.apache.org/maven2/org/apache/ftpserver/ftpserver-parent/1.0.0/ftpserver-parent-1.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 ICU
Requires: mvn-ftpserver-data = %{version}-%{release}
Requires: mvn-ftpserver-license = %{version}-%{release}

%description
The Apache FtpServer project team is proud to announce the release of
Apache FtpServer, version 1.0-M2

%package data
Summary: data components for the mvn-ftpserver package.
Group: Data

%description data
data components for the mvn-ftpserver package.


%package license
Summary: license components for the mvn-ftpserver package.
Group: Default

%description license
license components for the mvn-ftpserver package.


%prep
%setup -q -n ftpserver-1.0.0-M2

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-ftpserver
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-ftpserver/LICENSE.txt
cp distribution/LICENSE.slf4j.txt %{buildroot}/usr/share/package-licenses/mvn-ftpserver/distribution_LICENSE.slf4j.txt
cp distribution/LICENSE.springframework.txt %{buildroot}/usr/share/package-licenses/mvn-ftpserver/distribution_LICENSE.springframework.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftplet-api/1.0.0-M2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftplet-api/1.0.0-M2/ftplet-api-1.0.0-M2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftplet-api/1.0.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftplet-api/1.0.0/ftplet-api-1.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftplet-api/1.0.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftplet-api/1.0.0/ftplet-api-1.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-core/1.0.0-M2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-core/1.0.0-M2/ftpserver-core-1.0.0-M2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-core/1.0.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-core/1.0.0/ftpserver-core-1.0.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-core/1.0.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-core/1.0.0/ftpserver-core-1.0.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-deprecated/1.0.0-M2
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-deprecated/1.0.0-M2/ftpserver-deprecated-1.0.0-M2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-deprecated/1.0.0-M2
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-deprecated/1.0.0-M2/ftpserver-deprecated-1.0.0-M2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-parent/1.0.0-M2
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-parent/1.0.0-M2/ftpserver-parent-1.0.0-M2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-parent/1.0.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-parent/1.0.0/ftpserver-parent-1.0.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/ftpserver/ftplet-api/1.0.0-M2/ftplet-api-1.0.0-M2.pom
/usr/share/java/.m2/repository/org/apache/ftpserver/ftplet-api/1.0.0/ftplet-api-1.0.0.jar
/usr/share/java/.m2/repository/org/apache/ftpserver/ftplet-api/1.0.0/ftplet-api-1.0.0.pom
/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-core/1.0.0-M2/ftpserver-core-1.0.0-M2.pom
/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-core/1.0.0/ftpserver-core-1.0.0.jar
/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-core/1.0.0/ftpserver-core-1.0.0.pom
/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-deprecated/1.0.0-M2/ftpserver-deprecated-1.0.0-M2.jar
/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-deprecated/1.0.0-M2/ftpserver-deprecated-1.0.0-M2.pom
/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-parent/1.0.0-M2/ftpserver-parent-1.0.0-M2.pom
/usr/share/java/.m2/repository/org/apache/ftpserver/ftpserver-parent/1.0.0/ftpserver-parent-1.0.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-ftpserver/LICENSE.txt
/usr/share/package-licenses/mvn-ftpserver/distribution_LICENSE.slf4j.txt
/usr/share/package-licenses/mvn-ftpserver/distribution_LICENSE.springframework.txt

#%global debug_package %{nil}

Name:    sysbench
Version: 1.0.20
Release: 1
Summary: Scriptable database and system performance benchmark 
License: GPL2
URL:	 https://github.com/akopytov/sysbench
Source0: https://github.com/akopytov/sysbench/archive/%{name}-%{version}.tar.gz

BuildRequires: 	gcc libtool autoconf automake mariadb-devel libaio-devel libxslt ck-devel postgresql-devel 

%description
sysbench is a scriptable multi-threaded benchmark tool based on LuaJIT. It is most frequently used for database benchmarks, but can also be used to create arbitrarily complex workloads that do not involve a database server.

%prep
%setup -q -n %{name}-%{version}/

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%pre
%preun
%post
%postun

%check

%files
%license COPYING 
%doc README.md ChangeLog  
%{_bindir}/*
%{_docdir}/%{name}/*
/usr/share/%{name}/*

%changelog
* Sun Mar 29 2020 Wei Xiong <myeuler@163.com>
- Package init


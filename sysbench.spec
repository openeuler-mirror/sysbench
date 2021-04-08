Name:    sysbench
Version: 1.0.20
Release: 3
Summary: Scriptable database and system performance benchmark 
License: GPL2
URL:	 https://github.com/akopytov/sysbench
Source0: https://github.com/akopytov/sysbench/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: 	gcc libtool autoconf automake mariadb-devel libaio-devel libxslt ck-devel postgresql-devel luajit-devel

%description
sysbench is a scriptable multi-threaded benchmark tool based on LuaJIT. It is most frequently used for database benchmarks, but can also be used to create arbitrarily complex workloads that do not involve a database server.

%prep
%setup -q -n %{name}-%{version}/
# Use luajit-devel and ck-devel instead of embedded code
rm -r third_party/luajit/luajit/
rm -r third_party/concurrency_kit/ck/
rm -r third_party/cram/

%build
./autogen.sh
%configure --with-mysql \
           --with-pgsql \
           --with-system-ck \
           --with-system-luajit
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
%{_datadir}/%{name}/*

%changelog
* Thu Apr 08 2021 herengui <herengui@uniontech.com> - 1.0.20-3
- enable postgresql support

* Tue Oct 13 2020 liqingqing_1229 <liqingqing3@huawei.com>
- update source0

* Sun Mar 29 2020 Wei Xiong <myeuler@163.com>
- Package init


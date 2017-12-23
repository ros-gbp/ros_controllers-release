Name:           ros-kinetic-diff-drive-controller
Version:        0.13.2
Release:        0%{?dist}
Summary:        ROS diff_drive_controller package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_controllers/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-controller-interface
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-realtime-tools
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-urdf
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-interface
BuildRequires:  ros-kinetic-controller-manager
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-realtime-tools
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-urdf
BuildRequires:  ros-kinetic-xacro

%description
Controller for a differential drive mobile base.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Dec 23 2017 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.13.2-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.13.1-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.13.0-1
- Autogenerated by Bloom

* Thu Aug 10 2017 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.13.0-0
- Autogenerated by Bloom

* Sun Apr 23 2017 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.12.3-0
- Autogenerated by Bloom

* Wed Mar 08 2017 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.12.1-0
- Autogenerated by Bloom

* Wed Feb 15 2017 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.12.0-0
- Autogenerated by Bloom

* Tue Aug 16 2016 Bence Magyar <bence.magyar@pal-robotics.com> - 0.11.2-0
- Autogenerated by Bloom

* Mon May 23 2016 Bence Magyar <bence.magyar@pal-robotics.com> - 0.11.1-0
- Autogenerated by Bloom

* Tue May 03 2016 Bence Magyar <bence.magyar@pal-robotics.com> - 0.11.0-0
- Autogenerated by Bloom


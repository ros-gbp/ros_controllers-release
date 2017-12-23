Name:           ros-lunar-forward-command-controller
Version:        0.13.2
Release:        0%{?dist}
Summary:        ROS forward_command_controller package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_controllers/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-controller-interface
Requires:       ros-lunar-hardware-interface
Requires:       ros-lunar-realtime-tools
Requires:       ros-lunar-std-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-controller-interface
BuildRequires:  ros-lunar-hardware-interface
BuildRequires:  ros-lunar-realtime-tools
BuildRequires:  ros-lunar-std-msgs

%description
forward_command_controller

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sat Dec 23 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.13.2-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.13.1-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.13.0-1
- Autogenerated by Bloom

* Thu Aug 10 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.13.0-0
- Autogenerated by Bloom

* Sun Apr 23 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.12.3-0
- Autogenerated by Bloom

* Fri Apr 21 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.12.2-0
- Autogenerated by Bloom


Name:           ros-lunar-ros-controllers
Version:        0.13.0
Release:        1%{?dist}
Summary:        ROS ros_controllers package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/ros_controllers
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-diff-drive-controller
Requires:       ros-lunar-effort-controllers
Requires:       ros-lunar-force-torque-sensor-controller
Requires:       ros-lunar-forward-command-controller
Requires:       ros-lunar-gripper-action-controller
Requires:       ros-lunar-imu-sensor-controller
Requires:       ros-lunar-joint-state-controller
Requires:       ros-lunar-joint-trajectory-controller
Requires:       ros-lunar-position-controllers
Requires:       ros-lunar-rqt-joint-trajectory-controller
Requires:       ros-lunar-velocity-controllers
BuildRequires:  ros-lunar-catkin

%description
Library of ros controllers

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
* Mon Nov 06 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.13.0-1
- Autogenerated by Bloom

* Thu Aug 10 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.13.0-0
- Autogenerated by Bloom

* Sun Apr 23 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.12.3-0
- Autogenerated by Bloom

* Fri Apr 21 2017 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.12.2-0
- Autogenerated by Bloom


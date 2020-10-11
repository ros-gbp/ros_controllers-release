%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-ros-controllers
Version:        0.18.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros_controllers package

License:        BSD
URL:            http://ros.org/wiki/ros_controllers
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-noetic-ackermann-steering-controller
Requires:       ros-noetic-diff-drive-controller
Requires:       ros-noetic-effort-controllers
Requires:       ros-noetic-force-torque-sensor-controller
Requires:       ros-noetic-forward-command-controller
Requires:       ros-noetic-gripper-action-controller
Requires:       ros-noetic-imu-sensor-controller
Requires:       ros-noetic-joint-state-controller
Requires:       ros-noetic-joint-trajectory-controller
Requires:       ros-noetic-position-controllers
Requires:       ros-noetic-velocity-controllers
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Library of ros controllers

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Sun Oct 11 2020 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.18.0-1
- Autogenerated by Bloom

* Tue May 12 2020 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.17.0-1
- Autogenerated by Bloom

* Mon Apr 27 2020 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.16.1-1
- Autogenerated by Bloom


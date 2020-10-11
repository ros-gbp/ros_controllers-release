%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-joint-trajectory-controller
Version:        0.18.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS joint_trajectory_controller package

License:        BSD
URL:            https://github.com/ros-controls/ros_controllers/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-actionlib
Requires:       ros-noetic-angles
Requires:       ros-noetic-control-msgs
Requires:       ros-noetic-control-toolbox
Requires:       ros-noetic-controller-interface
Requires:       ros-noetic-hardware-interface
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-realtime-tools
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-trajectory-msgs
Requires:       ros-noetic-urdf
BuildRequires:  ros-noetic-actionlib
BuildRequires:  ros-noetic-angles
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-code-coverage
BuildRequires:  ros-noetic-control-msgs
BuildRequires:  ros-noetic-control-toolbox
BuildRequires:  ros-noetic-controller-interface
BuildRequires:  ros-noetic-controller-manager
BuildRequires:  ros-noetic-hardware-interface
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-realtime-tools
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-trajectory-msgs
BuildRequires:  ros-noetic-urdf
BuildRequires:  ros-noetic-xacro
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Controller for executing joint-space trajectories on a group of joints.

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


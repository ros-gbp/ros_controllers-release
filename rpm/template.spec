Name:           ros-lunar-gripper-action-controller
Version:        0.13.0
Release:        0%{?dist}
Summary:        ROS gripper_action_controller package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-actionlib
Requires:       ros-lunar-angles
Requires:       ros-lunar-cmake-modules
Requires:       ros-lunar-control-msgs
Requires:       ros-lunar-control-toolbox
Requires:       ros-lunar-controller-interface
Requires:       ros-lunar-controller-manager
Requires:       ros-lunar-hardware-interface
Requires:       ros-lunar-realtime-tools
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-trajectory-msgs
Requires:       ros-lunar-urdf
Requires:       ros-lunar-xacro
BuildRequires:  ros-lunar-actionlib
BuildRequires:  ros-lunar-angles
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cmake-modules
BuildRequires:  ros-lunar-control-msgs
BuildRequires:  ros-lunar-control-toolbox
BuildRequires:  ros-lunar-controller-interface
BuildRequires:  ros-lunar-controller-manager
BuildRequires:  ros-lunar-hardware-interface
BuildRequires:  ros-lunar-realtime-tools
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-trajectory-msgs
BuildRequires:  ros-lunar-urdf
BuildRequires:  ros-lunar-xacro

%description
The gripper_action_controller package

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
* Thu Aug 10 2017 Sachin Chitta <robot.moveit@gmail.com> - 0.13.0-0
- Autogenerated by Bloom

* Sun Apr 23 2017 Sachin Chitta <robot.moveit@gmail.com> - 0.12.3-0
- Autogenerated by Bloom

* Fri Apr 21 2017 Sachin Chitta <robot.moveit@gmail.com> - 0.12.2-0
- Autogenerated by Bloom


Name:           ros-kinetic-gripper-action-controller
Version:        0.13.0
Release:        1%{?dist}
Summary:        ROS gripper_action_controller package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-angles
Requires:       ros-kinetic-cmake-modules
Requires:       ros-kinetic-control-msgs
Requires:       ros-kinetic-control-toolbox
Requires:       ros-kinetic-controller-interface
Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-hardware-interface
Requires:       ros-kinetic-realtime-tools
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-trajectory-msgs
Requires:       ros-kinetic-urdf
Requires:       ros-kinetic-xacro
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-angles
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-control-msgs
BuildRequires:  ros-kinetic-control-toolbox
BuildRequires:  ros-kinetic-controller-interface
BuildRequires:  ros-kinetic-controller-manager
BuildRequires:  ros-kinetic-hardware-interface
BuildRequires:  ros-kinetic-realtime-tools
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-trajectory-msgs
BuildRequires:  ros-kinetic-urdf
BuildRequires:  ros-kinetic-xacro

%description
The gripper_action_controller package

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
* Mon Nov 06 2017 Sachin Chitta <robot.moveit@gmail.com> - 0.13.0-1
- Autogenerated by Bloom

* Thu Aug 10 2017 Sachin Chitta <robot.moveit@gmail.com> - 0.13.0-0
- Autogenerated by Bloom

* Sun Apr 23 2017 Sachin Chitta <robot.moveit@gmail.com> - 0.12.3-0
- Autogenerated by Bloom

* Wed Mar 08 2017 Sachin Chitta <robot.moveit@gmail.com> - 0.12.1-0
- Autogenerated by Bloom

* Wed Feb 15 2017 Sachin Chitta <robot.moveit@gmail.com> - 0.12.0-0
- Autogenerated by Bloom

* Tue Aug 16 2016 Sachin Chitta <robot.moveit@gmail.com> - 0.11.2-0
- Autogenerated by Bloom

* Mon May 23 2016 Sachin Chitta <robot.moveit@gmail.com> - 0.11.1-0
- Autogenerated by Bloom

* Tue May 03 2016 Sachin Chitta <robot.moveit@gmail.com> - 0.11.0-0
- Autogenerated by Bloom


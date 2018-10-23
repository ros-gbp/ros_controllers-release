Name:           ros-melodic-gripper-action-controller
Version:        0.14.2
Release:        0%{?dist}
Summary:        ROS gripper_action_controller package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-actionlib
Requires:       ros-melodic-angles
Requires:       ros-melodic-cmake-modules
Requires:       ros-melodic-control-msgs
Requires:       ros-melodic-control-toolbox
Requires:       ros-melodic-controller-interface
Requires:       ros-melodic-controller-manager
Requires:       ros-melodic-hardware-interface
Requires:       ros-melodic-realtime-tools
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-trajectory-msgs
Requires:       ros-melodic-urdf
Requires:       ros-melodic-xacro
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-angles
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-control-msgs
BuildRequires:  ros-melodic-control-toolbox
BuildRequires:  ros-melodic-controller-interface
BuildRequires:  ros-melodic-controller-manager
BuildRequires:  ros-melodic-hardware-interface
BuildRequires:  ros-melodic-realtime-tools
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-trajectory-msgs
BuildRequires:  ros-melodic-urdf
BuildRequires:  ros-melodic-xacro

%description
The gripper_action_controller package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Oct 23 2018 Sachin Chitta <robot.moveit@gmail.com> - 0.14.2-0
- Autogenerated by Bloom

* Tue Jun 26 2018 Sachin Chitta <robot.moveit@gmail.com> - 0.14.1-0
- Autogenerated by Bloom

* Fri Apr 27 2018 Sachin Chitta <robot.moveit@gmail.com> - 0.14.0-0
- Autogenerated by Bloom


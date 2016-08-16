Name:           ros-kinetic-force-torque-sensor-controller
Version:        0.11.2
Release:        0%{?dist}
Summary:        ROS force_torque_sensor_controller package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_controllers/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-controller-interface
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-hardware-interface
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-realtime-tools
Requires:       ros-kinetic-roscpp
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-controller-interface
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-hardware-interface
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-realtime-tools
BuildRequires:  ros-kinetic-roscpp

%description
Controller to publish state of force-torque sensors

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
* Tue Aug 16 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.11.2-0
- Autogenerated by Bloom

* Mon May 23 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.11.1-0
- Autogenerated by Bloom

* Tue May 03 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.11.0-0
- Autogenerated by Bloom


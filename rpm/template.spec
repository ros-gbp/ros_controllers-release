Name:           ros-melodic-ackermann-steering-controller
Version:        0.14.3
Release:        0%{?dist}
Summary:        ROS ackermann_steering_controller package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-melodic-controller-interface
Requires:       ros-melodic-diff-drive-controller
Requires:       ros-melodic-hardware-interface
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-realtime-tools
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-tf
Requires:       ros-melodic-urdf
BuildRequires:  boost-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-controller-interface
BuildRequires:  ros-melodic-controller-manager
BuildRequires:  ros-melodic-diff-drive-controller
BuildRequires:  ros-melodic-gazebo-ros
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-hardware-interface
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-realtime-tools
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-rosunit
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-urdf
BuildRequires:  ros-melodic-xacro

%description
Controller for a steer drive mobile base.

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
* Sat Feb 09 2019 Masaru Morita <p595201m@mail.kyutech.jp> - 0.14.3-0
- Autogenerated by Bloom


Name:           ros-melodic-effort-controllers
Version:        0.14.3
Release:        0%{?dist}
Summary:        ROS effort_controllers package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_controllers/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-angles
Requires:       ros-melodic-control-msgs
Requires:       ros-melodic-control-toolbox
Requires:       ros-melodic-controller-interface
Requires:       ros-melodic-forward-command-controller
Requires:       ros-melodic-realtime-tools
Requires:       ros-melodic-urdf
BuildRequires:  ros-melodic-angles
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-control-msgs
BuildRequires:  ros-melodic-control-toolbox
BuildRequires:  ros-melodic-controller-interface
BuildRequires:  ros-melodic-forward-command-controller
BuildRequires:  ros-melodic-realtime-tools
BuildRequires:  ros-melodic-urdf

%description
effort_controllers

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
* Sat Feb 09 2019 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.14.3-0
- Autogenerated by Bloom

* Tue Oct 23 2018 Bence Magyar <bence.magyar.robotics@gmail.com> - 0.14.2-0
- Autogenerated by Bloom

* Tue Jun 26 2018 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.14.1-0
- Autogenerated by Bloom

* Fri Apr 27 2018 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.14.0-0
- Autogenerated by Bloom


Name:           ros-indigo-effort-controllers
Version:        0.9.2
Release:        0%{?dist}
Summary:        ROS effort_controllers package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_controllers/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-angles
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-control-toolbox
Requires:       ros-indigo-controller-interface
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-forward-command-controller
Requires:       ros-indigo-realtime-tools
Requires:       ros-indigo-urdf
BuildRequires:  ros-indigo-angles
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-control-toolbox
BuildRequires:  ros-indigo-controller-interface
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-forward-command-controller
BuildRequires:  ros-indigo-realtime-tools
BuildRequires:  ros-indigo-urdf

%description
effort_controllers

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon May 04 2015 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.9.2-0
- Autogenerated by Bloom


Name:           ros-hydro-robot-web-tools
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS robot_web_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/robot_web_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-depthcloud-encoder
Requires:       ros-hydro-interactive-marker-proxy
Requires:       ros-hydro-mjpeg-server
Requires:       ros-hydro-ros-web-video
Requires:       ros-hydro-rosbridge-server
Requires:       ros-hydro-tf2-web-republisher
BuildRequires:  ros-hydro-catkin

%description
Robot Web Tools Metapackage and Top Level Launch Files

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Oct 21 2014 Russell Toris <rctoris@wpi.edu> - 0.0.2-0
- Autogenerated by Bloom

* Wed Aug 20 2014 Russell Toris <rctoris@wpi.edu> - 0.0.1-0
- Autogenerated by Bloom


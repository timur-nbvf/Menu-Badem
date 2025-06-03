{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.pip
    pkgs.git
    pkgs.unzip

    pkgs.gcc
    pkgs.libffi
    pkgs.openssl
    pkgs.cmake
    pkgs.python311Packages.setuptools
    pkgs.python311Packages.wheel
  ];
}

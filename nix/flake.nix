{
  description = "Aikoh's Waker Guide";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    flake-compat = {
      url = "github:edolstra/flake-compat";
      flake = false;
    };
  };

  outputs =
    {
      nixpkgs,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python =
          let
            packageOverrides = self: super: {
              mkdocs-material = super.mkdocs-material.overridePythonAttrs (old: rec {
                version = "9.6.17";
                src = pkgs.fetchFromGitHub {
                  owner = "squidfunk";
                  repo = "mkdocs-material";
                  tag = version;
                  hash = "sha256-yl5bc037gr3oAUH01uNvNj7fIe8ca2jH+yfWlgMImZE=";
                };
              });
            };
          in
          pkgs.python3.override {
            inherit packageOverrides;
            self = python;
          };
      in
      {
        devShells.deploy = pkgs.mkShellNoCC {
          packages = with pkgs; [
            (python.withPackages (python-pkgs: [
              python-pkgs.mkdocs-material
            ]))
            mask
          ];
        };

        devShells.default = pkgs.mkShellNoCC {
          packages = with pkgs; [
            (python.withPackages (python-pkgs: [
              python-pkgs.mkdocs-material
              python-pkgs.pillow
            ]))
            black
            ruff
            yaml-language-server
            mask
          ];
        };
      }
    );
}

{
  description = "University OOP project";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};

      myPython = pkgs.python313.withPackages (
        ps: with ps; [
          pytest
        ]
      );
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          myPython
        ];

        shellHook = ''
          echo "Python 3.13 dev environment ready!"
        '';
      };
    };
}

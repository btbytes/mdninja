{
  description = "MDNinja = markdown + jinja2 = beautiful HTML documents.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
  };

  outputs = { self, nixpkgs }:
    let
      # Systems supported
      allSystems = [
        "x86_64-linux" # 64-bit Intel/AMD Linux
        "aarch64-linux" # 64-bit ARM Linux
        "x86_64-darwin" # 64-bit Intel macOS
        "aarch64-darwin" # 64-bit ARM macOS
      ];

      # Helper to provide system-specific attributes
      forAllSystems = f: nixpkgs.lib.genAttrs allSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      packages = forAllSystems ({ pkgs }: {
        default =
          let
            python = pkgs.python39;
          in
          python.pkgs.buildPythonApplication {
            name = "mdninja";

            buildInputs = with python.pkgs; [ pip markdown jinja2 click ];

            src = ./.;
          };
      });
    };
}

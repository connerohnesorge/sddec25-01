# config.nix
let
  pkgs = import (builtins.fetchTarball "https://github.com/NixOS/nixpkgs/archive/refs/heads/nixos-unstable.tar.gz") {};
  mcp-servers = import (builtins.fetchTarball "https://github.com/natsukium/mcp-servers-nix/archive/refs/heads/main.tar.gz") {inherit pkgs;};
in
  mcp-servers.lib.mkConfig pkgs {
    programs = {
      playwright.enable = true;
      # Add more modules as needed
    };
  }

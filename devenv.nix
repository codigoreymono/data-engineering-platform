{ pkgs, ... }:

{
  languages.python = {
    enable = true;
    package = pkgs.python312;
  };

  packages = with pkgs; [
    uv
    ruff
    duckdb
  ];

  services.postgres = {
    enable = true;
    package = pkgs.postgresql_17;

    port = 5433;
    listen_addresses = "127.0.0.1";

    initialDatabases = [
      {
        name = "data_platform";
      }
    ];
  };
}


"Contains profile mappings used in the project"

from cosmos import profile_config


buy_box = ProfileConfig(
    profile_name="buy_box",
    target_name="dev",
    profiles_yml_filepath=buybox_path / "profiles.yml",
)

from dataclasses import dataclass
import tomllib

__all__ = ('TheHTTPConfig',)


@dataclass
class TheHTTPConfig:
    """Defines all configuration options for the app."""

    sync_on_start: bool
    """Toggles application command synchronization on startup."""

    logging_level: int
    """The logging level to use."""

    @classmethod
    def from_file(cls, toml_path: str) -> "TheHTTPConfig":
        """Loads the configuration from a TOML file."""
        with open(toml_path, 'rb') as f:
            data = tomllib.load(f)

        return cls(
            sync_on_start=data['bot']['sync_on_start'],
            logging_level=data['logging']['level'],
        )

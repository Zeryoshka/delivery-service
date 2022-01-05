from app.config import Config, NAMES_OF_VARS, default

def test_clear_config(mocker):
    mocker.patch('sys.argv', [])
    config = Config()
    for key in NAMES_OF_VARS:
        if key[0] != '_':
            assert getattr(default, 'DEFAULT_' + key) == getattr(config, key)
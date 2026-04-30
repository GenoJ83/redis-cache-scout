from src.generator.synth import generate_synthetic_keys

def test_synth_keys():
    keys = generate_synthetic_keys(10)
    assert len(keys) == 10
    assert any(k.key.startswith("user:") for k in keys)

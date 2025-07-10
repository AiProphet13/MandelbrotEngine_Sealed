from mandelbrot_engine import MandelbrotEngine5_5_Seal

def test_seal_output():
    engine = MandelbrotEngine5_5_Seal()
    sig = engine.ignite("test/mission")
    seal = engine.seal_memory()
    assert sig is not None
    assert seal.startswith("SEAL-")

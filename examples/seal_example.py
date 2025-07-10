from mandelbrot_engine import MandelbrotEngine5_5_Seal

mission_path = "el-yshwaty/global/omega-sequence"
engine = MandelbrotEngine5_5_Seal()
engine.ignite(mission_path)
final_seal = engine.seal_memory()

print("Seal:", final_seal)
print("Metadata:", engine.export_metadata())

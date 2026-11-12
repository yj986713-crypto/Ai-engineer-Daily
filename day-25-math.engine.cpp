import ctypes
import os
import platform
import numpy as np
import pandas as pd

def run_unified_pipeline():
    print("--- 🚀 Unified C++ / NumPy / Pandas Pipeline ---")

    # 1. Load the compiled C++ library automatically based on OS
    lib_name = "math_engine.dll" if platform.system() == "Windows" else "math_engine.so"
    lib_path = os.path.abspath(lib_name)

    if not os.path.exists(lib_path):
        print(f"❌ Error: '{lib_name}' not found. Compile math_engine.cpp first!")
        return

    cpp_lib = ctypes.CDLL(lib_path)

    # 2. Generate 100 student records using NumPy
    num_students = 100
    np.random.seed(42)
    
    student_ids = [f"STU-{1000 + i}" for i in range(1, num_students + 1)]
    math_scores = np.random.randint(40, 101, size=num_students, dtype=np.int32)
    physics_scores = np.random.randint(40, 101, size=num_students, dtype=np.int32)
    cs_scores = np.random.randint(40, 101, size=num_students, dtype=np.int32)

    # Prepare empty NumPy arrays to receive results from C++
    totals = np.zeros(num_students, dtype=np.int32)
    averages = np.zeros(num_students, dtype=np.float64)

    # 3. Define C++ argument pointer types
    cpp_lib.process_scores.argtypes = [
        np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags="C_CONTIGUOUS"),
        np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags="C_CONTIGUOUS"),
        np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags="C_CONTIGUOUS"),
        np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags="C_CONTIGUOUS"),
        np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
        ctypes.c_int
    ]

    # 4. Execute C++ calculation directly on NumPy memory
    cpp_lib.process_scores(math_scores, physics_scores, cs_scores, totals, averages, num_students)
    print("✅ C++ Engine finished processing all memory arrays!")

    # 5. Build and analyze the final table using Pandas
    df = pd.DataFrame({
        "Student_ID": student_ids,
        "Math": math_scores,
        "Physics": physics_scores,
        "CS": cs_scores,
        "Total": totals,
        "Average": np.round(averages, 2)
    })

    df["Status"] = np.where(df["Average"] >= 60.0, "PASS", "FAIL")

    print("\n--- 🏆 Top 5 Students (Processed via C++) ---")
    print(df.sort_values(by="Total", ascending=False).head(5).to_string(index=False))

    print(f"\n📊 Class Average: {df['Average'].mean():.2f}%")
    print(f"✅ Total Passed : {(df['Status'] == 'PASS').sum()} / {num_students}")

if __name__ == "__main__":
    run_unified_pipeline()
      

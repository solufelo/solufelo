<div align="center">
  <img width="220" height="220" alt="logo-helmet-TRANSPARENT_" src="https://github.com/user-attachments/assets/30a5bf5d-2482-484c-b3d3-b69a916ec540" />

  <h1>🌌 SOLOMON OLUFELO // CAPTAIN SOLO</h1>
  <p><strong>Systems Programmer • Engine & Tools Developer • Technical Artist</strong></p>
  <p><em>Low-level C++20 game architectures, runtime WebAssembly pipelines, and AAA studio tooling.</em></p>
  
  <p>
    <a href="https://solufelo.github.io/light-years-engine/" target="_blank">
      <img src="https://img.shields.io/badge/WASM_Engine-Live_Demo-00F5D4?style=for-the-badge&logo=webassembly&logoColor=black" alt="WASM Engine Live" />
    </a>
    <a href="https://solufelo.github.io/golden-hawks-helmet-shuffle/" target="_blank">
      <img src="https://img.shields.io/badge/Blender_Pipeline-Live_Showcase-FDB913?style=for-the-badge&logo=blender&logoColor=black" alt="Blender Pipeline" />
    </a>
    <a href="https://captainsolo.ca" target="_blank">
      <img src="https://img.shields.io/badge/Portfolio-captainsolo.ca-7928CA?style=for-the-badge" alt="Live Portfolio" />
    </a>
  </p>
</div>

---

> *"I write code where performance, determinism, and visual feedback converge. From custom C++20 game loops and zero-allocation memory pools to production Blender studio tooling and WebAssembly deployment, I build systems from the ground up."*

## 🧑‍💻 Who is Solomon Olufelo?

I'm **Solomon Olufelo**, a Computer Science student at **Wilfrid Laurier University** and dual US/Canadian citizen. 

Before transitioning into low-level systems and graphics programming, I ran a high-volume multimedia production business, completing **over 1,400+ paid freelance client orders** with a 4.8/5-star rating. Today, I combine that creative production background with rigorous systems engineering:

- **Game Engine Architecture**: Hand-crafting fixed-timestep loops, spatial hash broadphase partitioning, and SIMD-friendly memory structures in modern C++20.
- **Studio & Pipeline Tooling**: Building headless Python automation pipelines, 3D viewport trajectory visualizers, and runtime Unit Quaternion exporters for collegiate athletics and AAA game studio specifications.
- **Multi-Platform Deployment**: Shipping native Windows binaries (MSVC/CMake) alongside browser-embedded WebAssembly (Emscripten/SDL2) via automated CI/CD matrices.

---

## 💻 Technical Capabilities

### ⚙️ Systems, Engines & Low-Level
- **Languages**: `C++20`, `C`, `Python 3.11+`, `GLSL / Shaders`
- **Graphics & Frameworks**: `OpenGL 3.3`, `SDL2`, `WebAssembly (WASM / Emscripten)`, `Dear ImGui`
- **Architecture**: Fixed-timestep accumulators, zero-allocation pre-warmed object pools, spatial hash collision grids, Unit Quaternion math, memory profiling via `tracemalloc` and microsecond benchmarking
- **Build & Packaging**: `CMake`, `Ninja`, `vcpkg`, GitHub Actions CI/CD, Docker

### 🕸️ Interactive Platforms & Web Immersion
- **Frontend Core**: `React 19`, `Vite`, `Tailwind CSS v4`
- **3D & Animation**: `Three.js`, `React Three Fiber (R3F)`, `Drei`, `GSAP` (ScrollTrigger, Observer)
- **Services & Backend**: `Supabase`, `Stripe`, Linux VPS administration

---

## 🚀 Shipped & Verifiable Work

### 🌌 [Light Years Engine](https://github.com/solufelo/light-years-engine) • [Live Interactive Demo](https://solufelo.github.io/light-years-engine/)
Custom C++20 2D game engine running in the browser via Emscripten and SDL2:
- **Fixed 60 Hz Physics Loop**: Deterministic time accumulator with zero frame-rate dependency.
- **Broadphase Spatial Hash Grid**: Dynamically buckets colliding entities to drop collision overhead from $\mathcal{O}(N^2)$ to near $\mathcal{O}(N)$.
- **Zero-Allocation Particle & Bullet Pools**: Pre-warmed contiguous pools eliminating runtime heap allocations (`new`/`delete`) during active combat.
- **Dear ImGui Subsystem Profiler**: Real-time HUD tracking frame times, draw calls, active pool entity counts, and collision tests.
- **Automated CI/CD**: Dual-matrix GitHub Actions pipeline compiling both native Windows Desktop (MSVC) and WebAssembly (Emscripten).

### 🦅 [Golden Hawks Helmet Shuffle](https://github.com/solufelo/golden-hawks-helmet-shuffle) • [Live Showcase](https://solufelo.github.io/golden-hawks-helmet-shuffle/)
Production Blender 3D motion engine & AAA game studio tooling pipeline (v3.5.0):
- **Live Stadium Videoboard Operator**: 1-click Fitts's law setup generating venue geometry, volumetric lighting, continuous 60 FPS animation, and Apple ProRes 422 HQ / 4444 broadcast output in **75 ms**.
- **Camera-Normal Pitch Alignment (61.74°)**: Dynamic trigonometric incidence alignment between active camera and text center, eliminating all keystoning and foreshortening distortion.
- **Broadcast Sandwich Layout**: Network sports standard framing (+Y=0.58, center scale 0.68, -Y=-0.58) guaranteeing 0.26+ screen height units of air gap with **zero text overlap**.
- **AAA Runtime Track Serialization**: Exports per-frame Unit Quaternions `[w,x,y,z]`, velocity vectors, speed, and discrete event markers to structured JSON for Rockstar RAGE and Unreal Engine 5.
- **Headless Test Suite**: 9/9 automated tests passing headlessly via Blender 5.2.1 LTS CLI (35,000+ keys/sec throughput, +0.156 MB peak memory overhead, 0 leaks).

### 🌐 [captainsolo.ca](https://captainsolo.ca)
High-performance, theme-aware digital platform featuring React 19, interactive Three.js 3D viewport canvases, dynamic Liquid Glass shaders, and scroll-driven GSAP transitions.

---

## 📁 Repository Structure


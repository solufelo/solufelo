<div align="center">
  <img width="180" height="180" alt="Solomon Olufelo Logo" src="https://github.com/user-attachments/assets/30a5bf5d-2482-484c-b3d3-b69a916ec540" />

  <h1>Solomon Olufelo</h1>
  <p><strong>Systems Programmer • Engine & Tools Developer</strong></p>
  <p><em>Low-level C++20 game architectures, custom engine tooling, and WebAssembly pipelines.</em></p>

  <p>
    <a href="https://solufelo.github.io/light-years-engine/" target="_blank">
      <img src="https://img.shields.io/badge/WASM_Engine-Live_Demo-00F5D4?style=flat-square&logo=webassembly&logoColor=black" alt="WASM Engine Live" />
    </a>
    <a href="https://solufelo.github.io/golden-hawks-helmet-shuffle/" target="_blank">
      <img src="https://img.shields.io/badge/Blender_Pipeline-Live_Demo-FDB913?style=flat-square&logo=blender&logoColor=black" alt="Blender Pipeline" />
    </a>
    <a href="https://captainsolo.ca" target="_blank">
      <img src="https://img.shields.io/badge/Portfolio-captainsolo.ca-7928CA?style=flat-square" alt="Portfolio" />
    </a>
  </p>
</div>

---

### About Me
Computer Science student at **Wilfrid Laurier University** with a background running a commercial multimedia business (1,400+ client projects delivered). I build deterministic game systems, graphics pipelines, and studio automation tools from scratch.

---

### Featured Projects

#### 🌌 [Light Years Engine](https://github.com/solufelo/light-years-engine) • [Live Demo](https://solufelo.github.io/light-years-engine/)
Custom 2D C++20 engine targeting desktop and WebAssembly (Emscripten / SDL2).
- **Deterministic Loop:** Fixed 60 Hz physics accumulator independent of frame rate.
- **Spatial Hashing:** Broadphase collision grid dropping checks from $\mathcal{O}(N^2)$ to near $\mathcal{O}(N)$.
- **Memory Management:** Pre-warmed contiguous entity and particle pools—zero allocations during active loops.
- **Profiling & CI/CD:** Integrated Dear ImGui profiler; automated dual-target builds via GitHub Actions (MSVC & WASM).

#### 🦅 [Golden Hawks Helmet Shuffle](https://github.com/solufelo/golden-hawks-helmet-shuffle) • [Live Showcase](https://solufelo.github.io/golden-hawks-helmet-shuffle/)
Production Blender automation pipeline and runtime motion engine built for collegiate athletics.
- **CLI Pipeline:** Headless Python script generating 60 FPS arena videoboard assets in under 100 ms.
- **Clean Math:** Dynamic camera-normal pitch alignment (61.74°) eliminating text perspective distortion.
- **Runtime Serialization:** Exports per-frame Unit Quaternions `[w,x,y,z]` and velocity vectors to structured JSON for game engines.
- **Verified:** 9/9 automated tests passing headlessly via Blender CLI with zero memory leaks.

#### 🌐 [captainsolo.ca](https://captainsolo.ca)
Interactive portfolio built with React 19, Three.js / R3F viewports, and custom GLSL shaders.

---

### Core Stack
- **Systems & Graphics:** C++20, C, OpenGL 3.3, SDL2, WebAssembly (Emscripten), GLSL
- **Tooling & Profiling:** Python 3.11+, CMake, Ninja, vcpkg, Dear ImGui, Git/CI
- **Web & Interactive:** React 19, Three.js / R3F, Tailwind CSS, Linux VPS

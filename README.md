<div align="center">
  <img width="180" height="180" alt="Solomon Olufelo Logo" src="https://github.com/user-attachments/assets/30a5bf5d-2482-484c-b3d3-b69a916ec540" />

  <h1>Solomon Olufelo</h1>
  <p><strong>Systems Programmer • Engine & Tools Developer</strong></p>
  <p><em>Video engines, C++20 game systems, Blender pipeline tools, and AI apps that ship.</em></p>

  <p>
    <a href="https://unicreate-studio-demo.onrender.com">
      <img src="https://img.shields.io/badge/UniCreate_Studio-Live_Demo-FF4F64?style=flat-square&logo=ffmpeg&logoColor=white" alt="UniCreate Studio live demo" />
    </a>
    <a href="https://stepwhiz.onrender.com/app/">
      <img src="https://img.shields.io/badge/StepWhiz-Live_Demo-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="StepWhiz live demo" />
    </a>
    <a href="https://solufelo.github.io/light-years-engine/">
      <img src="https://img.shields.io/badge/WASM_Engine-Live_Demo-00F5D4?style=flat-square&logo=webassembly&logoColor=black" alt="Light Years Engine live demo" />
    </a>
    <a href="https://captainsolo.ca">
      <img src="https://img.shields.io/badge/Portfolio-captainsolo.ca-7928CA?style=flat-square" alt="Portfolio" />
    </a>
  </p>
</div>

---

### About Me
Student at **Wilfrid Laurier University** (computer science and film coursework), and a working videographer and web developer since 2020, including Video Assistant for Laurier Athletics since 2023. I build video engines, game systems and pipeline tools from scratch, and ship them with live demos.

---

### Featured Projects

#### 🎬 UniCreate Studio • [Live Demo](https://unicreate-studio-demo.onrender.com) • [Case Study](https://captainsolo.ca/work/unicreate-studio)
Drop in a shoot, get finished short-form clips: cut, captioned, checked and ready to post. A Python video engine behind a Next.js editor.
- **Engine:** transcribes on the local GPU (a 5-minute recording in 9.3 s on an RTX 4060 Ti), picks the moments, plans each clip as an EditSpec, and renders it with FFmpeg.
- **Preview equals export:** the editor runs TypeScript ports of the engine's motion, caption, colour and timeline code, with golden files checked byte for byte across both languages.
- **Broadcast-ready output:** cuts land on the 30 fps grid, sound stays locked to picture, and audio is mastered to −14 LUFS / −1 dBTP, in 9:16, 16:9, 1:1 and 4:5.
- **No database server:** the online demo runs the real Postgres schema and row-level security in-process with PGlite (WebAssembly).

#### 🌌 [Light Years Engine](https://github.com/solufelo/light-years-engine) • [Live Demo](https://solufelo.github.io/light-years-engine/)
A 2D game engine in C++20 with SDL2, built for Windows and the browser (WebAssembly via Emscripten).
- **Fixed-step loop:** 60 Hz physics accumulator, independent of frame rate.
- **Broadphase grid:** uniform 120 px cells cut collision checks from O(N²) to near O(N).
- **No heap on the hot path:** bullets and particles come from pools allocated at startup.
- **Tools and CI:** Dear ImGui profiler and animation inspector. GitHub Actions builds the MSVC and WebAssembly targets on every push and deploys the demo.

#### 🦅 Laurier Game Day • [Case Study](https://captainsolo.ca/work/laurier-gameday) • [Helmet Shuffle Repo](https://github.com/solufelo/golden-hawks-helmet-shuffle) • [Live Demo](https://solufelo.github.io/golden-hawks-helmet-shuffle/)
Videoboard and broadcast graphics for Laurier Golden Hawks football: the 2026 Senior Day opener, jumbotron games, 3D helmet renders and the live-stream scorebug.
- **Helmet Shuffle add-on:** a Blender tool that bakes a whole shell-game routine in under a quarter of a second. Three ProRes 422 HQ variants were rendered for the Oct 17, 2026 Senior Day game.
- **Readable type:** title and banner text tilt to face the camera, so their lines don't foreshorten.
- **Game-engine export:** per-frame unit quaternions [w, x, y, z], velocity vectors and Y-up positions as JSON.

#### 📚 StepWhiz • [Live Demo](https://stepwhiz.onrender.com/app/) • [Case Study](https://captainsolo.ca/work/stepwhiz)
AI study app: snap a problem, get a sourced step-by-step answer, then flashcards that make it stick.
- **One core, three apps:** a shared TypeScript and Preact client runs the web app (PWA), a Chrome extension and an Electron desktop app, against one zod-typed API contract.
- **Sourced answers:** a Fastify 5 API with a SQLite source library, running on a cloud model or a local one.
- **Tested:** 1,200+ unit tests and 260+ end-to-end checks.
- **Private by design:** no accounts, and study data stays on the device.

**Also built:** [captainsolo.ca](https://captainsolo.ca) (React 19 and Vite on Cloudflare Workers, 58 end-to-end checks) · [Suburbia](https://suburbia-solo.netlify.app/) (3D skateboard builder, Next.js + R3F) · [Velare](https://velare-site.netlify.app/) (3D motorcycle launch concept, three.js) · [CinemaVerse](https://cinemaverse-solo.netlify.app/) (social film log on live TMDB data) · [Captain Funds](https://captainfunds.netlify.app/) (fundraising platform)

---

### Core Stack
- **Systems & engine:** C++20, SDL2, Dear ImGui, WebAssembly (Emscripten), CMake, Ninja, vcpkg
- **Pipelines & tools:** Python, FFmpeg, faster-whisper, Blender add-ons (bpy), GitHub Actions
- **Apps & web:** TypeScript, React 19, Next.js, Preact, Fastify, PostgreSQL, SQLite, Electron, Chrome extensions, Three.js / R3F, Tailwind CSS, Cloudflare Workers
- **Video & motion:** Premiere Pro, After Effects, Blender

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>PEMDS</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@300;400&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg:        #080d14;
      --surface:   #0d1520;
      --surface2:  #111c2d;
      --border:    #1a2d45;
      --border2:   #243d5c;
      --text:      #e8edf5;
      --muted:     #4a6080;
      --blue:      #3b82f6;
      --blue-dim:  #1e3a5f;
      --blue-dark: #2563eb;
      --blue-glow: rgba(59,130,246,0.15);
      --green:     #34d399;
      --green-bg:  #052e1c;
      --green-bdr: #065f38;
      --red:       #f87171;
      --red-bg:    #2d0a0a;
      --red-bdr:   #7f1d1d;
      --sans:      'DM Sans', sans-serif;
      --mono:      'DM Mono', monospace;
      --r:         8px;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--sans);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      -webkit-font-smoothing: antialiased;
    }

    /* Subtle blue radial glow at top */
    body::before {
      content: '';
      position: fixed;
      top: -200px;
      left: 50%;
      transform: translateX(-50%);
      width: 600px;
      height: 400px;
      background: radial-gradient(ellipse, rgba(59,130,246,0.08) 0%, transparent 70%);
      pointer-events: none;
      z-index: 0;
    }

    /* Header */
    header {
      width: 100%;
      padding: 16px 40px;
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: relative;
      z-index: 1;
    }
    .logo {
      font-family: var(--mono);
      font-size: 13px;
      color: var(--blue);
      letter-spacing: 0.12em;
    }
    .header-center {
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
    }
    .school-logo {
      width: 44px;
      height: 44px;
      object-fit: contain;
      border-radius: 50%;
      opacity: 0.9;
    }
    .logo-sub {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--muted);
      letter-spacing: 0.05em;
    }

    /* Main */
    main {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 60px 20px;
      width: 100%;
      position: relative;
      z-index: 1;
    }

    /* Title */
    .title-block {
      text-align: center;
      margin-bottom: 40px;
      animation: up 0.5s ease both;
    }
    .title-tag {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--blue);
      letter-spacing: 0.18em;
      text-transform: uppercase;
      margin-bottom: 10px;
    }
    .title-main {
      font-size: clamp(26px, 4vw, 38px);
      font-weight: 300;
      color: var(--text);
      letter-spacing: -0.02em;
      line-height: 1.2;
    }
    .title-main strong { font-weight: 500; color: var(--blue); }
    .title-desc {
      margin-top: 8px;
      font-size: 14px;
      color: var(--muted);
      font-weight: 300;
    }

    @keyframes up {
      from { opacity: 0; transform: translateY(14px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    /* Card */
    .card {
      width: 100%;
      max-width: 500px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--r);
      animation: up 0.5s 0.1s ease both;
      box-shadow: 0 0 0 1px rgba(59,130,246,0.05), 0 8px 32px rgba(0,0,0,0.4);
    }
    .card-body { padding: 28px; }

    /* Drop zone */
    .dropzone {
      border: 1.5px dashed var(--border2);
      border-radius: var(--r);
      padding: 40px 20px;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s;
      position: relative;
    }
    .dropzone:hover, .dropzone.dragover {
      border-color: var(--blue);
      background: var(--blue-glow);
    }
    .dropzone input {
      position: absolute;
      inset: 0;
      opacity: 0;
      cursor: pointer;
      width: 100%;
      height: 100%;
    }
    .drop-icon {
      width: 42px; height: 42px;
      margin: 0 auto 14px;
      border: 1.5px solid var(--border2);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--blue);
      font-size: 18px;
      transition: all 0.2s;
    }
    .dropzone:hover .drop-icon {
      border-color: var(--blue);
      background: var(--blue-dim);
    }
    .drop-text { font-size: 14px; color: var(--text); font-weight: 300; }
    .drop-text span { color: var(--blue); font-weight: 400; }
    .drop-hint {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--muted);
      margin-top: 6px;
      letter-spacing: 0.04em;
    }

    /* File pill */
    .file-pill {
      display: none;
      align-items: center;
      gap: 10px;
      padding: 10px 14px;
      background: var(--blue-dim);
      border: 1px solid var(--blue-dark);
      border-radius: var(--r);
      margin-top: 14px;
      font-size: 13px;
    }
    .file-pill.show { display: flex; }
    .pill-name { color: var(--blue); font-weight: 500; flex: 1; }
    .pill-size { font-family: var(--mono); font-size: 11px; color: var(--muted); }

    /* Buttons */
    .btn {
      width: 100%;
      margin-top: 16px;
      padding: 13px;
      background: var(--blue);
      color: #fff;
      border: none;
      border-radius: var(--r);
      font-family: var(--sans);
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      transition: background 0.2s, box-shadow 0.2s, opacity 0.2s;
      letter-spacing: 0.01em;
    }
    .btn:hover {
      background: var(--blue-dark);
      box-shadow: 0 0 16px rgba(59,130,246,0.3);
    }
    .btn:disabled { opacity: 0.3; cursor: not-allowed; box-shadow: none; }

    .btn-ghost {
      width: 100%;
      margin-top: 10px;
      padding: 10px;
      background: transparent;
      color: var(--muted);
      border: 1px solid var(--border);
      border-radius: var(--r);
      font-family: var(--sans);
      font-size: 13px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-ghost:hover { border-color: var(--border2); color: var(--text); }

    /* Loading */
    .loading { display: none; padding: 20px 0 8px; text-align: center; }
    .loading.show { display: block; }
    .loading-text { font-size: 13px; color: var(--muted); margin-bottom: 12px; font-family: var(--mono); letter-spacing: 0.05em; }
    .progress { height: 1px; background: var(--border); border-radius: 2px; overflow: hidden; }
    .progress-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--blue-dark), var(--blue));
      animation: prog 2.5s ease-in-out forwards;
      box-shadow: 0 0 8px var(--blue);
    }
    @keyframes prog {
      0%  { width: 0%; }
      60% { width: 75%; }
      100%{ width: 92%; }
    }

    /* Result */
    .result { display: none; margin-top: 20px; }
    .result.show { display: block; animation: up 0.4s ease both; }

    .result-main {
      padding: 24px;
      border-radius: var(--r);
      text-align: center;
      margin-bottom: 14px;
    }
    .result-main.benign  { background: var(--green-bg); border: 1px solid var(--green-bdr); }
    .result-main.malware { background: var(--red-bg);   border: 1px solid var(--red-bdr); }

    .result-icon  { font-size: 22px; margin-bottom: 6px; }
    .result-label { font-size: 28px; font-weight: 500; letter-spacing: 0.06em; }
    .benign  .result-label { color: var(--green); }
    .malware .result-label { color: var(--red); }
    .result-conf  {
      font-family: var(--mono);
      font-size: 12px;
      color: var(--muted);
      margin-top: 4px;
      letter-spacing: 0.05em;
    }

    /* Meta */
    .meta {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 14px;
    }
    .meta-item {
      background: var(--surface2);
      border: 1px solid var(--border);
      border-radius: var(--r);
      padding: 12px 14px;
    }
    .meta-key {
      font-family: var(--mono);
      font-size: 10px;
      color: var(--muted);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 3px;
    }
    .meta-val {
      font-size: 13px;
      font-weight: 500;
      color: var(--text);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* Features */
    .feat-title {
      font-family: var(--mono);
      font-size: 10px;
      color: var(--muted);
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 8px;
    }
    .feat-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 7px 0;
      border-bottom: 1px solid var(--border);
      font-size: 13px;
    }
    .feat-row:last-child { border-bottom: none; }
    .feat-name { color: var(--muted); font-weight: 300; }
    .feat-val  { font-family: var(--mono); font-size: 12px; color: var(--blue); }

    /* Error */
    .error {
      display: none;
      margin-top: 14px;
      padding: 12px 14px;
      background: var(--red-bg);
      border: 1px solid var(--red-bdr);
      border-radius: var(--r);
      font-size: 13px;
      color: var(--red);
    }
    .error.show { display: block; }

    footer {
      padding: 24px;
      font-family: var(--mono);
      font-size: 11px;
      color: var(--muted);
      letter-spacing: 0.05em;
      position: relative;
      z-index: 1;
    }
  </style>
</head>
<body>

  <header>
    <div class="logo">PEMDS</div>
    <div class="header-center">
      <img src="/static/logo.png" alt="Suankularb Wittayalai Thonburi" class="school-logo"/>
    </div>
    <div class="logo-sub">SK-THONBURI.AC.TH</div>
  </header>

  <main>
    <div class="title-block">
      <div class="title-tag">Malware Detection System</div>
      <div class="title-main">Scan your <strong>PE file</strong></div>
      <div class="title-desc">Upload .exe .dll .sys — results in seconds</div>
    </div>

    <div class="card">
      <div class="card-body">

        <div class="dropzone" id="dropzone">
          <input type="file" id="fileInput" accept=".exe,.dll,.sys"/>
          <div class="drop-icon">↑</div>
          <div class="drop-text">Drop file here or <span>browse</span></div>
          <div class="drop-hint">.exe · .dll · .sys · max 50mb</div>
        </div>

        <div class="file-pill" id="filePill">
          <span>📄</span>
          <span class="pill-name" id="fileName">—</span>
          <span class="pill-size" id="fileSize"></span>
        </div>

        <button class="btn" id="btnScan" onclick="startScan()" disabled>Scan File</button>

        <div class="error" id="errorBox"></div>

        <div class="loading" id="loading">
          <div class="loading-text">analyzing file...</div>
          <div class="progress"><div class="progress-fill" id="progressFill"></div></div>
        </div>

        <div class="result" id="result"></div>

      </div>
    </div>
  </main>

  <footer>PEMDS · Portable Executable Malware Detection System</footer>

  <script>
    const fileInput = document.getElementById("fileInput");
    const dropzone  = document.getElementById("dropzone");
    const filePill  = document.getElementById("filePill");
    const fileName  = document.getElementById("fileName");
    const fileSize  = document.getElementById("fileSize");
    const btnScan   = document.getElementById("btnScan");
    const loading   = document.getElementById("loading");
    const result    = document.getElementById("result");
    const errorBox  = document.getElementById("errorBox");

    dropzone.addEventListener("dragover", e => { e.preventDefault(); dropzone.classList.add("dragover"); });
    dropzone.addEventListener("dragleave", () => dropzone.classList.remove("dragover"));
    dropzone.addEventListener("drop", e => {
      e.preventDefault();
      dropzone.classList.remove("dragover");
      if (e.dataTransfer.files[0]) { fileInput.files = e.dataTransfer.files; handleFile(e.dataTransfer.files[0]); }
    });
    fileInput.addEventListener("change", () => { if (fileInput.files[0]) handleFile(fileInput.files[0]); });

    function handleFile(file) {
      fileName.textContent = file.name;
      fileSize.textContent = (file.size / 1024).toFixed(1) + " KB";
      filePill.classList.add("show");
      btnScan.disabled = false;
      result.classList.remove("show");
      errorBox.classList.remove("show");
    }

    async function startScan() {
      const file = fileInput.files[0];
      if (!file) return;

      btnScan.disabled = true;
      loading.classList.add("show");
      result.classList.remove("show");
      errorBox.classList.remove("show");

      const fill = document.getElementById("progressFill");
      fill.style.animation = "none"; fill.offsetHeight; fill.style.animation = "";

      const fd = new FormData();
      fd.append("file", file);

      try {
        const res  = await fetch("/scan", { method: "POST", body: fd });
        const data = await res.json();
        loading.classList.remove("show");

        if (data.error) {
          errorBox.textContent = data.error;
          errorBox.classList.add("show");
          btnScan.disabled = false;
          return;
        }
        renderResult(data);
      } catch {
        loading.classList.remove("show");
        errorBox.textContent = "Cannot connect to server.";
        errorBox.classList.add("show");
        btnScan.disabled = false;
      }
    }

    function renderResult(data) {
      const isMalware = data.label === "MALWARE";
      const cls  = isMalware ? "malware" : "benign";
      const icon = isMalware ? "⚠️" : "✅";

      let featsHTML = "";
      if (data.top_features) {
        featsHTML = `
          <div class="feat-title">Top Feature Indicators</div>
          ${Object.entries(data.top_features).map(([k,v]) =>
            `<div class="feat-row"><span class="feat-name">${k}</span><span class="feat-val">${v}</span></div>`
          ).join("")}
        `;
      }

      result.innerHTML = `
        <div class="result-main ${cls}">
          <div class="result-icon">${icon}</div>
          <div class="result-label">${data.label}</div>
          <div class="result-conf">Confidence ${data.confidence}%</div>
        </div>
        <div class="meta">
          <div class="meta-item">
            <div class="meta-key">Filename</div>
            <div class="meta-val">${data.filename}</div>
          </div>
          <div class="meta-item">
            <div class="meta-key">File Size</div>
            <div class="meta-val">${data.file_size_kb} KB</div>
          </div>
        </div>
        ${featsHTML}
        <button class="btn-ghost" onclick="resetScan()">Scan another file</button>
      `;
      result.classList.add("show");
    }

    function resetScan() {
      fileInput.value = "";
      filePill.classList.remove("show");
      result.classList.remove("show");
      errorBox.classList.remove("show");
      btnScan.disabled = true;
    }
  </script>
</body>
</html>
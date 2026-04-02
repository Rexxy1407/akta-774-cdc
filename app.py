<!DOCTYPE html>
<html lang="ms">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard | Pemantauan Pendaftaran Akta 774</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>

    <style>
        /* ================================================================
           RESET & PEMBOLEHUBAH CSS GLOBAL
        ================================================================ */
        *, *::before, *::after {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            /* Palet Warna Utama */
            --teal:           #00897b;
            --teal-light:     #4db6ac;
            --teal-dark:      #00695c;
            --teal-glow:      rgba(0, 137, 123, 0.4);
            --navy:           #0d47a1;
            --navy-light:     #1565c0;
            --navy-dark:      #072f6b;
            --accent-cyan:    #00e5ff;
            --accent-warm:    #ffd54f;

            /* Glassmorphism */
            --glass-bg:       rgba(255, 255, 255, 0.075);
            --glass-bg-hover: rgba(255, 255, 255, 0.11);
            --glass-border:   rgba(255, 255, 255, 0.14);
            --glass-shadow:   0 12px 40px rgba(0, 0, 0, 0.4), 0 2px 0 rgba(255,255,255,0.06) inset;

            /* Teks */
            --teks-utama:     rgba(255, 255, 255, 0.96);
            --teks-kedua:     rgba(255, 255, 255, 0.65);
            --teks-perlahan:  rgba(255, 255, 255, 0.38);

            /* Status Warna */
            --warna-lengkap:  #00e676;
            --warna-amaran:   #ffd740;
            --warna-tamat:    #ff5252;

            /* Radius */
            --r-sm:  10px;
            --r-md:  16px;
            --r-lg:  22px;
            --r-xl:  30px;
        }

        html, body {
            height: 100%;
            font-family: 'DM Sans', sans-serif;
            color: var(--teks-utama);
            overflow: hidden;
        }

        /* ================================================================
           LATAR BELAKANG BERANIMASI
        ================================================================ */
        body {
            background: linear-gradient(135deg, #072f6b 0%, #00695c 40%, #0d47a1 70%, #00897b 100%);
            background-size: 400% 400%;
            animation: anjakGradien 14s ease infinite;
            position: relative;
        }

        @keyframes anjakGradien {
            0%   { background-position: 0%   50%; }
            50%  { background-position: 100% 50%; }
            100% { background-position: 0%   50%; }
        }

        /* Orb apungan - kedalaman visual */
        .orb {
            position: fixed;
            border-radius: 50%;
            filter: blur(90px);
            opacity: 0.22;
            pointer-events: none;
            z-index: 0;
        }
        .orb-1 {
            width: 650px; height: 650px;
            background: radial-gradient(circle, #00897b 0%, transparent 70%);
            top: -200px; left: -180px;
            animation: terapung1 20s ease-in-out infinite;
        }
        .orb-2 {
            width: 550px; height: 550px;
            background: radial-gradient(circle, #1565c0 0%, transparent 70%);
            bottom: -180px; right: -150px;
            animation: terapung2 24s ease-in-out infinite;
        }
        .orb-3 {
            width: 350px; height: 350px;
            background: radial-gradient(circle, #00e5ff 0%, transparent 70%);
            top: 40%; left: 50%;
            opacity: 0.09;
            animation: terapung3 16s ease-in-out infinite;
        }
        @keyframes terapung1 {
            0%, 100% { transform: translate(0px, 0px); }
            33%       { transform: translate(70px, 55px); }
            66%       { transform: translate(-35px, 90px); }
        }
        @keyframes terapung2 {
            0%, 100% { transform: translate(0px, 0px); }
            50%       { transform: translate(-70px, -55px); }
        }
        @keyframes terapung3 {
            0%, 100% { transform: translate(-50%, -50%) scale(1); }
            50%       { transform: translate(-50%, -50%) scale(1.3); }
        }

        /* Grid halus untuk tekstur */
        .grid-latar {
            position: fixed;
            inset: 0;
            background-image:
                linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
            background-size: 55px 55px;
            z-index: 0;
            pointer-events: none;
        }

        /* ================================================================
           SUSUN ATUR APLIKASI
        ================================================================ */
        .pembungkus-app {
            position: relative;
            z-index: 1;
            height: 100vh;
            display: flex;
            flex-direction: column;
            padding: 16px 20px;
            gap: 14px;
            overflow: hidden;
        }

        /* ================================================================
           PENGEPALA (HEADER)
        ================================================================ */
        .pengepala {
            background: var(--glass-bg);
            backdrop-filter: blur(24px) saturate(200%);
            -webkit-backdrop-filter: blur(24px) saturate(200%);
            border: 1px solid var(--glass-border);
            border-radius: var(--r-lg);
            padding: 14px 28px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--glass-shadow);
            flex-shrink: 0;
            animation: geluncur-turun 0.65s cubic-bezier(0.34, 1.56, 0.64, 1) both;
        }

        @keyframes geluncur-turun {
            from { opacity: 0; transform: translateY(-28px); }
            to   { opacity: 1; transform: translateY(0);      }
        }

        .pengepala-kiri {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .logo-sistem {
            width: 50px; height: 50px;
            background: linear-gradient(135deg, var(--teal), var(--accent-cyan));
            border-radius: 14px;
            display: flex; align-items: center; justify-content: center;
            font-size: 22px;
            box-shadow: 0 4px 18px var(--teal-glow);
            flex-shrink: 0;
            position: relative;
            overflow: hidden;
        }
        .logo-sistem::after {
            content: '';
            position: absolute;
            top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: linear-gradient(45deg, transparent 40%, rgba(255,255,255,0.15) 50%, transparent 60%);
            animation: kilatLogo 4s ease-in-out infinite;
        }
        @keyframes kilatLogo {
            0%, 80%, 100% { transform: translateX(-150%) rotate(45deg); }
            40%            { transform: translateX(150%) rotate(45deg);  }
        }

        .tajuk-sistem h1 {
            font-family: 'Sora', sans-serif;
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--teks-utama);
            letter-spacing: -0.025em;
            line-height: 1.25;
        }
        .tajuk-sistem h1 span {
            color: var(--accent-cyan);
        }
        .tajuk-sistem p {
            font-size: 0.72rem;
            color: var(--teks-kedua);
            font-weight: 400;
            margin-top: 2px;
            letter-spacing: 0.01em;
        }

        .pengepala-kanan {
            display: flex;
            align-items: center;
            gap: 18px;
        }

        /* Lencana 'Live' */
        .lencana-Live {
            display: flex;
            align-items: center;
            gap: 7px;
            background: rgba(0, 230, 118, 0.12);
            border: 1px solid rgba(0, 230, 118, 0.3);
            border-radius: 50px;
            padding: 5px 14px;
            font-size: 0.68rem;
            font-weight: 700;
            color: #00e676;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }
        .titik-nadi {
            width: 7px; height: 7px;
            background: #00e676;
            border-radius: 50%;
            animation: nadi 2s ease-in-out infinite;
        }
        @keyframes nadi {
            0%, 100% { opacity: 1; transform: scale(1);   box-shadow: 0 0 0 0 rgba(0,230,118,0.5);    }
            50%       { opacity: 0.6; transform: scale(0.75); box-shadow: 0 0 0 5px rgba(0,230,118,0); }
        }

        /* Paparan Jam */
        .paparan-jam {
            text-align: right;
            font-family: 'Sora', sans-serif;
        }
        .masa-jam {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--teks-utama);
            display: block;
            font-variant-numeric: tabular-nums;
            letter-spacing: 0.03em;
        }
        .tarikh-jam {
            font-size: 0.67rem;
            color: var(--teks-perlahan);
            display: block;
            margin-top: 1px;
        }

        /* Pembahagi menegak */
        .pembahagi-tegak {
            width: 1px;
            height: 36px;
            background: var(--glass-border);
        }

        /* ================================================================
           KANDUNGAN UTAMA
        ================================================================ */
        .kandungan-utama {
            display: grid;
            grid-template-columns: 400px 1fr;
            gap: 14px;
            flex: 1;
            min-height: 0;
            animation: pudar-masuk 0.7s ease 0.15s both;
        }

        @keyframes pudar-masuk {
            from { opacity: 0; transform: translateY(18px); }
            to   { opacity: 1; transform: translateY(0);    }
        }

        /* ================================================================
           KAD KACA (GLASS CARD)
        ================================================================ */
        .kad-kaca {
            background: var(--glass-bg);
            backdrop-filter: blur(22px) saturate(180%);
            -webkit-backdrop-filter: blur(22px) saturate(180%);
            border: 1px solid var(--glass-border);
            border-radius: var(--r-lg);
            box-shadow: var(--glass-shadow);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        .pengepala-kad {
            padding: 16px 22px 14px;
            border-bottom: 1px solid var(--glass-border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255, 255, 255, 0.03);
            flex-shrink: 0;
        }

        .tajuk-kad {
            display: flex;
            align-items: center;
            gap: 11px;
        }

        .ikon-kad {
            width: 38px; height: 38px;
            border-radius: 11px;
            display: flex; align-items: center; justify-content: center;
            font-size: 17px;
            flex-shrink: 0;
        }
        .ikon-teal { background: rgba(0, 137, 123, 0.25); border: 1px solid rgba(0, 137, 123, 0.4); }
        .ikon-biru { background: rgba(21, 101, 192, 0.25); border: 1px solid rgba(21, 101, 192, 0.45); }

        .tajuk-kad h2 {
            font-family: 'Sora', sans-serif;
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--teks-utama);
            letter-spacing: -0.01em;
        }
        .tajuk-kad p {
            font-size: 0.68rem;
            color: var(--teks-perlahan);
            margin-top: 1px;
        }

        /* ================================================================
           PANEL BORANG
        ================================================================ */
        .panel-borang .badan-kad {
            flex: 1;
            min-height: 0;
            overflow: hidden;
        }
        .panel-borang iframe {
            width: 100%;
            height: 100%;
            border: none;
            display: block;
            /* Penapisan cahaya untuk integrasi visual yang lebih baik */
            filter: brightness(0.97) hue-rotate(0deg);
        }

        /* ================================================================
           PANEL JADUAL
        ================================================================ */
        .panel-jadual {
            overflow: hidden;
        }

        /* Baris Statistik Ringkasan */
        .baris-statistik {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            padding: 14px 18px;
            border-bottom: 1px solid var(--glass-border);
            flex-shrink: 0;
        }

        .kad-stat {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: var(--r-sm);
            padding: 11px 14px;
            text-align: center;
            transition: background 0.2s, transform 0.2s;
            cursor: default;
        }
        .kad-stat:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateY(-2px);
        }

        .nombor-stat {
            font-family: 'Sora', sans-serif;
            font-size: 1.7rem;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 4px;
            letter-spacing: -0.04em;
        }
        .label-stat {
            font-size: 0.62rem;
            font-weight: 600;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            color: var(--teks-kedua);
        }

        .stat-jumlah  .nombor-stat { color: var(--accent-cyan); }
        .stat-lengkap .nombor-stat { color: var(--warna-lengkap); }
        .stat-amaran  .nombor-stat { color: var(--warna-amaran); }
        .stat-tamat   .nombor-stat { color: var(--warna-tamat); }

        /* ================================================================
           BUTANG KEMAS KINI
        ================================================================ */
        .btn-kemaskini {
            display: flex;
            align-items: center;
            gap: 7px;
            background: linear-gradient(135deg, var(--teal) 0%, var(--navy-light) 100%);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: var(--r-sm);
            padding: 8px 16px;
            color: white;
            font-family: 'DM Sans', sans-serif;
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 4px 14px rgba(0, 137, 123, 0.35);
            letter-spacing: 0.015em;
            white-space: nowrap;
        }
        .btn-kemaskini:hover {
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 8px 22px rgba(0, 137, 123, 0.5);
        }
        .btn-kemaskini:active { transform: scale(0.97); }
        .btn-kemaskini:disabled { opacity: 0.7; cursor: not-allowed; transform: none; }

        .ikon-putar {
            display: inline-block;
            font-size: 1rem;
            line-height: 1;
            transition: transform 0.3s;
        }
        .btn-kemaskini.memuat .ikon-putar {
            animation: putar 0.85s linear infinite;
        }
        @keyframes putar {
            from { transform: rotate(0deg); }
            to   { transform: rotate(360deg); }
        }

        /* Teks terakhir kemas kini */
        .teks-kemaskini {
            font-size: 0.68rem;
            color: var(--teks-perlahan);
            display: flex;
            align-items: center;
            gap: 5px;
            white-space: nowrap;
        }

        /* ================================================================
           BEKAS JADUAL
        ================================================================ */
        .bekas-jadual {
            flex: 1;
            overflow: auto;
            min-height: 0;
        }

        /* Jadual Data */
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.79rem;
        }

        thead {
            position: sticky;
            top: 0;
            z-index: 10;
        }

        thead th {
            background: rgba(7, 47, 107, 0.7);
            backdrop-filter: blur(12px);
            padding: 11px 15px;
            text-align: left;
            font-family: 'Sora', sans-serif;
            font-size: 0.62rem;
            font-weight: 700;
            letter-spacing: 0.07em;
            text-transform: uppercase;
            color: rgba(255, 255, 255, 0.62);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            white-space: nowrap;
        }
        thead th:first-child { text-align: center; width: 46px; }

        tbody tr {
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
            transition: background 0.18s;
        }
        tbody tr:hover { background: rgba(255, 255, 255, 0.055); }
        tbody tr:last-child { border-bottom: none; }

        tbody td {
            padding: 11px 15px;
            color: var(--teks-kedua);
            vertical-align: middle;
            white-space: nowrap;
        }

        .sel-no {
            font-family: 'Sora', sans-serif;
            font-weight: 600;
            color: var(--teks-perlahan);
            font-size: 0.72rem;
            text-align: center;
        }
        .sel-nama {
            font-weight: 600;
            color: var(--teks-utama);
            max-width: 180px;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* ================================================================
           LENCANA STATUS
        ================================================================ */
        .lencana-status {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 5px 12px;
            border-radius: 50px;
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.03em;
            white-space: nowrap;
        }

        .status-lengkap {
            background: rgba(0, 230, 118, 0.13);
            border: 1px solid rgba(0, 230, 118, 0.32);
            color: #69f0ae;
        }
        .status-amaran {
            background: rgba(255, 215, 64, 0.13);
            border: 1px solid rgba(255, 215, 64, 0.35);
            color: #ffd740;
        }
        .status-tamat {
            background: rgba(255, 82, 82, 0.15);
            border: 1px solid rgba(255, 82, 82, 0.38);
            color: #ff5252;
            animation: denyutTamat 2.2s ease-in-out infinite;
        }
        @keyframes denyutTamat {
            0%, 100% { box-shadow: 0 0 0 0 rgba(255, 82, 82, 0);    }
            50%       { box-shadow: 0 0 10px 2px rgba(255,82,82,0.18); }
        }
        .status-tidak-diketahui {
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: var(--teks-perlahan);
        }

        /* Hari berbaki */
        .hari-berbaki {
            font-family: 'Sora', sans-serif;
            font-weight: 700;
            font-size: 0.82rem;
            text-align: right;
        }
        .hari-tamat   { color: var(--warna-tamat); }
        .hari-amaran  { color: var(--warna-amaran); }
        .hari-lengkap { color: var(--warna-lengkap); }

        /* ================================================================
           KEADAAN: MEMUATKAN / KOSONG / RALAT
        ================================================================ */
        .keadaan-memuatkan,
        .keadaan-kosong,
        .keadaan-ralat {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 55px 30px;
            text-align: center;
            min-height: 200px;
        }

        .pusing-muat {
            width: 46px; height: 46px;
            border: 3px solid rgba(255, 255, 255, 0.1);
            border-top-color: var(--teal-light);
            border-radius: 50%;
            animation: putar 0.9s linear infinite;
            margin-bottom: 16px;
        }

        .keadaan-memuatkan p,
        .keadaan-kosong p,
        .keadaan-ralat p {
            color: var(--teks-kedua);
            font-size: 0.82rem;
            line-height: 1.6;
        }

        .ikon-ralat   { font-size: 2.8rem; margin-bottom: 12px; }
        .ikon-kosong  { font-size: 3rem; margin-bottom: 12px; opacity: 0.45; }
        .mesej-ralat  { color: var(--warna-tamat) !important; font-weight: 600; margin-bottom: 6px; }

        /* ================================================================
           PENGAKI (FOOTER)
        ================================================================ */
        .pengaki {
            text-align: center;
            padding: 8px 16px;
            font-size: 0.65rem;
            color: var(--teks-perlahan);
            letter-spacing: 0.03em;
            flex-shrink: 0;
        }
        .pengaki span { color: var(--teks-perlahan); opacity: 0.6; margin: 0 5px; }

        /* ================================================================
           TATAL (SCROLLBAR) TERSUAI
        ================================================================ */
        ::-webkit-scrollbar { width: 4px; height: 4px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.18); border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.32); }

        /* ================================================================
           RESPONSIF
        ================================================================ */
        @media (max-width: 1100px) {
            .kandungan-utama { grid-template-columns: 360px 1fr; }
        }
        @media (max-width: 880px) {
            html, body { overflow: auto; }
            .pembungkus-app { height: auto; overflow: visible; }
            .kandungan-utama { grid-template-columns: 1fr; height: auto; }
            .panel-borang .badan-kad { height: 620px; }
            .baris-statistik { grid-template-columns: repeat(2, 1fr); }
            .pengepala { flex-wrap: wrap; gap: 10px; }
        }
    </style>
</head>
<body>

    <!-- Elemen latar belakang dekoratif -->
    <div class="grid-latar"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <div class="pembungkus-app">

        <!-- ============================================================
             PENGEPALA SISTEM
        ============================================================ -->
        <header class="pengepala">
            <div class="pengepala-kiri">
                <div class="logo-sistem">🏥</div>
                <div class="tajuk-sistem">
                    <h1>Dashboard Pemantauan Status Pendaftaran <span>APC</span></h1>
                    <p>Pengamal Kesihatan Bersekutu (Akta 774) &bull; CDC Unit, Pejabat Kesihatan Daerah Timur Laut</p>
                </div>
            </div>

            <div class="pengepala-kanan">
                <div class="lencana-Live">
                    <span class="titik-nadi"></span>
                    Live
                </div>
                <div class="pembahagi-tegak"></div>
                <div class="paparan-jam">
                    <span class="masa-jam" id="masa-jam">--:--:--</span>
                    <span class="tarikh-jam" id="tarikh-jam">-- --- ----</span>
                </div>
            </div>
        </header>

        <!-- ============================================================
             KANDUNGAN UTAMA — BORANG (KIRI) + JADUAL (KANAN)
        ============================================================ -->
        <main class="kandungan-utama">

            <!-- ── PANEL KIRI: BORANG ENTRI DATA ───────────────── -->
            <div class="kad-kaca panel-borang">
                <div class="pengepala-kad">
                    <div class="tajuk-kad">
                        <div class="ikon-kad ikon-teal">📝</div>
                        <div>
                            <h2>Borang Entri Data</h2>
                            <p>Tambah atau kemaskini rekod PPKP</p>
                        </div>
                    </div>
                </div>
                <div class="badan-kad">
                    <!-- Borang Google Forms yang ditanam (embed) -->
                    <iframe
                        src="https://forms.gle/uEUSESzUaGPbDYvF7?embedded=true"
                        title="Borang Pendaftaran PPKP - Akta 774"
                        frameborder="0"
                        marginheight="0"
                        marginwidth="0"
                        loading="lazy"
                    >
                        Sedang memuatkan borang...
                    </iframe>
                </div>
            </div>

            <!-- ── PANEL KANAN: JADUAL PEMANTAUAN ──────────────── -->
            <div class="kad-kaca panel-jadual">

                <!-- Pengepala kad dengan butang kemas kini -->
                <div class="pengepala-kad">
                    <div class="tajuk-kad">
                        <div class="ikon-kad ikon-biru">📋</div>
                        <div>
                            <h2>Rekod Status Pendaftaran PPKP</h2>
                            <p>Pemantauan masa nyata — 9 Pembantu Kesihatan Awam</p>
                        </div>
                    </div>
                    <div style="display:flex; align-items:center; gap:12px;">
                        <span class="teks-kemaskini" id="teks-kemaskini">
                            🕐 Belum dikemas kini
                        </span>
                        <button class="btn-kemaskini" id="btn-kemaskini" onclick="muatData()">
                            <span class="ikon-putar">⟳</span>
                            Kemas Kini Jadual
                        </button>
                    </div>
                </div>

                <!-- Baris statistik ringkasan -->
                <div class="baris-statistik">
                    <div class="kad-stat stat-jumlah">
                        <div class="nombor-stat" id="stat-jumlah">—</div>
                        <div class="label-stat">Jumlah PPKP</div>
                    </div>
                    <div class="kad-stat stat-lengkap">
                        <div class="nombor-stat" id="stat-lengkap">—</div>
                        <div class="label-stat">✅ Lengkap</div>
                    </div>
                    <div class="kad-stat stat-amaran">
                        <div class="nombor-stat" id="stat-amaran">—</div>
                        <div class="label-stat">⏳ Perlu Tindakan</div>
                    </div>
                    <div class="kad-stat stat-tamat">
                        <div class="nombor-stat" id="stat-tamat">—</div>
                        <div class="label-stat">🔴 Tamat Tempoh</div>
                    </div>
                </div>

                <!-- Bekas utama jadual data -->
                <div class="bekas-jadual" id="bekas-jadual">
                    <!-- Keadaan permulaan: sedang memuatkan -->
                    <div class="keadaan-memuatkan">
                        <div class="pusing-muat"></div>
                        <p>Sedang memuatkan data daripada Google Sheets…</p>
                    </div>
                </div>

            </div>
        </main>

        <!-- ============================================================
             PENGAKI
        ============================================================ -->
        <footer class="pengaki">
            Sistem Pemantauan Pendaftaran PPKP
            <span>&bull;</span>
            CDC Unit, Pejabat Kesihatan Daerah Timur Laut
            <span>&bull;</span>
            Untuk Kegunaan Dalaman Sahaja
            <span>&bull;</span>
            &copy; 2025
        </footer>

    </div><!-- /.pembungkus-app -->


    <!-- ================================================================
         SKRIP JAVASCRIPT UTAMA
    ================================================================ -->
    <script>
        /* ================================================================
           SISTEM PEMANTAUAN PENDAFTARAN PPKP — AKTA 774
           CDC Unit, Pejabat Kesihatan Daerah Timur Laut
           ----------------------------------------------------------------
           Versi  : 2.0.0
           Tujuan : Memantau status APC 9 PPKP secara masa nyata
           Sumber : Google Sheets (CSV) via PapaParse
        ================================================================ */

        // ── Konfigurasi Aplikasi ────────────────────────────────────────
        const KONFIG = {
            // URL eksport CSV dari Google Sheets (sumber data Live)
            urlCsv: 'https://docs.google.com/spreadsheets/d/1V2m0Zd_YprRmtT5uVAUFv2MATYdAfMmgGbHAo24veBw/export?format=csv',

            // Senarai proksi CORS — dicuba mengikut urutan jika URL terus disekat
            proksiCors: [
                function(u) { return u; },
                function(u) { return 'https://corsproxy.io/?' + encodeURIComponent(u); },
                function(u) { return 'https://api.allorigins.win/raw?url=' + encodeURIComponent(u); },
                function(u) { return 'https://api.codetabs.com/v1/proxy?quest=' + u; }
            ],

            // Had hari untuk amaran (<=90 hari -> Perlu Tindakan)
            hadAmaran: 90,

            // Tempoh auto-muat semula (minit -> milisaat)
            selangAutoMuat: 5 * 60 * 1000,

            // Kata kunci untuk mengenal pasti lajur "Tarikh Tamat APC"
            // (tidak peka huruf besar/kecil)
            katakunciTarikh: ['tamat', 'apc', 'luput', 'expir', 'tamat tempoh', 'tarikh tamat']
        };

        // ── Pembolehubah Global ──────────────────────────────────────────
        let lajurTarikh = null; // Nama lajur tarikh tamat APC yang dikesan secara dinamik

        // ── JAM Live ─────────────────────────────────────────────────
        /**
         * Mengemas kini paparan jam dan tarikh setiap saat.
         * Menggunakan locale 'ms-MY' untuk format tempatan Malaysia.
         */
        function kemasJam() {
            const skrg  = new Date();
            const masa  = skrg.toLocaleTimeString('ms-MY', { hour12: false });
            const tarikh = skrg.toLocaleDateString('ms-MY', {
                day: '2-digit', month: 'long', year: 'numeric'
            });
            document.getElementById('masa-jam').textContent   = masa;
            document.getElementById('tarikh-jam').textContent = tarikh;
        }
        setInterval(kemasJam, 1000);
        kemasJam(); // Panggil serta-merta

        // ── PARSE TARIKH ─────────────────────────────────────────────────
        /**
         * Menukar rentetan tarikh kepada objek Date JavaScript.
         * Menyokong format yang lazim digunakan di Malaysia:
         *   - DD/MM/YYYY (paling lazim)
         *   - DD-MM-YYYY
         *   - YYYY-MM-DD (format ISO)
         *
         * @param {string} str - Rentetan tarikh untuk di-parse
         * @returns {Date|null} - Objek Date atau null jika tidak sah
         */
        function parseTarikh(str) {
            if (!str || String(str).trim() === '' || String(str).trim() === '-') return null;
            const s = String(str).trim();

            // Format DD/MM/YYYY — standard Malaysia
            let padanan = s.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/);
            if (padanan) {
                const [, hari, bulan, tahun] = padanan;
                const d = new Date(+tahun, +bulan - 1, +hari);
                return isNaN(d.getTime()) ? null : d;
            }

            // Format DD-MM-YYYY
            padanan = s.match(/^(\d{1,2})-(\d{1,2})-(\d{4})$/);
            if (padanan) {
                const [, hari, bulan, tahun] = padanan;
                const d = new Date(+tahun, +bulan - 1, +hari);
                return isNaN(d.getTime()) ? null : d;
            }

            // Format YYYY-MM-DD (ISO 8601)
            padanan = s.match(/^(\d{4})-(\d{2})-(\d{2})$/);
            if (padanan) {
                const d = new Date(s + 'T00:00:00');
                return isNaN(d.getTime()) ? null : d;
            }

            // Cuba parse generik sebagai usaha terakhir
            const d = new Date(s);
            return isNaN(d.getTime()) ? null : d;
        }

        // ── KIRAAN HARI BERBAKI ──────────────────────────────────────────
        /**
         * Mengira bilangan hari dari hari ini hingga tarikh tamat.
         * Nilai negatif bermakna sudah tamat tempoh.
         *
         * @param {string} tarikhStr - Rentetan tarikh tamat
         * @returns {number|null} - Bilangan hari atau null jika tarikh tidak sah
         */
        function kiraBakiHari(tarikhStr) {
            const tarikh = parseTarikh(tarikhStr);
            if (!tarikh) return null;
            const hariIni = new Date();
            hariIni.setHours(0, 0, 0, 0);
            return Math.floor((tarikh - hariIni) / (1000 * 60 * 60 * 24));
        }

        // ── PENENTU STATUS ───────────────────────────────────────────────
        /**
         * Menentukan status dan lencana berdasarkan bilangan hari berbaki.
         *
         * @param {number|null} hari - Bilangan hari berbaki
         * @returns {Object} - { labelLencana, kelasLencana, kelasHari, teksHari }
         */
        function tentukanStatus(hari) {
            if (hari === null) {
                return {
                    labelLencana: '❓ Tiada Data',
                    kelasLencana: 'status-tidak-diketahui',
                    kelasHari:    '',
                    teksHari:     '—'
                };
            }
            if (hari < 0) {
                return {
                    labelLencana: '🔴 TAMAT TEMPOH',
                    kelasLencana: 'status-tamat',
                    kelasHari:    'hari-tamat',
                    teksHari:     `${Math.abs(hari)} hari lalu`
                };
            }
            if (hari <= KONFIG.hadAmaran) {
                return {
                    labelLencana: '⏳ PERLU TINDAKAN',
                    kelasLencana: 'status-amaran',
                    kelasHari:    'hari-amaran',
                    teksHari:     `${hari} hari lagi`
                };
            }
            return {
                labelLencana: '✅ LENGKAP',
                kelasLencana: 'status-lengkap',
                kelasHari:    'hari-lengkap',
                teksHari:     `${hari} hari lagi`
            };
        }

        // ── KENAL PASTI LAJUR TARIKH ─────────────────────────────────────
        /**
         * Mengesan secara automatik lajur mana yang mengandungi
         * tarikh tamat APC berdasarkan senarai kata kunci.
         *
         * @param {string[]} pengepala - Senarai nama lajur dari CSV
         * @returns {string|null} - Nama lajur yang dikesan atau null
         */
        function kenalPastiLajurTarikh(pengepala) {
            for (const hdr of pengepala) {
                const hdrKecil = String(hdr).toLowerCase();
                for (const kata of KONFIG.katakunciTarikh) {
                    if (hdrKecil.includes(kata)) {
                        return hdr;
                    }
                }
            }
            return null;
        }

        // ── KEMAS KINI STATISTIK ─────────────────────────────────────────
        /**
         * Mengira dan memaparkan statistik ringkasan untuk semua rekod.
         *
         * @param {Object[]} data - Senarai rekod yang diproses
         */
        function kemasKiniStatistik(data) {
            let jumlah = data.length;
            let lengkap = 0, amaran = 0, tamat = 0;

            data.forEach(baris => {
                const hari = lajurTarikh ? kiraBakiHari(baris[lajurTarikh]) : null;
                if (hari === null) return;
                if (hari < 0)                    tamat++;
                else if (hari <= KONFIG.hadAmaran) amaran++;
                else                              lengkap++;
            });

            // Papar dengan animasi counter
            animasiAngka('stat-jumlah',  jumlah);
            animasiAngka('stat-lengkap', lengkap);
            animasiAngka('stat-amaran',  amaran);
            animasiAngka('stat-tamat',   tamat);
        }

        // ── ANIMASI COUNTER ──────────────────────────────────────────────
        /**
         * Animasi pertambahan nombor dari 0 ke nilai akhir.
         *
         * @param {string} idElemen - ID elemen HTML
         * @param {number} nilaiAkhir - Nilai destinasi
         */
        function animasiAngka(idElemen, nilaiAkhir) {
            const elemen = document.getElementById(idElemen);
            if (!elemen) return;
            const tempoh = 750, selang = 14;
            const bilLangkah = tempoh / selang;
            let langkah = 0;
            const jeda = setInterval(() => {
                langkah++;
                // Fungsi kemudahan "ease-out"
                const kemajuan = 1 - Math.pow(1 - langkah / bilLangkah, 3);
                elemen.textContent = Math.round(kemajuan * nilaiAkhir);
                if (langkah >= bilLangkah) {
                    elemen.textContent = nilaiAkhir;
                    clearInterval(jeda);
                }
            }, selang);
        }

        // ── ESCAPE HTML ──────────────────────────────────────────────────
        /**
         * Melarikan aksara khas HTML untuk mengelak XSS.
         *
         * @param {*} nilai - Nilai untuk dilarikan
         * @returns {string} - Rentetan yang selamat untuk dimasukkan ke HTML
         */
        function escHtml(nilai) {
            return String(nilai ?? '—')
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
        }

        // ── RENDER JADUAL ────────────────────────────────────────────────
        /**
         * Menjana dan memaparkan jadual data HTML berdasarkan rekod CSV.
         * Secara dinamik mencipta lajur berdasarkan pengepala sebenar
         * dalam Google Sheets, dan menambah lajur "Hari Berbaki" & "Status"
         * yang dikira secara automatik.
         *
         * @param {Object[]} data     - Senarai rekod data
         * @param {string[]} pengepala - Nama-nama lajur (dari CSV)
         */
        function renderJadual(data, pengepala) {
            const bekas = document.getElementById('bekas-jadual');

            // ── Keadaan kosong: tiada rekod ──────────────────────────
            if (!data || data.length === 0) {
                bekas.innerHTML = `
                    <div class="keadaan-kosong">
                        <div class="ikon-kosong">📂</div>
                        <p><strong>Tiada rekod dijumpai.</strong></p>
                        <p style="margin-top:6px; font-size:0.75rem; color:var(--teks-perlahan);">
                            Sila tambah rekod PPKP menggunakan borang di sebelah kiri,<br>
                            kemudian klik "Kemas Kini Jadual" untuk menyegarkan data.
                        </p>
                    </div>
                `;
                return;
            }

            // ── Bina pengepala jadual ────────────────────────────────
            let htmlPengepala = '<th>No.</th>';
            pengepala.forEach(hdr => {
                htmlPengepala += `<th>${escHtml(hdr)}</th>`;
            });
            // Lajur tambahan yang dikira
            if (lajurTarikh) {
                htmlPengepala += '<th style="text-align:right;">Hari Berbaki</th>';
            }
            htmlPengepala += '<th>Status Pendaftaran</th>';

            // ── Bina baris data ──────────────────────────────────────
            let htmlBaris = '';
            data.forEach((baris, i) => {
                const hari   = lajurTarikh ? kiraBakiHari(baris[lajurTarikh]) : null;
                const status = tentukanStatus(hari);

                // Sel-sel bagi setiap lajur dari Google Sheets
                let htmlSel = `<td class="sel-no">${i + 1}</td>`;
                pengepala.forEach((hdr, j) => {
                    const nilai    = baris[hdr] !== undefined && baris[hdr] !== '' ? baris[hdr] : '—';
                    const kelaSel  = j === 0 ? 'sel-nama' : '';
                    htmlSel += `<td class="${kelaSel}">${escHtml(nilai)}</td>`;
                });

                // Sel hari berbaki (dikira)
                if (lajurTarikh) {
                    htmlSel += `
                        <td style="text-align:right;">
                            <span class="hari-berbaki ${status.kelasHari}">${escHtml(status.teksHari)}</span>
                        </td>`;
                }

                // Sel lencana status
                htmlSel += `
                    <td>
                        <span class="lencana-status ${status.kelasLencana}">${status.labelLencana}</span>
                    </td>`;

                htmlBaris += `<tr>${htmlSel}</tr>`;
            });

            // ── Pasang ke DOM ────────────────────────────────────────
            bekas.innerHTML = `
                <table>
                    <thead><tr>${htmlPengepala}</tr></thead>
                    <tbody>${htmlBaris}</tbody>
                </table>
            `;
        }

        // ── FUNGSI PEMBANTU: CUBA SATU URL PROKSI ───────────────────────
        /**
         * Cuba mengambil CSV dari satu URL (terus atau melalui proksi).
         * Mengembalikan Promise yang resolve dengan { data, meta }
         * atau reject jika gagal atau data kosong/tidak sah.
         *
         * @param {string} url - URL yang akan dicuba
         * @returns {Promise<{data, meta}>}
         */
        function cubaAmbilCsv(url) {
            return new Promise(function(resolve, reject) {
                var tamatMasa = setTimeout(function() {
                    reject(new Error('Tamat masa (timeout)'));
                }, 12000); // 12 saat had masa

                Papa.parse(url, {
                    download:       true,
                    header:         true,
                    skipEmptyLines: true,
                    complete: function(keputusan) {
                        clearTimeout(tamatMasa);
                        // Sahkan bahawa data yang diterima adalah CSV yang sah
                        if (!keputusan.meta || !keputusan.meta.fields || keputusan.meta.fields.length === 0) {
                            reject(new Error('Data CSV tidak sah atau kosong'));
                            return;
                        }
                        resolve(keputusan);
                    },
                    error: function(ralat) {
                        clearTimeout(tamatMasa);
                        reject(new Error(ralat.message || 'Ralat PapaParse'));
                    }
                });
            });
        }

        // ── FUNGSI UTAMA: MUAT DATA (DENGAN SANDARAN PROKSI CORS) ────────
        /**
         * Mengambil data CSV dari Google Sheets menggunakan PapaParse.
         * Secara automatik mencuba senarai proksi CORS jika URL terus disekat,
         * memastikan dashboard berfungsi dalam semua persekitaran pelayar.
         *
         * Urutan percubaan:
         *   1. URL terus (berfungsi apabila dihoskan di pelayan web)
         *   2. corsproxy.io
         *   3. allorigins.win
         *   4. codetabs.com
         */
        async function muatData() {
            var btn            = document.getElementById('btn-kemaskini');
            var bekas          = document.getElementById('bekas-jadual');
            var teksKemaskini  = document.getElementById('teks-kemaskini');

            // ── Tunjukkan animasi memuatkan ──────────────────────────
            btn.classList.add('memuat');
            btn.disabled = true;
            bekas.innerHTML = `
                <div class="keadaan-memuatkan">
                    <div class="pusing-muat"></div>
                    <p>Sedang mengambil data daripada Google Sheets&hellip;<br>
                    <span style="font-size:0.72rem; color:var(--teks-perlahan);">Sila tunggu sebentar.</span></p>
                </div>
            `;

            var urlAsas   = KONFIG.urlCsv + '&cacheBust=' + Date.now();
            var senaraiFn = KONFIG.proksiCors;
            var keputusan = null;
            var ralaatAkhir = null;
            var proksiDigunakan = 'terus';

            // ── Cuba setiap proksi mengikut urutan ───────────────────
            for (var i = 0; i < senaraiFn.length; i++) {
                var urlCuba = senaraiFn[i](urlAsas);
                var namaProksi = ['Terus', 'corsproxy.io', 'allorigins.win', 'codetabs.com'][i];

                // Kemas kini mesej pemuatan dengan proksi semasa
                var elMuat = bekas.querySelector('p');
                if (elMuat) {
                    elMuat.innerHTML = 'Sedang mengambil data&hellip; <span style="font-size:0.7rem;color:var(--teks-perlahan);">Cuba: ' + namaProksi + '</span>';
                }

                try {
                    console.log('[PPKP] Cuba proksi ' + (i + 1) + '/' + senaraiFn.length + ': ' + namaProksi);
                    keputusan = await cubaAmbilCsv(urlCuba);
                    proksiDigunakan = namaProksi;
                    console.log('[PPKP] Berjaya melalui: ' + namaProksi);
                    break; // Berjaya — hentikan percubaan
                } catch (e) {
                    console.warn('[PPKP] Gagal (' + namaProksi + '):', e.message);
                    ralaatAkhir = e;
                    keputusan   = null;
                }
            }

            // ── Semua proksi gagal ───────────────────────────────────
            if (!keputusan) {
                console.error('[PPKP Dashboard] Semua proksi gagal. Ralat terakhir:', ralaatAkhir);
                bekas.innerHTML = `
                    <div class="keadaan-ralat">
                        <div class="ikon-ralat">&#9888;&#65039;</div>
                        <p class="mesej-ralat">Gagal Memuatkan Data</p>
                        <p>
                            Tidak dapat menyambung ke Google Sheets selepas mencuba<br>
                            ${senaraiFn.length} kaedah sambungan. Kemungkinan sebab:
                        </p>
                        <ul style="text-align:left; margin:10px auto; max-width:340px; font-size:0.78rem; color:var(--teks-kedua); line-height:1.9;">
                            <li>Google Sheets belum ditetapkan sebagai <strong>"Kongsi kepada semua orang"</strong></li>
                            <li>Tiada sambungan internet</li>
                            <li>Pelayar menyekat semua proksi CORS</li>
                        </ul>
                        <p style="margin-top:6px; font-size:0.7rem; color:var(--teks-perlahan); background:rgba(255,82,82,0.08); border:1px solid rgba(255,82,82,0.2); border-radius:8px; padding:8px 14px;">
                            Ralat: ${escHtml(ralaatAkhir ? ralaatAkhir.message : 'Tidak diketahui')}
                        </p>
                    </div>
                `;
                teksKemaskini.innerHTML = '<span style="color:var(--warna-tamat);">&#9888;&#65039; Gagal dikemas kini</span>';
                btn.classList.remove('memuat');
                btn.disabled = false;
                return;
            }

            // ── Proses dan papar data yang berjaya diambil ───────────
            try {
                var data      = keputusan.data;
                var pengepala = keputusan.meta.fields || [];

                // Kesan lajur tarikh tamat APC secara automatik
                lajurTarikh = kenalPastiLajurTarikh(pengepala);

                // Render jadual data
                renderJadual(data, pengepala);

                // Kemas kini statistik ringkasan
                kemasKiniStatistik(data);

                // Kemas kini cap masa terakhir dikemas kini
                var skrg    = new Date();
                var masaStr = skrg.toLocaleTimeString('ms-MY', { hour12: false });
                teksKemaskini.innerHTML = `&#128336; Dikemas kini: <strong>${masaStr}</strong>`;

            } catch (e) {
                console.error('[PPKP] Ralat semasa memproses data:', e);
            } finally {
                btn.classList.remove('memuat');
                btn.disabled = false;
            }
        }

        // ── PERMULAAN APLIKASI ───────────────────────────────────────────
        // Muat data secara automatik setelah DOM siap dimuatkan
        document.addEventListener('DOMContentLoaded', function () {
            muatData();
        });

        // Auto-muat semula setiap 5 minit untuk memastikan data segar
        setInterval(muatData, KONFIG.selangAutoMuat);

        /* ================================================================
           AKHIR SKRIP — Sistem Pemantauan Akta 774
        ================================================================ */
    </script>

</body>
</html>
```

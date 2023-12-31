#!/usr/bin/env python

import string

li = [
    "E ",
    "e ",
    "Ë ",
    "ë ",
    "O ",
    "o ",
    "A ",
    " T",
    " t",
    " A",
    " d",
    "të",
    "T ",
    "ea",
    "D ",
    "r ",
    "TA",
    "t ",
    "R ",
    "ST",
    " e",
    "st",
    " C",
    "re",
    "te",
    "ta",
    "LA",
    "AS",
    " V",
    " W",
    " c",
    "et",
    "SZ",
    " v",
    "sz",
    "nt",
    ", ",
    "ra",
    "OV",
    "ov",
    "AT",
    ". ",
    "RA",
    " w",
    "ge",
    "DA",
    "L ",
    "KO",
    " O",
    "Ă ",
    "CO",
    "TO",
    "TT",
    "OW",
    "tt",
    "ko",
    "VA",
    "ow",
    "at",
    " o",
    "co",
    "SA",
    "Í ",
    "í ",
    "to",
    "AA",
    "JA",
    " J",
    "YA",
    " f",
    "K ",
    " Z",
    "KA",
    "ka",
    "Ā ",
    " G",
    "PA",
    "AU",
    "ų ",
    "ij",
    "ro",
    "RO",
    "va",
    " z",
    "WA",
    "Y ",
    " j",
    "GY",
    "y ",
    "W ",
    "ze",
    " Y",
    "ya",
    "CZ",
    " g",
    "ke",
    " Î",
    "RZ",
    "cz",
    "rz",
    "Ä ",
    "gy",
    "EG",
    "TÄ",
    "wa",
    "ve",
    " y",
    "LO",
    "w ",
    "TĀ",
    "AV",
    " î",
    "ce",
    "CA",
    "LT",
    "of",
    "V ",
    "AY",
    "LU",
    "KU",
    "za",
    "F ",
    "rd",
    "în",
    "GA",
    "f ",
    "YC",
    "ca",
    "ga",
    "ÃO",
    "ku",
    "OJ",
    "v ",
    "nj",
    "KS",
    "fo",
    "TÁ",
    "FO",
    "ks",
    "av",
    "AŠ",
    "ZY",
    "zy",
    "VO",
    "tä",
    "yc",
    "FÖ",
    "fö",
    "AC",
    "Å ",
    "rë",
    "OA",
    "AG",
    "UA",
    "LY",
    "vo",
    "TĂ",
    "tā",
    "r.",
    "Z ",
    "z ",
    "RT",
    "L'",
    "É ",
    "é ",
    "we",
    "ny",
    "OT",
    "ay",
    " é",
    "EJ",
    "DZ",
    "lj",
    "af",
    "WY",
    "LJ",
    "ÓW",
    "RU",
    "ÁS",
    "gj",
    "BA",
    "rt",
    "vv",
    "T,",
    "go",
    "ÁT",
    "DÁ",
    "ĀS",
    "aj",
    "ów",
    "JĀ",
    "ře",
    "ot",
    "TS",
    "tá",
    "VÁ",
    "AW",
    "EC",
    "AJ",
    "WO",
    "PÅ",
    "KÖ",
    "VÄ",
    "'A",
    "ev",
    "ÝC",
    "T.",
    "ké",
    "ÁV",
    "kā",
    "TY",
    "RY",
    "tă",
    "ez",
    "ts",
    "wo",
    "ł ",
    "BY",
    "ye",
    "ty",
    "Ł ",
    "À ",
    " Q",
    "KĀ",
    "kö",
    "rā",
    "ĀT",
    "ly",
    "ré",
    "EV",
    "ŁY",
    "CĂ",
    "té",
    " q",
    "VĀ",
    "rs",
    "ný",
    "ŁO",
    " À",
    "vd",
    "ýc",
    "că",
    "ÄT",
    "Ą ",
    "S,",
    "by",
    "A.",
    "RS",
    "FA",
    "AŞ",
    "kë",
    "ŁA",
    "KT",
    "rá",
    "O,",
    "YM",
    "fe",
    "ZO",
    "Ý ",
    "ZT",
    "SÁ",
    "SÄ",
    "s,",
    "RĀ",
    "ła",
    "kt",
    "AO",
    "aw",
    "PĀ",
    "DT",
    "r,",
    "vá",
    " 1",
    "AÇ",
    "PÄ",
    "rg",
    "YO",
    "ÉG",
    "e,",
    "TÀ",
    "DJ",
    "zo",
    "VÆ",
    "ý ",
    "ĄC",
    "vä",
    "vē",
    "ĂT",
    "ÁG",
    "VÕ",
    "Á ",
    "vě",
    "zá",
    "ÄY",
    "Ta",
    " Á",
    "o,",
    "ÇÃ",
    "ŠA",
    "ry",
    "DY",
    "LG",
    "LÄ",
    "Ę ",
    "ę ",
    "Y,",
    "LV",
    "PĂ",
    "Ve",
    "Ě ",
    "ě ",
    "YÖ",
    "CT",
    "át",
    "ră",
    "YS",
    "çã",
    "A,",
    "RÁ",
    "RG",
    "fi",
    "LÁ",
    "ët",
    "'a",
    "SV",
    "Y.",
    "TJ",
    "t,",
    "SĂ",
    "L’",
    "áv",
    "DĀ",
    "JĄ",
    "OZ",
    "KÝ",
    "ŞT",
    "ÄV",
    "VY",
    "V.",
    "ÅT",
    " Å",
    "ey",
    "RV",
    "S.",
    "A'",
    "TÓ",
    "'d",
    " Ä",
    "DŽ",
    "GT",
    "võ",
    "kä",
    "V,",
    "dj",
    "ct",
    "oz",
    "LS",
    "'s",
    "Te",
    "PÁ",
    "To",
    "TÖ",
    "ký",
    "AŤ",
    "GÁ",
    "VÅ",
    " (",
    "AČ",
    "Ė ",
    "ė ",
    "TĄ",
    "cj",
    "s.",
    "JÄ",
    "vé",
    "CC",
    "RĂ",
    "sv",
    "Ya",
    "P ",
    "YÁ",
    "rå",
    "ĀV",
    "We",
    "TÂ",
    "Ť ",
    "ró",
    "ÂT",
    "yo",
    "Va",
    "'e",
    "KY",
    "CY",
    "TÆ",
    "JÁ",
    "şt",
    "LĀ",
    "EY",
    "VÝ",
    " Č",
    "TÅ",
    "OY",
    "sj",
    "FÄ",
    "Vo",
    "W.",
    "YJ",
    "ét",
    "ÁC",
    "ys",
    "Yo",
    "t.",
    "LÓ",
    "LÝ",
    "ŤA",
    "cc",
    "KÄ",
    "W,",
    "\",",
    "TÃ",
    "vā",
    "VÂ",
    "VĂ",
    "rä",
    "ky",
    "fa",
    "L”",
    "y,",
    "ÖZ",
    "Ye",
    "ŠT",
    "yö",
    "P.",
    "PJ",
    "VJ",
    "’A",
    "O.",
    " Ç",
    "A’",
    "v.",
    "U,",
    "fø",
    "Tc",
    "WS",
    "YÄ",
    "‘A",
    "FÆ",
    "RÓ",
    "\".",
    "”.",
    "FÅ",
    "PÂ",
    "če",
    "CJ",
    "F.",
    "āj",
    "ĄT",
    "”,",
    "“A",
    "\"A",
    "AĞ",
    "A”",
    "āt",
    "F,",
    "v,",
    "P,",
    " Į",
    "D,",
    "FÁ",
    "ía",
    "Wa",
    "tó",
    "YT",
    " \"",
    "Tu",
    "y.",
    "QY",
    "FĂ",
    "Tr",
    "L\"",
    "A\"",
    "že",
    "rc",
    "ÖT",
    "WÄ",
    "UX",
    "RÝ",
    "Tä",
    "ÅV",
    "ÂY",
    "KÕ",
    "YG",
    "öz",
    "'À",
    "cy",
    "Po",
    "Ó ",
    "ó ",
    "Të",
    "Yd",
    " į",
    ".\"",
    "ēt",
    "St",
    "ká",
    "D.",
    "“,",
    "Té",
    "KÓ",
    "Ts",
    "ĀC",
    "ÝM",
    "ÖV",
    "DV",
    "VÃ",
    "Tö",
    "SJ",
    "“.",
    "Tó",
    "Ý,",
    "U.",
    "Tõ",
    "'Â",
    "ŞA",
    "FØ",
    "-A",
    "\"Å",
    "Ko",
    ".”",
    "\"Ä",
    "ws",
    "'Á",
    "Tá",
    "LW",
    "YÂ",
    "PÆ",
    " ç",
    "Ä”",
    "RW",
    "YÅ",
    "L“",
    "Á”",
    "EČ",
    "VĄ",
    "ŁT",
    "væ",
    "Tø",
    "Ý.",
    "TV",
    "tö",
    "zé",
    "VS",
    "FÂ",
    "Tā",
    "Yö",
    ",”",
    "„V",
    ".“",
    "’.",
    ".’",
    "',",
    "’,",
    "T-",
    "Ă”",
    "rv",
    "Tâ",
    "p ",
    "Ť,",
    "ím",
    "Ty",
    "Ys",
    "WĄ",
    "\"Ā",
    "’À",
    "LÜ",
    "Tå",
    "w.",
    "ÅG",
    "ØY",
    "A“",
    ".T",
    "ŦA",
    "ex",
    "„Y",
    ",\"",
    ",“",
    "ČA",
    "„T",
    "Tü",
    "ť ",
    "Le",
    "”A",
    "'.",
    "év",
    "RÅ",
    ".'",
    "Á'",
    "Fa",
    "PÃ",
    "-T",
    "ĂV",
    "TZ",
    "št",
    "Vā",
    "”Á",
    "Tę",
    "Ł”",
    "Ä\"",
    "e.",
    "ft",
    "Á\"",
    "À\"",
    "Yu",
    ".V",
    "Tē",
    "Pa",
    "Ť.",
    "ĀY",
    "ät",
    "ÉC",
    "w,",
    "UJ",
    "ÄŤ",
    "FÃ",
    "EĆ",
    "ĀJ",
    "Vá",
    "Wo",
    "7.",
    "YĀ",
    "Tě",
    "tv",
    "ĄV",
    "Ą”",
    ".Y",
    "ræ",
    "'é",
    "KC",
    "Tw",
    "FT",
    "X ",
    "ŤÁ",
    "Au",
    "Á“",
    "Av",
    "o.",
    " č",
    "Ā\"",
    " Ž",
    "Vä",
    "a'",
    "Fo",
    "ĽT",
    "ča",
    "Ă\"",
    "Tą",
    "FJ",
    "ew",
    "gö",
    "„W",
    "Ťa",
    "Vd",
    "Vé",
    "SY",
    "BÁ",
    "Tă",
    "Võ",
    "Fe",
    "PĄ",
    "ëv",
    "Ą“",
    "RC",
    "ÄG",
    "kó",
    "Vâ",
    "ÁŤ",
    "Vê",
    "'o",
    "DÄ",
    "TÕ",
    "Vë",
    "Vå",
    "ÖY",
    ",T",
    "Tš",
    "RJ",
    "LÕ",
    "RÄ",
    "ČČ",
    "Vö",
    "oy",
    "T«",
    "Ų,",
    "öv",
    "AQ",
    "DW",
    "KÁ",
    "Vu",
    "Tz",
    "Tv",
    "»T",
    "my",
    "vs",
    "Y-",
    "uj",
    "FĀ",
    "’d",
    "Fr",
    "ĽV",
    "FĄ",
    "Yn",
    "OŽ",
    "Ő ",
    "kõ",
    "Væ",
    "ő ",
    "’e",
    "tě",
    "ÄS",
    "çe",
    "ŁU",
    "Vē",
    "ÕT",
    "Yr",
    "Tú",
    "rē",
    "ŦÁ",
    "Ay",
    "Yp",
    "Wc",
    "ŁW",
    " Ö",
    "Vs",
    "čč",
    "Da",
    "WC",
    "kc",
    "MY",
    "Ly",
    "‘J",
    "TW",
    "’o",
    "ĎA",
    "Re",
    "zd",
    "SŤ",
    " 2",
    "7,",
    "Vě",
    "ĄW",
    "Wä",
    "ZC",
    "rè",
    "n'",
    "Y«",
    "’a",
    "äy",
    "Lv",
    "Vă",
    "Tý",
    "LC",
    "ÁŦ",
    "-Y",
    "Vď",
    "//",
    "k,",
    "T»",
    "ZÖ",
    "AŦ",
    "Vč",
    "SÅ",
    "AĆ",
    "’é",
    "Yü",
    "TØ",
    "ož",
    "Ka",
    "x ",
    "Ī ",
    "Yv",
    "ī ",
    "“J",
    "«T",
    " ž",
    "Wó",
    "Äv",
    "ÄU",
    "yd",
    "tw",
    "tà",
    "kd",
    "Wô",
    "ľk",
    "ět",
    "ř.",
    "Áv",
    "Wö",
    "YW",
    "KÔ",
    "KØ",
    "äv",
    "yg",
    "ÝJ",
    "Fö",
    "B ",
    "’œ",
    ".W",
    "Tų",
    "’s",
    "b ",
    "TG",
    "f“",
    "ăt",
    "”J",
    "vå",
    "»V",
    "ÓT",
    "’ê",
    "TC",
    "RÜ",
    "DÅ",
    "LÖ",
    "„v",
    "rę",
    "XO",
    "f,",
    "Lý",
    "KÇ",
    "zc",
    "vë",
    "ÄC",
    "”d",
    "YĆ",
    "ĐA",
    "đa",
    "Ky",
    "Ku",
    "OX",
    "LØ",
    "”o",
    "DÝ",
    "ë,",
    "wc",
    "rö",
    "öt",
    "Tū",
    "Ų.",
    "ý,",
    "”e",
    "Pe",
    "SĀ",
    "VŠ",
    "WÓ",
    "f.",
    "Fä",
    "ÁŠ",
    "Kv",
    "Ke",
    "f\"",
    "YÓ",
    "f'",
    "Ž ",
    "ž ",
    "’-",
    "«Y",
    "Aw",
    "Vr",
    "PT",
    "\"J",
    "YQ",
    "Fá",
    "sy",
    "ÔV",
    "“c",
    "CÂ",
    "ÇA",
    "ÕJ",
    "SÃ",
    "VT",
    "EĞ",
    " ö",
    "Fæ",
    "YV",
    "Co",
    "ý.",
    "Ws",
    "pt",
    "ĂC",
    "Lw",
    "o\"",
    "“d",
    "Få",
    "ZÓ",
    "(j",
    "DĂ",
    "LĂ",
    "XC",
    "“o",
    "ÄČ",
    "rw",
    "'J",
    "Wę",
    "że",
    "uT",
    "Kw",
    "“e",
    "Fé",
    "rç",
    "ř,",
    "YČ",
    "-Ť",
    "-V",
    "»W",
    "Äy",
    "„w",
    "ÉV",
    "KG",
    "BĀ",
    "Vš",
    ".v",
    "tē",
    "Vn",
    "zö",
    "Tř",
    "e'",
    "BÝ",
    "ŠÍ",
    "ĽO",
    "Ja",
    "zw",
    "ÓV",
    "\" ",
    "”g",
    "*A",
    "VG",
    "ff",
    "V-",
    "rø",
    "La",
    "Y»",
    "ef",
    "Y/",
    "fd",
    "VC",
    "Fø",
    "øy",
    "ZG",
    "mj",
    "Kö",
    "KČ",
    "/A",
    "fä",
    "RÆ",
    "će",
    "YÇ",
    "ça",
    "KQ",
    "V«",
    "Vp",
    "”-",
    "n’",
    "\"c",
    "L-",
    "fé",
    "ĂU",
    "”č",
    "CÍ",
    "\"o",
    "\"d",
    "UÁ",
    "VÔ",
    "ÓX",
    "ĻV",
    "UĂ",
    "\"e",
    "VÖ",
    "ÔT",
    "ØT",
    "TÒ",
    "“g",
    "o'",
    "o”",
    "ØV",
    "‘a",
    "Vy",
    "’à",
    "Ký",
    "“č",
    "V_",
    "\"-",
    "T/",
    "”s",
    "K-",
    "ĻT",
    "Kë",
    "Vi",
    "n”",
    "o“",
    "o’",
    "ÓA",
    "«V",
    "'c",
    "a\"",
    "LQ",
    "”a",
    "Vz",
    "ÇO",
    "kç",
    "Yı",
    "Kõ",
    "TÇ",
    "ĒC",
    "Ro",
    "zą",
    "āv",
    "n“",
    "Wu",
    ") ",
    "XQ",
    "m’",
    "a”",
    "QA",
    "xe",
    "\"4",
    "V/",
    "Ā,",
    "f)",
    "'œ",
    "ox",
    "VÓ",
    "yá",
    "ØJ",
    "Pä",
    "rý",
    "ŁÓ",
    "”á",
    "KŠ",
    "'ê",
    "ÁU",
    "xo",
    "T:",
    "Fă",
    "-\"",
    "ÕV",
    "m”",
    "OÁ",
    "DX",
    "XÓ",
    "p”",
    "XÕ",
    "ÄO",
    "VÒ",
    "vă",
    "ÂC",
    "\"q",
    "“a",
    "Ā.",
    "Fu",
    "Ă,",
    "Pë",
    "a’",
    "X-",
    "\"ö",
    "{j",
    "Vü",
    "Xo",
    "Yt",
    "ŤO",
    "Fā",
    "ó”",
    "EO",
    "QV",
    "vâ",
    "RÖ",
    "\"ç",
    "Xe",
    "Në",
    "m'",
    "a“",
    "BT",
    "kj",
    "„C",
    "\"é",
    "lv",
    "UĀ",
    "kô",
    "ÖÄ",
    "gé",
    "ÇÕ",
    "ËV",
    "'è",
    "T’",
    "«W",
    ".w",
    "Ee",
    "P/",
    "s'",
    "DÆ",
    "Fs",
    "EÇ",
    "b\"",
    "RŮ",
    "câ",
    "OÃ",
    "YŌ",
    "n\"",
    "Y:",
    "sť",
    "l’",
    "b'",
    "ĆA",
    "zv",
    "râ",
    "VČ",
    "Ä.",
    "p\"",
    "e”",
    "A-",
    "ÖA",
    "WJ",
    "?.",
    "” ",
    "få",
    "?,",
    "„1",
    "zó",
    "rq",
    "LÇ",
    "KJ",
    "ŽO",
    "/,",
    "Fē",
    "Wy",
    "wó",
    "zę",
    "YŠ",
    "p'",
    "fă",
    "nv",
    "F/",
    "ĻU",
    "TÔ",
    "ÐV",
    "ÝČ",
    "T”",
    "ço",
    "/.",
    "RØ",
    "Ké",
    "Kó",
    "\\T",
    "”š",
    "« ",
    "vt",
    "Kd",
    "Ó,",
    " »",
    "DÃ",
    "Wr",
    " „",
    "Kø",
    "vš",
    "0.",
    "A\\",
    "QT",
    "ÓÁ",
    "AÕ",
    "T_",
    "ŠV",
    "DÂ",
    "Ze",
    "tõ",
    "PY",
    "\\V",
    "„O",
    "m\"",
    "fá",
    "\"a",
    "ë.",
    "kø",
    "m“",
    "xc",
    "eV",
    "Wn",
    "r-",
    "rê",
    "/c",
    "/a",
    "På",
    "LÔ",
    "\\\\",
    "Vý",
    "ÜA",
    "KŌ",
    "nV",
    "ÂU",
    "„G",
    "7/",
    "VØ",
    "LÒ",
    "No",
    "OÄ",
    "-W",
    "s\"",
    "/d",
    "n‘",
    "DĄ",
    "W-",
    "/o",
    "/e",
    "\"č",
    "TŐ",
    "ĄG",
    "tő",
    "Ac",
    "KÜ",
    "õ'",
    "ÚA",
    "TQ",
    "DÀ",
    "ÐA",
    "vc",
    "ÁQ",
    "fg",
    "OÅ",
    "AÓ",
    "e’",
    ".y",
    "'č",
    "e\"",
    "ń”",
    "ČO",
    "ÄÖ",
    "ČÁ",
    "-X",
    "fæ",
    "kč",
    " ë",
    "ĂS",
    "ZS",
    "LŲ",
    "Tı",
    "Põ",
    "çõ",
    "„Ö",
    "/g",
    "py",
    "ÁČ",
    "KĆ",
    "Y;",
    "AÖ",
    "ø\"",
    "ă”",
    "ľa",
    "ÄQ",
    "åt",
    "AÚ",
    "UÂ",
    "á“",
    ",\\",
    "'à",
    "Vů",
    "bý",
    "ža",
    "T;",
    "wä",
    "At",
    "[1",
    "\"g",
    "Ů.",
    "UÃ",
    "ća",
    "Fü",
    "ØA",
    "LÚ",
    "ôv",
    "Pē",
    "s“",
    "'«",
    "UÅ",
    "ä”",
    "ĘC",
    "Pá",
    "ÝS",
    " «",
    "rò",
    "Ů,",
    ".\\",
    "á”",
    "'g",
    "öy",
    "“s",
    "yé",
    "Wz",
    "ą“",
    "kš",
    "„U",
    "fë",
    "LŪ",
    "čj",
    "rą",
    "BV",
    "ÂG",
    "ÚJ",
    "Wü",
    "pv",
    "Wś",
    "e“",
    "Wp",
    "čo",
    "AÜ",
    "Wi",
    "„Č",
    "vg",
    "rf",
    "Ó.",
    "W/",
    "ĄĆ",
    "kq",
    "á'",
    "\"s",
    "ŁC",
    "&\\",
    "ať",
    "V»",
    "UÆ",
    "RÇ",
    "ä\"",
    "SÆ",
    "9.",
    "Kü",
    "Na",
    "„t",
    "tę",
    "»,",
    "OŦ",
    "á\"",
    "74",
    "ză",
    "à\"",
    "ÖW",
    "GÅ",
    "LŐ",
    "TČ",
    "ĽA",
    "/J",
    "Ce",
    "xq",
    "R-",
    "tą",
    "'â",
    "óx",
    "kę",
    "xd",
    "ÓJ",
    "K«",
    "ĀO",
    "YY",
    "xa",
    "ÖJ",
    "/s",
    "Az",
    "ŠY",
    "zs",
    "řa",
    "wą",
    "Pâ",
    "ā\"",
    "WÖ",
    "óv",
    "ë”",
    "bv",
    "tø",
    "Zu",
    "J.",
    "vč",
    "În",
    "Ò,",
    "Ö,",
    "/4",
    "'á",
    "xé",
    "ĀČ",
    "Pr",
    "OŤ",
    "Lo",
    "fc",
    "».",
    "OĀ",
    "ă\"",
    "Ca",
    "ą”",
    "žo",
    "čá",
    "LČ",
    "Pé",
    "s’",
    "Fy",
    "yä",
    "ĽU",
    "Ö.",
    "ęt",
    "øv",
    "vã",
    "RŲ",
    "áj",
    "ĀU",
    "zg",
    "Kč",
    "LŌ",
    "rô",
    "ĎÁ",
    "J,",
    "“š",
    "ŌT",
    "Pó",
    "u’",
    "4'",
    "k-",
    "ľb",
    "Ò.",
    "ŠĀ",
    "fq",
    "é“",
    "õt",
    " “",
    "Ð,",
    "EQ",
    "“V",
    "ë“",
    "ĀG",
    "ką",
    "Zw",
    "7-",
    " ”",
    "Õ,",
    "fâ",
    "TŌ",
    "vè",
    "D’",
    "L«",
    "Fú",
    "Ev",
    "“-",
    "ë\"",
    "\"ā",
    "vê",
    "Lt",
    "ÝŠ",
    "ŁG",
    ".O",
    "vô",
    "gd",
    "ÆG",
    "Ü.",
    "xë",
    "ę”",
    "Pô",
    "ež",
    ".1",
    "ĂG",
    "WÔ",
    " '",
    "LŮ",
    "Ą,",
    "Kę",
    "Es",
    "vz",
    "WG",
    "Kē",
    "KV",
    "YŚ",
    "Pö",
    "Pè",
    "vą",
    "x-",
    "RŤ",
    "xó",
    "*J",
    "Q.",
    "BĂ",
    "s)",
    "rã",
    "ę“",
    "fç",
    "Sv",
    "KŲ",
    "xõ",
    "Ą.",
    "p.",
    "Tf",
    "Pā",
    "SĄ",
    "vö",
    "RŪ",
    "L?",
    "ě“",
    "Fw",
    "é'",
    "rõ",
    "Ď,",
    "wd",
    "fó",
    "V:",
    ",1",
    "vę",
    "t-",
    "r’",
    "-S",
    "yć",
    ".C",
    "k«",
    "rč",
    "\"š",
    "-7",
    "rė",
    "(«",
    "s”",
    "Pă",
    "KW",
    "õv",
    "šv",
    "fè",
    "\"ş",
    "kć",
    "Zv",
    "'š",
    "Ne",
    "Ru",
    "“Y",
    "Me",
    "Ø.",
    "Ď.",
    "fê",
    "rà",
    "vó",
    "rX",
    "JJ",
    "-1",
    "ŔT",
    "FS",
    "ŘT",
    "æv",
    "Za",
    "ŚW",
    "vò",
    "Xu",
    "»Z",
    "Zo",
    "FG",
    " Ż",
    "0,",
    "Ō,",
    "Ü,",
    "4\"",
    "Ť:",
    "Ao",
    "Ä,",
    "T“",
    "nw",
    "Ø,",
    "r/",
    "„A",
    "’n",
    "zë",
    "fô",
    "”V",
    "ē\"",
    "Åt",
    "åv",
    "ÞA",
    "Át",
    "Ú,",
    "Vj",
    "Ät",
    "Xa",
    "’Y",
    "V”",
    "ò ",
    "Ò ",
    "ÂĞ",
    "kg",
    "VZ",
    ".G",
    "zē",
    "kē",
    "r”",
    "Lu",
    "Z-",
    "vď",
    "řá",
    "Ă.",
    "a\\",
    "ÈC",
    "ÓZ",
    "TÝ",
    "r«",
    "řo",
    "”Y",
    "BW",
    "fã",
    "BX",
    "R”",
    "R’",
    "V;",
    "TŎ",
    "Ú.",
    "Ká",
    "wę",
    "’T",
    "Q,",
    "kâ",
    "tâ",
    "èv",
    "Vt",
    "tg",
    "RQ",
    "Gj",
    "cé",
    "Ad",
    "tý",
    "’O",
    "Je",
    "CÓ",
    "”T",
    "p,",
    "Sz",
    "SW",
    "Zy",
    ".Q",
    "’m",
    "fs",
    "E-",
    "Y”",
    "kü",
    "ťa",
    "kō",
    "BÅ",
    "„c",
    "' ",
    "fī",
    "»J",
    "Jo",
    "tc",
    "”W",
    "TŠ",
    "„u",
    "cē",
    "_1",
    "Ù,",
    ".Ö",
    "MT",
    "JÆ",
    "Ù.",
    "4’",
    "yč",
    "nf",
    "ēv",
    "ĻO",
    "LÆ",
    ".«",
    "W’",
    "bw",
    "/-",
    "ât",
    "RÒ",
    "fē",
    "fč",
    "Ra",
    "cë",
    "RÚ",
    "/n",
    "L1",
    "yq",
    "W”",
    "È ",
    ":T",
    "KÚ",
    "Pě",
    "/m",
    "“T",
    "GV",
    "êt",
    "„o",
    "/r",
    "KŮ",
    "ş’",
    " ż",
    "vø",
    "A?",
    "fî",
    "qj",
    "’ ",
    " İ",
    ".Ç",
    "kv",
    "Yi",
    "b.",
    "t«",
    "Y’",
    "gë",
    "ót",
    "BÄ",
    "sw",
    "ÅS",
    "Kä",
    "ó,",
    "ÔZ",
    "Kū",
    "Fi",
    "kų",
    "Ť“",
    "św",
    "Yj",
    "rć",
    "-Á",
    "yó",
    "-J",
    "Ti",
    "/p",
    "ÔJ",
    "yâ",
    ",«",
    "+\\",
    "R«",
    "Eg",
    "kæ",
    "yå",
    "fę",
    "Zd",
    "êv",
    "SÝ",
    "tå",
    "Et",
    "7A",
    "šj",
    "v/",
    "Ry",
    "Kr",
    "Šv",
    "rş",
    "PZ",
    ": ",
    "Ey",
    "š”",
    "ļa",
    "/u",
    ".U",
    "V“",
    "ŲJ",
    "C’",
    "ěv",
    "ÔŽ",
    "ZQ",
    "fą",
    "- ",
    "ZÒ",
    "Tj",
    "JÀ",
    "„č",
    ".t",
    "Y“",
    "b,",
    "Ae",
    "ĽÚ",
    "ÉQ",
    "wö",
    "C'",
    "è ",
    "A«",
    "PÝ",
    "PV",
    ".Č",
    "Če",
    ",t",
    "r“",
    "Ū.",
    "tæ",
    "éx",
    "fā",
    "řč",
    "Že",
    "Ró",
    "y”",
    "”O",
    "Aç",
    "Ū,",
    "Kâ",
    "Wt",
    "Aq",
    "Vf",
    "C«",
    "nī",
    "„d",
    "»A",
    "kå",
    "„e",
    "Kā",
    "”G",
    "t’",
    "wg",
    "W:",
    "Kå",
    "Žv",
    "E«",
    "rō",
    "’Œ",
    "»v",
    "Af",
    "ÉO",
    "ZÕ",
    "ZÔ",
    "XA",
    "C-",
    "tò",
    "öw",
    "Aa",
    "Aé",
    "Un",
    "RÔ",
    "”C",
    "yç",
    "ďa",
    "Áu",
    "yš",
    " ‘",
    "9,",
    "t”",
    "YŞ",
    "Ä-",
    "F-",
    "Äu",
    "Ád",
    ".?",
    "Rö",
    "c«",
    "Ew",
    "B'",
    "JÂ",
    "Žy",
    "Ý“",
    "ÓŹ",
    "-Z",
    "pw",
    "Sy",
    "P-",
    "šy",
    "pf",
    "ŌJ",
    "Ç’",
    "Ré",
    " ’",
    "có",
    "yā",
    "rš",
    "bt",
    "JÅ",
    "Fj",
    "yè",
    "y’",
    "_O",
    "„é",
    "-t",
    "B\"",
    " è",
    "C”",
    "LÅ",
    "JÃ",
    "Fı",
    "äj",
    "l”",
    "mt",
    "kw",
    "„f",
    "mv",
    "ĄS",
    "(e",
    "Ă?",
    "-\\",
    "(a",
    "Rø",
    "Ed",
    "ťo",
    "Rd",
    "CĪ",
    "í)",
    "óz",
    "ĀŠ",
    "ÁJ",
    "(d",
    "Ą?",
    "ľo",
    ".Ü",
    "v«",
    ".0",
    "Év",
    "o)",
    "BJ",
    "Rõ",
    "Ec",
    "tã",
    "+7",
    "AŚ",
    "Zé",
    "Á-",
    "FÓ",
    "w’",
    "ŞY",
    "f-",
    "6'",
    "Ă-",
    "FC",
    "ăv",
    "“ ",
    "Zë",
    "y/",
    "QJ",
    "ÕZ",
    "y«",
    "„g",
    "-Å",
    "ĶO",
    "ây",
    "c'",
    ".)",
    "Zg",
    "Eu",
    "DŹ",
    "»z",
    "CQ",
    "Ps",
    "41",
    "FQ",
    "c\\",
    "“G",
    "ş'",
    "êx",
    "lý",
    "øt",
    "\\v",
    "(G",
    "RÕ",
    "ÀS",
    "CÔ",
    "zā",
    "kú",
    "Mo",
    "kW",
    "ó.",
    "ëx",
    "[4",
    "Ač",
    "Ft",
    "žd",
    "-v",
    "Cy",
    "VŞ",
    "ků",
    "ŽG",
    "ýd",
    "RČ",
    "JĂ",
    "Ć”",
    "Rë",
    "KŪ",
    "D)",
    "w”",
    "Ea",
    "Rw",
    "pý",
    "Žo",
    "Rê",
    "À-",
    "e)",
    "/x",
    "FÔ",
    "ÍS",
    "Dá",
    "Č’",
    "BĄ",
    "ís",
    "“Q",
    "Ho",
    "éy",
    "CÒ",
    "EÓ",
    "td",
    "O’",
    "U/",
    "O)",
    "?/",
    "Cv",
    "Mu",
    "ŽC",
    "tė",
    "O”",
    "BÂ",
    "ŽÕ",
    "T&",
    "D”",
    "jj",
    "(o",
    "RÂ",
    " Ā",
    "Ē ",
    "ş\"",
    "cī",
    "ē ",
    "ŞV",
    "CÇ",
    "rð",
    ",0",
    "W;",
    "ôž",
    "Ād",
    "“O",
    "&W",
    "-À",
    "(c",
    "6’",
    "[«",
    "ßv",
    "tç",
    "*d",
    "Éc",
    "ĚC",
    "ôz",
    "ąt",
    "ąv",
    "bz",
    "ť“",
    "47",
    "B’",
    "Ã-",
    "ö,",
    "ò,",
    "V&",
    "PŽ",
    "Sw",
    "LŠ",
    "o?",
    ",7",
    "ŠŤ",
    "ĘG",
    "tè",
    "pz",
    "Ét",
    "*o",
    "ŘO",
    "FÇ",
    "kė",
    "ýs",
    "(O",
    ".-",
    "BÆ",
    "SÂ",
    "/O",
    "/C",
    "óź",
    "ÈG",
    "Ox",
    "ÃS",
    "-Ä",
    " Æ",
    "/G",
    "tô",
    "-Ž",
    "y)",
    "Ó”",
    "„a",
    "Ż ",
    "ż ",
    "D/",
    "KĄ",
    "eX",
    "*e",
    "Ju",
    "-2",
    "ÇÖ",
    "y-",
    "v“",
    "ČJ",
    "Lõ",
    "k’",
    "ôt",
    "CĄ",
    "cè",
    "wz",
    "ø,",
    "-y",
    "tê",
    "Ef",
    "YZ",
    "Ag",
    "WZ",
    "-3",
    "4T",
    "F4",
    "Eq",
    "ĎŽ",
    "ýč",
    "e?",
    "Ç'",
    "ZČ",
    "Rý",
    "B”",
    "(v",
    "ëz",
    "ö.",
    "yō",
    ":V",
    "xã",
    "ø.",
    "GW",
    "Ķe",
    "Ře",
    "Dx",
    "0)",
    "ŌZ",
    "Zü",
    "Q_",
    "Rē",
    "c\"",
    "mw",
    "ÂS",
    "gó",
    "õ,",
    "xá",
    "c’",
    "B.",
    "ç'",
    "ČT",
    "/w",
    "Kf",
    "Ço",
    "Eé",
    "ķe",
    "(C",
    "ò.",
    "ŠÁ",
    "/y",
    "ËG",
    "FČ",
    ".o",
    "cq",
    ".7",
    "zq",
    "ŮJ",
    "7:",
    "eż",
    "» ",
    "RĄ",
    "v-",
    "ŹC",
    "Cu",
    "-Ą",
    "æt",
    "Çe",
    "z-",
    "Ví",
    "Lü",
    "Č-",
    "CG",
    "ŹĆ",
    "+2",
    " ł",
    "OŹ",
    "«e",
    "«d",
    "(w",
    "mý",
    "t“",
    "“?",
    "WŚ",
    "Eö",
    "Éd",
    "Ą-",
    "Ć-",
    "Ā-",
    "*a",
    "k”",
    "ÙJ",
    "RÛ",
    "Lé",
    "O/",
    "(A",
    "Có",
    "ÇT",
    "CĀ",
    "*-",
    "ć'",
    "Pu",
    "CÁ",
    "ßw",
    "«c",
    "EÕ",
    "ō,",
    "-Ā",
    ",4",
    "Lë",
    "xă",
    "G’",
    "EÖ",
    "p)",
    "ŠĄ",
    "Zá",
    "b)",
    "tq",
    "Lä",
    "4]",
    "n?",
    "Tí",
    "EÒ",
    "\\O",
    "ć\"",
    "m?",
    "B,",
    "ČC",
    "Cé",
    "Lö",
    "r)",
    "zò",
    "č'",
    "+1",
    ".c",
    "ĄJ",
    "3.",
    "4\\",
    "ÂŠ",
    "(q",
    "SÀ",
    "0T",
    "Cô",
    "Šy",
    "My",
    "ĻĢ",
    "Lú",
    "6.",
    "w)",
    "ÇG",
    "CŒ",
    "\\C",
    "/3",
    "Pj",
    "yś",
    "ŠÄ",
    "97",
    "ÊC",
    "Më",
    "e»",
    "v)",
    "24",
    "9)",
    "ŪJ",
    "RŌ",
    "ó)",
    "Św",
    "cô",
    ".f",
    "RĆ",
    "ŘŮ",
    "S)",
    "VĢ",
    "Ég",
    "c”",
    "[o",
    "-z",
    "a)",
    "cò",
    "c“",
    "7e",
    "-,",
    "~7",
    "ßt",
    "EØ",
    "}}",
    "Çd",
    "ĒG",
    "ŘA",
    "76",
    "ËQ",
    "(é",
    "çd",
    "éz",
    "ö)",
    "«a",
    "Âg",
    "õ)",
    ".e",
    "ĻG",
    "/v",
    ".4",
    "ĻŪ",
    "(ö",
    "KŚ",
    "Ág",
    "(Q",
    "Ló",
    "ÈQ",
    "ąw",
    "Ud",
    "ző",
    "ZŐ",
    "5.",
    "zõ",
    "KŞ",
    "zô",
    "Áf",
    "õz",
    "öf",
    ".A",
    "Žu",
    "9/",
    "Io",
    "ļu",
    "_o",
    "OŻ",
    "ŘU",
    "oŧ",
    "(ç",
    "kū",
    "7c",
    "C\"",
    "c-",
    "«å",
    "’t",
    "cç",
    "»t",
    "oż",
    "[c",
    "/6",
    "(r",
    "Nj",
    "ÊQ",
    "/t",
    "\\Q",
    "çë",
    "Äg",
    "Gy",
    "źd",
    "GÄ",
    "Ło",
    "XT",
    "ë)",
    "\\G",
    "By",
    "o»",
    "(õ",
    "(4",
    "çö",
    "ÆC",
    "ÆV",
    ".u",
    "o]",
    "Sý",
    "*g",
    "ÆO",
    "ĘĆ",
    "kł",
    "Çë",
    "Rá",
    "Çö",
    "Čo",
    "ø)",
    "žc",
    "ŘČ",
    "Ľ ",
    "ĆO",
    "zê",
    "Nd",
    "ěz",
    "Ua",
    "zè",
    ".d",
    "ÉÇ",
    "[d",
    "n)",
    "C“",
    "SX",
    "āy",
    "4.",
    "-.",
    "KÆ",
    "[e",
    "şv",
    "(t",
    "«o",
    "ýš",
    "ír",
    "ē,",
    "(1",
    "cê",
    "7a",
    "Łu",
    "r]",
    "Ľu",
    "ÇY",
    "C=",
    "J/",
    "2]",
    "ėt",
    "ýð",
    "Lū",
    "Né",
    "é,",
    "(Ç",
    "ÉČ",
    "Vī",
    "Lø",
    "(u",
    "ķē",
    "Rü",
    "%1",
    "(Ö",
    "gø",
    "Ó)",
    "Y)",
    "Ë-",
    "cą",
    "cd",
    "\\t",
    "8.",
    "F:",
    "(s",
    "Tī",
    "ě.",
    "Æt",
    "zč",
    "Um",
    "ŁĄ",
    "Čc",
    "a?",
    "Āf",
    "řs",
    "ē.",
    "Ră",
    "fy",
    "Nõ",
    "žõ",
    "(Õ",
    "Cē",
    "Åa",
    "-w",
    "Õ)",
    "+3",
    "t\\",
    "K+",
    "Ks",
    "ĚČ",
    "P4",
    "ŞÂ",
    "Jó",
    "XS",
    "Æg",
    "/1",
    "Ö)",
    "Us",
    "Câ",
    "p»",
    "èt",
    "zď",
    "Ťi",
    "ķo",
    "T?",
    "CÃ",
    "Ža",
    "iT",
    "žā",
    "Ça",
    "-ž",
    "ČY",
    "Rä",
    ",d",
    "ć”",
    "új",
    "Zä",
    "/9",
    "/2",
    "tō",
    "aļ",
    "lw",
    "Eğ",
    "(J",
    "ćo",
    "/0",
    "Jä",
    "(n",
    "ě,",
    "(0",
    "FY",
    "Št",
    "8)",
    "Rå",
    "É-",
    "6]",
    "Ağ",
    "[w",
    "Uc",
    "D]",
    "ōz",
    "óf",
    "Üç",
    "Ã ",
    "Ê-",
    "Râ",
    "p}",
    "MÝ",
    "Cá",
    "Já",
    "3)",
    "oź",
    "4)",
    "Úd",
    "Cs",
    "KÂ",
    "pž",
    ".ē",
    "Új",
    "e]",
    "ę,",
    "2-",
    "Á,",
    "~1",
    "Č'",
    "Uz",
    "Ie",
    "Rú",
    "Ć'",
    "čc",
    "07",
    "(č",
    "78",
    "źc",
    "ÆČ",
    "70",
    "cę",
    "AX",
    "ťd",
    "tč",
    "F;",
    "źć",
    "žé",
    "A1",
    "ă?",
    "Jø",
    "Uj",
    "{o",
    "S_",
    ".g",
    "ěž",
    "Ää",
    "Łó",
    " Ø",
    "Sx",
    "{e",
    "Jc",
    "CÄ",
    "Jd",
    "é)",
    "GÂ",
    "ăj",
    "B)",
    "ō)",
    "Zā",
    "O]",
    "w-",
    "cā",
    "Jé",
    "{d",
    "Uo",
    "tď",
    "D}",
    "žy",
    "Ug",
    "Jæ",
    "vş",
    "žá",
    "wś",
    "ą?",
    "şy",
    "/f",
    "s?",
    "xs",
    "9T",
    "Ş,",
    "{q",
    " Â",
    "bž",
    "Jõ",
    "žē",
    "sý",
    "Â ",
    "žď",
    "Ng",
    "ť,",
    "*T",
    "A)",
    "51",
    "KÛ",
    "Ue",
    "cœ",
    "éf",
    "(à",
    "AĢ",
    " Ť",
    "Jö",
    "Zs",
    "ć-",
    "ť.",
    "[C",
    "[2",
    "Š,",
    "?-",
    "61",
    "V)",
    "Žá",
    "(á",
    "sf",
    "'?",
    "(Ø",
    "Nó",
    "(ú",
    "žę",
    "ŘÁ",
    "Ć\"",
    "Rt",
    "Gv",
    "ÄJ",
    "CV",
    ",9",
    "Ræ",
    "(6",
    "Mc",
    "(Č",
    "*V",
    "fz",
    "CÆ",
    "„S",
    "Ex",
    "ÄX",
    "Kn",
    "_{",
    "/S",
    "Ús",
    "(-",
    "/8",
    "[z",
    "kļ",
    "4%",
    " :",
    "m)",
    "LĄ",
    "-)",
    "~2",
    "6T",
    "zä",
    "Id",
    "ř ",
    "é.",
    "Nø",
    "C»",
    "ĶS",
    "zâ",
    "Că",
    "3T",
    "6)",
    "*v",
    "Řa",
    "Ø)",
    "tš",
    "Mõ",
    "Mv",
    "Nö",
    "ÝV",
    "~3",
    "Lá",
    "0/",
    "(z",
    "Oa",
    "cá",
    "Cz",
    "PW",
    "+.",
    "RÃ",
    "Rā",
    ".9",
    "tŏ",
    "67",
    "čd",
    "Rū",
    "WT",
    "2)",
    "ĪS",
    "Ča",
    "vė",
    "s»",
    "Sf",
    "ĽS",
    "[G",
    "Js",
    "Á.",
    "ę.",
    "Řá",
    "{J",
    "īn",
    "7;",
    "Km",
    "*W",
    "ćd",
    "bf",
    "Üs",
    " Ą",
    "Úg",
    "Ě-",
    "Š.",
    "Uu",
    "{O",
    "Sj",
    "īs",
    "Ic",
    "u)",
    "Mj",
    "))",
    "r}",
    "ČĀ",
    "š?",
    " Ă",
    "cv",
    "-f",
    "}_",
    "(m",
    "P)",
    "žg",
    "øf",
    "Úz",
    "MV",
    "ČÂ",
    "ŗa",
    "yş",
    "İs",
    "Fí",
    "Jå",
    "\\0",
    "ð,",
    "GÃ",
    "0}",
    "[O",
    "Üz",
    "kş",
    "\\&",
    "Ij",
    "C4",
    "PŤ",
    "O}",
    "ľt",
    "[č",
    "Čá",
    "Mé",
    "Dä",
    "Rů",
    "ÝT",
    "łą",
    "rģ",
    "rő",
    "ęz",
    "C,",
    "ÁX",
    "ČÆ",
    "{a",
    "KÅ",
    "Ig",
    "Cæ",
    "RÀ",
    "Gw",
    "Ďa",
    "u?",
    "[t",
    "Ļ ",
    "mf",
    "kś",
    "gê",
    "Mö",
    "„Š",
    "GÀ",
    "~X",
    "zã",
    "oť",
    "V(",
    "4,",
    "ťá",
    "-}",
    "; ",
    "Ĕ-",
    "XU",
    "As",
    "{4",
    "Čt",
    "Çu",
    "Lå",
    "ě)",
    "«s",
    "ŽS",
    "(S",
    "ðv",
    "Çü",
    "čt",
    "c)",
    "Pü",
    "s}",
    "8/",
    "e7",
    "8\\",
    "ín",
    "{s",
    "ōt",
    ",6",
    "(g",
    "{Q",
    "À,",
    "Då",
    "CŤ",
    "Bý",
    "Dz",
    "2T",
    "C\\",
    "Ō)",
    "XÃ",
    "íř",
    "„Ś",
    "Là",
    "ē)",
    "Ču",
    "çt",
    "tĕ",
    "GX",
    ",A",
    ".a",
    "XJ",
    "gè",
    ".6",
    "Hj",
    "87",
    "fj",
    "ČV",
    " ø",
    "3,",
    "*s",
    "Mê",
    "XÁ",
    "cã",
    "gõ",
    "cg",
    "BZ",
    "ľ ",
    "[Č",
    "Mó",
    "JĮ",
    "-Š",
    " X",
    "CW",
    "c]",
    "RX",
    "XĂ",
    "ŠJ",
    "v&",
    "c»",
    "lį",
    "ç)",
    "xy",
    "Pú",
    "49",
    "çg",
    "VM",
    "ŁS",
    "čv",
    "Mô",
    "ę)",
    "*w",
    "K_",
    "[9",
    "f3",
    "rś",
    "cä",
    "Ła",
    "-/",
    "Pv",
    "\\S",
    "Lā",
    "ľv",
    "4}",
    "5,",
    "Ľa",
    "Å,",
    "Ax",
    "XV",
    "Lă",
    "ş)",
    "Dâ",
    "xu",
    "(8",
    "ßf",
    "c,",
    "À.",
    "ļā",
    "ZŠ",
    ")T",
    "gò",
    "gc",
    "Py",
    "B}",
    "„s",
    "/V",
    "äť",
    "-ť",
    "Dā",
    "69",
    "ŕš",
    "LÂ",
    "ŤT",
    "=3",
    "{6",
    "ŧe",
    "9}",
    "ş,",
    "s_",
    "gô",
    "Læ",
    "B/",
    "\\c",
    "z)",
    "kû",
    "C.",
    "3/",
    "zæ",
    "XY",
    "(ś",
    "YX",
    "Uš",
    ".}",
    "rť",
    " Õ",
    "Fī",
    "Ś,",
    "/Y",
    "8}",
    "{-",
    "FX",
    "ËJ",
    "({",
    "{0",
    "čâ",
    "čā",
    "Łą",
    "YŤ",
    "T(",
    "\\d",
    " Í",
    "„š",
    "đu",
    "Å.",
    "})",
    "\\o",
    "fv",
    "ŕt",
    "ÈV",
    "Ś.",
    "5/",
    "žą",
    "LÀ",
    "(ž",
    "řt",
    "{C",
    "6\\",
    "{n",
    "š.",
    "ÉY",
    "Ş.",
    "š,",
    "És",
    "ŽŠ",
    "cæ",
    "Ļo",
    "Qa",
    "ų?",
    "SÍ",
    "{A",
    "è,",
    "İn",
    "(ş",
    "37",
    "Dą",
    "á)",
    "Ës",
    "c.",
    "ēz",
    "ČÍ",
    "p/",
    "ê,",
    "n}",
    "š»",
    "à)",
    "Zp",
    "kz",
    "\\f",
    "eť",
    "ê.",
    "(.",
    "ĆW",
    "[A",
    "â)",
    "LÃ",
    "éž",
    "ćw",
    "Q)",
    "Ã.",
    "9A",
    "b/",
    "\\e",
    "{1",
    "6,",
    "G)",
    "Ã,",
    "ĽŠ",
    "Tb",
    "Tl",
    "{{",
    "{r",
    "(9",
    "u}",
    "fw",
    "Â,",
    "{m",
    "Ls",
    "(Ģ",
    "žs",
    "æ,",
    "zý",
    " õ",
    "(x",
    "k_",
    ".ä",
    "SĪ",
    "m}",
    "Eš",
    "o/",
    "Yb",
    "ć)",
    "æ.",
    "B1",
    "eA",
    "2}",
    ")}",
    "27",
    "X,",
    "[5",
    "Yk",
    "Yl",
    "ťt",
    "\\q",
    "ů)",
    ":3",
    "īm",
    "{(",
    "8T",
    "sī",
    "{9",
    "pť",
    "ň)",
    "E4",
    "-9",
    "ņv",
    "zš",
    "5 ",
    "3}",
    "ŽĢ",
    "ß ",
    "rx",
    "*t",
    "»)",
    "čæ",
    "k)",
    "ž)",
    "eź",
    "ÉJ",
    "43",
    "r?",
    "šť",
    "7C",
    "(À",
    "(Ä",
    "(Á",
    "S/",
    "A]",
    "č)",
    "ĕ,",
    "Pt",
    "ŐT",
    "6}",
    "TX",
    "ÊV",
    "őt",
    "(Å",
    ":s",
    "2\\",
    "kį",
    "a}",
    "(Š",
    "ŻO",
    "59",
    "A_",
    "8,",
    "L=",
    "çy",
    "O?",
    "Eş",
    "95",
    "X_",
    "Oz",
    "[Á",
    "eæ",
    "45",
    "5%",
    "K?",
    "R&",
    "ęź",
    "R?",
    "(ř",
    "FV",
    "ė“",
    "żo",
    "R]",
    "ŠZ",
    "aŧ",
    "ć,",
    "«)",
    "žš",
    "áť",
    "x)",
    "áf",
    "ė'",
    " ť",
    "ēž",
    "P}",
    "Š)",
    "\\s",
    "ş.",
    "čy",
    "(»",
    "Q}",
    "\\}",
    " ‚",
    "ĕt",
    "6/",
    "2+",
    ":7",
    "æf",
    "Á]",
    "Ā)",
    "»]",
    "{8",
    "‘ ",
    "BŽ",
    "E+",
    "Kī",
    "R)",
    "ĻŠ",
    "-5",
    "Ă)",
    "»;",
    "‚ ",
    "ė”",
    "Bf",
    "2 ",
    "ďu",
    "äf",
    "ěť",
    "cA",
    "[~",
    "V=",
    "(Ś",
    "(Ā",
    "_l",
    "Š/",
    "ďá",
    "[g",
    "Ş)",
    "wt",
    "fő",
    "Īp",
    "Jį",
    "{S",
    "*f",
    "íp",
    "71",
    "kî",
    "ŠŽ",
    "Ć,",
    "x_",
    "ĻS",
    "ś,",
    "f4",
    "(Ş",
    "kī",
    "A}",
    "ć.",
    "(2",
    "áŧ",
    "Ä)",
    "Á)",
    "ëf",
    "42",
    "R_",
    "(f",
    "2e",
    ")V",
    "č.",
    "=1",
    "+9",
    "4 ",
    "\\a",
    ";7",
    "Ír",
    "nį",
    "NĮ",
    "73",
    "ża",
    "Ís",
    "*G",
    "t)",
    "6%",
    "O3",
    "À)",
    "X1",
    "Îm",
    "2d",
    "G}",
    "Ì ",
    "VX",
    "Ás",
    "Ín",
    "ďm",
    "6 ",
    " ď",
    "Â)",
    "g)",
    "o:",
    "85",
    "āf",
    "{x",
    "ĂJ",
    "*O",
    "Äs",
    "Ås",
    "23",
    "İm",
    "šf",
    "62",
    "R}",
    "t]",
    "63",
    "=2",
    "?)",
    "č,",
    "52",
    "şf",
    "cC",
    "ç.",
    "İS",
    "Cī",
    "7 ",
    "ľs",
    "Aš",
    "ç,",
    "e2",
    "79",
    " 4",
    "{2",
    "Tk",
    " -",
    "7%",
    "&f",
    "îm",
    "e/",
    "İr",
    " Ő",
    "F=",
    "b2",
    "* ",
    "*n",
    "ß.",
    "$7",
    "īr",
    "C2",
    "Īr",
    "ė,",
    " Ī",
    "c:",
    "wv",
    "*p",
    "*r",
    "*m",
    "cG",
    "L)",
    "Ć.",
    "ß,",
    ",3",
    " Ł",
    "ć:",
    "x}",
    "B2",
    ".3",
    "05",
    ",8",
    "g}",
    "Č,",
    "Īn",
    "Č.",
    "k}",
    "4/",
    ".S",
    "åf",
    "ďs",
    "5_",
    "Īs",
    " ő",
    "Aş",
    "ßz",
    "ŐZ",
    "őz",
    "Ç,",
    "6:",
    ".]",
    "53",
    "C)",
    "Čī",
    "4x",
    "mī",
    "t?",
    "t&",
    " {",
    "Ď ",
    "ď ",
    "ë/",
    "C&",
    "[f",
    "šz",
    " ;",
    "cł",
    "ŠĪ",
    " +",
    ".s",
    "ņt",
    "t}",
    " 5",
    "72",
    "7(",
    "Ç.",
    "6A",
    " ī",
    "ůj",
    "ÓŻ",
    "óż",
    "c=",
    "a_",
    "s/",
    " *",
    "c_",
    "t_",
    "ı)",
    "cť",
    "īp",
    "7t",
    "İş",
    "o;",
    ":e",
    ".8",
    "aî",
    "çf",
    "L}",
    "{3",
    "(3",
    "c;",
    "p:",
    "T1",
    "šž",
    "ùj",
    "?]",
    "žė",
    "4X",
    " Ć",
    "% ",
    "V3",
    "5t",
    "E?",
    "65",
    " ć",
    "35",
    "c/",
    ",S",
    " 9",
    " %",
    "î ",
    "Î ",
    "Ř ",
    ",s",
    "ļi",
    "dį",
    "jį",
    "ūj",
    "3A",
    ":o",
    "Šį",
    "*S",
    "š/",
    "+5",
    "b:",
    "E&",
    "C_",
    " Ó",
    "V1",
    "ïa",
    "F3",
    "ÍŠ",
    "Šī",
    "B3",
    "C/",
    "s:",
    "ćf",
    "ĪŠ",
    "cf",
    "=9",
    "Ć)",
    "Ç)",
    "ęż",
    "Č)",
    " ó",
    " 7",
    "ŐV",
    "őv",
    ".Š",
    " Ģ",
    "ó:",
    "Ö ",
    "ö ",
    ".Ş",
    "ŐJ",
    "p;",
    "S}",
    " ļ",
    "VŐ",
    "vő",
    " ê",
    "V2",
    "ļ ",
    "e:",
    "Ő,",
    "ő,",
    "ļl",
    "ė.",
    "īņ",
    " ģ",
    "ïp",
    "YŐ",
    "yő",
    "C:",
    "GÍ",
    "uļ",
    "Ć:",
    "(ģ",
    "Sī",
    "żs",
    "ŻS",
    "Q ",
    "Ł)",
    " ,",
    ":4",
    "żą",
    "?T",
    "*z",
    "T2",
    "îr",
    "ļk",
    "ļķ",
    "SÌ",
    "sì",
    "KŐ",
    "ļb",
    "4f",
    "kő",
    "e;",
    "ļū",
    "A3",
    "*u",
    "SĮ",
    "sį",
    "gļ",
    "s;",
    "ò:",
    "C;",
    "iļ",
    " /",
    "żd",
    ":]",
    "Õ ",
    " ė",
    "õ ",
    " ē",
    "}\\",
    "> ",
    " x",
    "ėv",
    "ĐÁ",
    "đá",
    "ó;",
    "} ",
    "? ",
    "ê ",
    "Ê ",
    "ë:",
    "őf",
    " .",
    "ėž",
    "ŐA",
    "gì",
    "ïn",
    " \\",
    "aï",
    "/ ",
    "+ ",
    "zė",
    " Œ",
    "ŠĮ",
    " >",
    "Ő.",
    "ő.",
    " œ",
    "mî",
    "DŻ",
    "šį",
    "& ",
    " &",
    "ŰJ",
    "űj",
    "Vė",
    " Ź",
    "Ű,",
    "Ży",
    "rđ",
    " ź",
    " }",
    "CÌ",
    "cì",
    ":a",
    "ķī",
    "ŻC",
    "żc",
    "%,",
    "Ź ",
    "ź ",
    " =",
    "āļ",
    "Ø ",
    "ø ",
    "5:",
    " #",
    "4:",
    "nî",
    "= ",
    "%.",
    "uì",
    " ~",
    "łs",
    "ŻÓ",
    " <",
    "ė)",
    "żó",
    "ïs",
    "ÏS",
    " _",
    "Fő",
    "ļr",
    "ļš",
    "ë;",
    "aī",
    "ųs",
    "ĢĪ",
    "ģī",
    "gį",
    "GĮ",
    "< ",
    "[.",
    "CŁ",
    "İŞ",
    " Đ",
    ")\\",
    "Æ ",
    "æ ",
    "ėz",
    "(+",
    "=\\",
    "ŐÁ",
    "(=",
    "nì",
    "Ō ",
    "ō ",
    "żę",
    "ė:",
    "6t",
    "4t",
    "Ő)",
    ":)",
    " )",
    " Ō",
    "ô ",
    "Ô ",
    "uï",
    "LŰ",
    "ŏ ",
    "Ŏ ",
    " ō",
    "× ",
    "( ",
    " Ô",
    " ô",
    "Że",
    "%2",
    "ļņ",
    "SÎ",
    "Ű.",
    "sî",
    "Żo",
    "~ ",
    "Ð ",
    "ð ",
    "AĠ",
    "đm",
    "ő:",
    "Pė",
    "%3",
    "Kė",
    "ş;",
    " ×",
    "íň",
    "æ:",
    "ĕ ",
    "Ĕ ",
    "\\ ",
    "$5",
    "Kő",
    "Ża",
    "E=",
    "mį",
    "Lė",
    " `",
    "MĮ",
    "%9",
    "=f",
    "B:",
    "(~",
    "->",
    "ę:",
    "cė",
    "ě:",
    "(%",
    "e5",
    ":ä",
    "ï ",
    "Ï ",
    "+}",
    "`A",
    "ļs",
    "uī",
    "<õ",
    "õ>",
    "ē:",
    "ūŗ",
    "é:",
    "R=",
    "r=",
    "<-",
    "ĐV",
    "ĐÂ",
    "đâ",
    "š:",
    "ĐJ",
    "Ė-",
    "Tė",
    "uŗ",
    "<T",
    "ŰA",
    "6;",
    "5;",
    "f=",
    "ė;",
    "4;",
    " đ",
    "Ŗ ",
    "Y>",
    "GĪ",
    "šļ",
    ">)",
    "ě;",
    "ű)",
    "ĠV",
    "Rė",
    "(<",
    "Żu",
    "T=",
    "t=",
    "Lő",
    "é;",
    "CÎ",
    "GÌ",
    "v=",
    "E3",
    "ïm",
    "A=",
    "š;",
    "_L",
    "vđ",
    "_n",
    ")?",
    "_N",
    "=5",
    "($",
    "ČĪ",
    "aŗ",
    ">.",
    ">,",
    "2s",
    "čė",
    "%;",
    "fė",
    "t`",
    "#V",
    "#4"
]

en_kern = [it for it in li if it[0].isascii() and it[1].isascii()][0:200]
print(";".join([ "{},{}".format(it[0], it[1]) for it in en_kern]))


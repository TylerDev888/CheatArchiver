/* ============================================================
   CheatCode Archive – CRT effects: matrix column + hex ticker
   ============================================================ */

(function () {
  'use strict';

  /* ── Matrix falling-numbers column ─────────────────────── */
  var col = document.getElementById('matrixCol');
  if (col) {
    var chars = '0123456789ABCDEF';
    var ROW_HEIGHT_PX   = 20;   /* approximate line height of each matrix character */
    var ROW_BUFFER      = 4;    /* extra rows beyond visible height to avoid gaps */
    var ANIM_DUR_MIN    = 1.2;  /* seconds – fastest fall speed */
    var ANIM_DUR_RANGE  = 2.8;  /* seconds – added on top of min for slowest fall */
    var CHAR_CYCLE_MS   = 120;  /* milliseconds between random character swaps */
    var CHAR_CYCLE_PROB = 0.3;  /* probability (0–1) that any given character changes */

    var numRows = Math.floor(window.innerHeight / ROW_HEIGHT_PX) + ROW_BUFFER;
    for (var i = 0; i < numRows; i++) {
      var span = document.createElement('span');
      span.textContent = chars[Math.floor(Math.random() * chars.length)];
      var dur = (ANIM_DUR_MIN + Math.random() * ANIM_DUR_RANGE).toFixed(2) + 's';
      var delay = (Math.random() * -4).toFixed(2) + 's';
      span.style.animationDuration = dur;
      span.style.animationDelay = delay;
      col.appendChild(span);
    }

    /* Cycle characters periodically */
    setInterval(function () {
      var spans = col.querySelectorAll('span');
      spans.forEach(function (s) {
        if (Math.random() < CHAR_CYCLE_PROB) {
          s.textContent = chars[Math.floor(Math.random() * chars.length)];
        }
      });
    }, CHAR_CYCLE_MS);
  }

  /* ── Hex ticker strip ───────────────────────────────────── */
  var ticker = document.getElementById('hexTicker');
  if (ticker) {
    function randHex(len) {
      var out = '';
      for (var i = 0; i < len; i++) {
        out += Math.floor(Math.random() * 16).toString(16).toUpperCase();
      }
      return out;
    }

    function buildTickerText() {
      var parts = [];
      for (var i = 0; i < 40; i++) {
        parts.push(randHex(8) + ' ' + randHex(8));
      }
      return parts.join('  ');
    }

    var inner = document.createElement('span');
    inner.className = 'hex-ticker-inner';
    var text = buildTickerText();
    /* Duplicate so the scroll loops seamlessly */
    inner.textContent = text + '    ' + text;
    ticker.appendChild(inner);
  }

  /* ── A-Z navigation (injected after h1) ────────────────── */
  var content = document.querySelector('.screen-content');
  if (!content) return;

  /* Collect all h2 headings that are single uppercase letters */
  var headings = content.querySelectorAll('h2');
  var letterHeadings = [];
  headings.forEach(function (h) {
    var txt = h.textContent.trim();
    if (/^[A-Z]$/.test(txt)) {
      letterHeadings.push(txt);
      /* Ensure each h2 has an id for anchor linking */
      if (!h.id) {
        h.id = txt;
      }
    }
  });

  if (letterHeadings.length === 0) {
    /* Try h2 headings that start with a letter section (e.g. "Games (A-Z)") */
    /* Still build nav from what anchors exist in the page if any */
  } else {
    /* Build full A-Z nav, greying out absent letters */
    var nav = document.createElement('nav');
    nav.className = 'az-nav';
    nav.setAttribute('aria-label', 'Jump to letter');

    var alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
    alphabet.forEach(function (letter) {
      var a = document.createElement('a');
      a.textContent = letter;
      if (letterHeadings.indexOf(letter) !== -1) {
        a.href = '#' + letter;
        a.addEventListener('click', function () {
          nav.querySelectorAll('a').forEach(function (x) { x.classList.remove('active'); });
          a.classList.add('active');
        });
      } else {
        a.href = '#';
        a.style.opacity = '0.3';
        a.style.pointerEvents = 'none';
      }
      nav.appendChild(a);
    });

    /* Insert after the first h1 (and any immediate sibling p) */
    var h1 = content.querySelector('h1');
    if (h1) {
      var insertAfter = h1;
      /* Skip past any immediately following <p> (subtitle) */
      if (insertAfter.nextElementSibling && insertAfter.nextElementSibling.tagName === 'P') {
        insertAfter = insertAfter.nextElementSibling;
      }
      insertAfter.parentNode.insertBefore(nav, insertAfter.nextSibling);
    } else {
      content.prepend(nav);
    }

    /* Highlight active letter on scroll */
    function onScroll() {
      var scrollTop = content.scrollTop;
      var active = null;
      headings.forEach(function (h) {
        if (/^[A-Z]$/.test(h.textContent.trim())) {
          if (h.offsetTop - content.offsetTop <= scrollTop + 40) {
            active = h.textContent.trim();
          }
        }
      });
      nav.querySelectorAll('a').forEach(function (a) {
        a.classList.toggle('active', a.textContent === active);
      });
    }
    content.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ── Format region tags inside h3 headings ──────────────── */
  var gameHeadings = content.querySelectorAll('h3');
  gameHeadings.forEach(function (h) {
    /* Match patterns like "Armored Core 2 (NTSC-U)" */
    var text = h.innerHTML;
    h.innerHTML = text.replace(/\(([^)]+)\)/g, '<span class="region-tag"> ($1)</span>');
  });

}());

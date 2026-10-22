/* IA342 Week 10: turn Jekyll-rendered Markdown headings into classroom slides. */
(function () {
  "use strict";
  function init() {
    var deck = document.getElementById("ia342-lecture-deck");
    var end = document.getElementById("ia342-slides-end");
    if (!deck || !end || deck.parentNode !== end.parentNode) return;

    var candidateNodes = [];
    var node = deck.nextSibling;
    while (node && node !== end) {
      candidateNodes.push(node);
      node = node.nextSibling;
    }
    if (node !== end) return;
    var headings = candidateNodes.filter(function (item) {
      return item.nodeType === 1 && item.tagName === "H2" && /^Slide\s+\d{1,2}\s+[—-]/.test(item.textContent.trim());
    });
    if (headings.length !== 35 || headings.some(function (item, index) {
      var match = item.textContent.trim().match(/^Slide\s+(\d{1,2})\s+[—-]\s*(.*)$/);
      return !match || Number(match[1]) !== index + 1;
    })) {
      deck.hidden = true;
      return; // Keep the original Markdown readable if the page structure changes.
    }

    var stage = document.getElementById("ia342-slide-stage");
    var slides = [];
    var section = null;
    candidateNodes.forEach(function (item) {
      if (item.nodeType === 8 || (item.nodeType === 3 && !item.textContent.trim())) {
        item.remove();
        return;
      }
      if (item.nodeType === 1 && item.tagName === "HR") {
        item.remove();
        return;
      }
      var match = item.nodeType === 1 && item.tagName === "H2" ? item.textContent.trim().match(/^Slide\s+(\d{1,2})\s+[—-]\s*(.*)$/) : null;
      if (match) {
        section = document.createElement("section");
        section.className = "ia342-slide";
        section.id = "slide-" + Number(match[1]);
        section.setAttribute("role", "group");
        section.setAttribute("aria-label", "Slide " + Number(match[1]) + ": " + match[2]);
        section.hidden = true;
        item.textContent = match[2];
        section.appendChild(item);
        stage.appendChild(section);
        slides.push(section);
      } else if (section && item.nodeType === 1 && item.tagName === "BLOCKQUOTE" && /^Instructor notes:/i.test(item.textContent.trim())) {
        var details = document.createElement("details");
        details.className = "ia342-speaker-notes";
        var summary = document.createElement("summary");
        summary.textContent = "Instructor notes";
        details.appendChild(summary);
        details.appendChild(item);
        section.appendChild(details);
      } else if (section) {
        if (item.nodeType === 1 && item.tagName === "P" && /^Source\s*\/\s*attribution:/i.test(item.textContent.trim())) {
          item.classList.add("ia342-credit");
        }
        section.appendChild(item);
      } else {
        item.remove();
      }
    });

    var numberLabel = document.getElementById("ia342-slide-count");
    var progress = document.getElementById("ia342-progress");
    var previous = document.getElementById("ia342-prev");
    var next = document.getElementById("ia342-next");
    var fullscreenButton = document.getElementById("ia342-fullscreen");
    var footerTopic = document.getElementById("ia342-topic");
    var current = 1;
    var initialHash = window.location.hash.match(/^#slide-(\d{1,2})$/);
    if (initialHash && Number(initialHash[1]) >= 1 && Number(initialHash[1]) <= slides.length) current = Number(initialHash[1]);

    function suspendVideo(slide) {
      if (!slide) return;
      slide.querySelectorAll("iframe[data-src]").forEach(function (frame) {
        if (frame.getAttribute("src") !== "about:blank") frame.setAttribute("src", "about:blank");
      });
    }
    function activateVideo(slide) {
      slide.querySelectorAll("iframe[data-src]").forEach(function (frame) {
        if (frame.getAttribute("src") !== frame.dataset.src) frame.setAttribute("src", frame.dataset.src);
      });
    }
    function render(updateHash) {
      slides.forEach(function (slide, index) {
        var active = index + 1 === current;
        if (!active) suspendVideo(slide);
        slide.hidden = !active;
        slide.setAttribute("aria-hidden", active ? "false" : "true");
      });
      var active = slides[current - 1];
      activateVideo(active);
      active.scrollTop = 0;
      stage.scrollTop = 0;
      numberLabel.textContent = "Slide " + current + " / " + slides.length;
      progress.style.width = (100 * current / slides.length).toFixed(2) + "%";
      previous.disabled = current === 1;
      next.disabled = current === slides.length;
      footerTopic.textContent = active.querySelector("h2").textContent;
      if (updateHash && history.replaceState) {
        history.replaceState(null, "", "#slide-" + current);
      }
    }
    function goTo(index, updateHash) {
      if (index < 1 || index > slides.length || index === current) return;
      current = index;
      render(updateHash !== false);
    }

    previous.addEventListener("click", function () { goTo(current - 1); });
    next.addEventListener("click", function () { goTo(current + 1); });
    fullscreenButton.addEventListener("click", function () {
      if (document.fullscreenElement === deck) {
        if (document.exitFullscreen) document.exitFullscreen();
      } else if (deck.requestFullscreen) {
        deck.requestFullscreen().catch(function () { /* Browser may block fullscreen. */ });
      }
    });
    document.addEventListener("fullscreenchange", function () {
      fullscreenButton.textContent = document.fullscreenElement === deck ? "Exit Fullscreen" : "Fullscreen";
    });
    document.addEventListener("keydown", function (event) {
      if (event.altKey || event.metaKey || event.ctrlKey || event.shiftKey) return;
      var target = event.target;
      if (target && target.closest && target.closest("input, textarea, select, button, summary, [contenteditable='true']")) return;
      var key = event.key;
      if (key === "ArrowRight" || key === "PageDown" || key === " ") {
        if (key === " " && target && target.closest && target.closest("a")) return;
        event.preventDefault();
        goTo(current + 1);
      } else if (key === "ArrowLeft" || key === "PageUp") {
        event.preventDefault();
        goTo(current - 1);
      } else if (key === "Home") {
        event.preventDefault();
        goTo(1);
      } else if (key === "End") {
        event.preventDefault();
        goTo(slides.length);
      }
    });
    window.addEventListener("hashchange", function () {
      var hash = window.location.hash.match(/^#slide-(\d{1,2})$/);
      if (hash) goTo(Number(hash[1]), false);
    });
    render(false);
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
}());

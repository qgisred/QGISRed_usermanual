// The manual's behaviour: mobile menu, search, print button. Plain script,
// no dependencies, no bundler. Trimmed-down v1 scope (no theme toggle, no
// screenshot zoom, no scroll-spy TOC highlight -- decided explicitly, see
// the plan's "Fuera de v1" section).
(function () {
  "use strict";

  var menuButton = document.querySelector("[data-menu-toggle]");
  var nav = document.querySelector(".m-nav");
  if (menuButton && nav) {
    menuButton.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      menuButton.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("click", function (event) {
      if (!nav.classList.contains("is-open")) return;
      if (nav.contains(event.target) || menuButton.contains(event.target)) return;
      nav.classList.remove("is-open");
      menuButton.setAttribute("aria-expanded", "false");
    });
  }

  var printButton = document.querySelector("[data-print]");
  if (printButton) {
    printButton.addEventListener("click", function () {
      window.print();
    });
  }

  var input = document.getElementById("m-search-input");
  var results = document.getElementById("m-search-results");
  if (!input || !results) return;

  // Same "../" prefix the page's own CSS/JS links use (template.ts) -- the
  // manual isn't necessarily deployed at its host's root, so a path that
  // reads from the manual's own root needs this to resolve from here too.
  var base = document.body.getAttribute("data-base") || "";

  var index = null;
  var indexPromise = null;

  function loadIndex() {
    if (!indexPromise) {
      indexPromise = fetch(base + "search-index.json")
        .then(function (response) {
          return response.ok ? response.json() : [];
        })
        .then(function (data) {
          index = data;
          return data;
        })
        .catch(function () {
          index = [];
          return [];
        });
    }
    return indexPromise;
  }

  function render(entries, query) {
    results.innerHTML = "";
    if (entries.length === 0) {
      var empty = document.createElement("li");
      empty.className = "m-result-empty";
      empty.textContent = input.dataset.empty || "";
      results.appendChild(empty);
      results.hidden = false;
      return;
    }
    entries.slice(0, 20).forEach(function (entry) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = base + entry.u;
      var title = document.createElement("strong");
      title.textContent = entry.h ? entry.p + " — " + entry.h : entry.p;
      var path = document.createElement("span");
      path.className = "m-result-path";
      path.textContent = entry.x.length > 120 ? entry.x.slice(0, 120) + "…" : entry.x;
      a.appendChild(title);
      a.appendChild(path);
      li.appendChild(a);
      results.appendChild(li);
    });
    results.hidden = false;
    void query;
  }

  function search(query) {
    var trimmed = query.trim().toLowerCase();
    if (trimmed.length < 2) {
      results.hidden = true;
      results.innerHTML = "";
      return;
    }
    loadIndex().then(function (entries) {
      var matches = entries.filter(function (entry) {
        return (
          entry.p.toLowerCase().indexOf(trimmed) !== -1 ||
          entry.h.toLowerCase().indexOf(trimmed) !== -1 ||
          entry.x.toLowerCase().indexOf(trimmed) !== -1
        );
      });
      render(matches, trimmed);
    });
  }

  input.addEventListener("input", function () {
    search(input.value);
  });
  input.addEventListener("focus", function () {
    if (input.value.trim().length >= 2) search(input.value);
  });
  input.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      results.hidden = true;
      input.blur();
    }
  });
  document.addEventListener("click", function (event) {
    if (results.hidden) return;
    if (results.contains(event.target) || input.contains(event.target)) return;
    results.hidden = true;
  });
})();

(() => {
  const hero = document.querySelector(".hero");
  if (!hero) return;

  const sunEl = hero.querySelector(".hero-sun");
  const moonEl = hero.querySelector(".hero-moon");
  const params = new URLSearchParams(location.search);

  // Deterministic string hash -> [0, 1). No external calls, no storage:
  // the same date string always yields the same value.
  function seededRandom(seedStr) {
    let h = 5381;
    for (let i = 0; i < seedStr.length; i++) {
      h = ((h << 5) + h + seedStr.charCodeAt(i)) >>> 0;
    }
    return (h % 100000) / 100000;
  }

  function localDateStr(d) {
    const y = d.getFullYear();
    const m = String(d.getMonth() + 1).padStart(2, "0");
    const day = String(d.getDate()).padStart(2, "0");
    return `${y}-${m}-${day}`;
  }

  // sunny 60% / rain 15% / fog 15% / windy 10%
  function weatherForDate(d) {
    const r = seededRandom(localDateStr(d) + "-cocoon-weather");
    if (r < 0.6) return "sunny";
    if (r < 0.75) return "rain";
    if (r < 0.9) return "fog";
    return "windy";
  }

  function timePeriod(hour) {
    if (hour >= 5 && hour < 10) return "morning";
    if (hour >= 10 && hour < 16) return "midday";
    if (hour >= 16 && hour < 19) return "evening";
    return "night";
  }

  // Used to position the sun/moon when the period is overridden (test
  // param / heroScene.set) so the arc still matches the chosen period
  // instead of whatever the real clock happens to say.
  function representativeHour(period) {
    switch (period) {
      case "morning": return 7.5;
      case "evening": return 17.5;
      case "night": return 1;
      case "midday":
      default: return 13;
    }
  }

  function clamp(v, min, max) {
    return Math.min(max, Math.max(min, v));
  }

  // One continuous arc across 05:00-19:00 for the sun, and 19:00-05:00
  // (wrapping midnight) for the moon. Stays in the upper "sky" band of
  // the illustration so it never sits behind the centered logo.
  function sunProgress(hour) {
    return clamp((hour - 5) / (19 - 5), 0, 1);
  }
  function moonProgress(hour) {
    const h = hour >= 19 ? hour - 19 : hour + 5; // 19:00 -> 0, 05:00 -> 10
    return clamp(h / 10, 0, 1);
  }

  function positionBody(el, progress, yTop, yDip) {
    if (!el) return;
    const x = 8 + progress * 84; // 8%..92%
    const y = yTop - yDip * Math.sin(progress * Math.PI);
    el.style.setProperty("--cx", x.toFixed(1) + "%");
    el.style.setProperty("--cy", y.toFixed(1) + "%");
  }

  function computeState(overrides) {
    const now = new Date();
    const timeOverride = (overrides && overrides.time) || params.get("heroTime") || null;
    const period = timeOverride || timePeriod(now.getHours());
    const weather = (overrides && overrides.weather) || params.get("heroWeather") || weatherForDate(now);

    let mushroom;
    const mOverride = overrides && overrides.mushroom !== undefined ? overrides.mushroom : params.get("heroMushroom");
    if (mOverride !== null && mOverride !== undefined) {
      mushroom = mOverride === true || mOverride === "1" || mOverride === "true";
    } else {
      const yesterday = new Date(now);
      yesterday.setDate(now.getDate() - 1);
      mushroom = weatherForDate(yesterday) === "rain";
    }

    const hourFloat = timeOverride ? representativeHour(period) : now.getHours() + now.getMinutes() / 60;

    return { period, weather, mushroom, now, hourFloat };
  }

  function apply(state) {
    hero.dataset.time = state.period;
    hero.dataset.weather = state.weather;
    hero.dataset.mushroom = state.mushroom ? "true" : "false";

    positionBody(sunEl, sunProgress(state.hourFloat), 32, 17);
    positionBody(moonEl, moonProgress(state.hourFloat), 22, 12);
  }

  apply(computeState());

  // Manual test hook — no need to wait for real time/weather to change:
  //   window.heroScene.set({ time: "night", weather: "rain", mushroom: true })
  //   window.heroScene.reset()
  // Or via URL: ?heroTime=night&heroWeather=fog&heroMushroom=1
  window.heroScene = {
    set(overrides) {
      apply(computeState(overrides || {}));
    },
    reset() {
      apply(computeState({}));
    },
  };
})();

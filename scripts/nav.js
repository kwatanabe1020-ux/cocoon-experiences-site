document.querySelectorAll(".nav-toggle").forEach((btn) => {
  const nav = btn.closest(".nav");
  const links = nav && nav.querySelector(".nav-links");
  if (!links) return;
  btn.addEventListener("click", () => {
    const open = links.classList.toggle("is-open");
    btn.classList.toggle("is-open", open);
    btn.setAttribute("aria-expanded", String(open));
  });
  links.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      links.classList.remove("is-open");
      btn.classList.remove("is-open");
      btn.setAttribute("aria-expanded", "false");
    })
  );
});

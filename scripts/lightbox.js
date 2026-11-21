// タップで画像を原寸拡大表示するライトボックス。
// .lightbox-trigger(button要素、中に img を1枚持つ)をページ内に置くだけで動く。
// ネイティブの <dialog> を使うため、フォーカス移動・Escキーでの閉じる動作はブラウザ任せにできる。
(function () {
  const triggers = document.querySelectorAll(".lightbox-trigger");
  if (!triggers.length) return;

  const dialog = document.createElement("dialog");
  dialog.className = "lightbox";
  dialog.innerHTML =
    '<button type="button" class="lightbox-close" aria-label="閉じる">&times;</button>' +
    '<img class="lightbox-img" alt="">';
  document.body.appendChild(dialog);

  const img = dialog.querySelector(".lightbox-img");
  const closeBtn = dialog.querySelector(".lightbox-close");

  triggers.forEach((trigger) => {
    trigger.addEventListener("click", () => {
      const source = trigger.querySelector("img");
      if (!source) return;
      img.src = source.currentSrc || source.src;
      img.alt = source.alt;
      dialog.showModal();
    });
  });

  closeBtn.addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (e) => {
    if (e.target === dialog) dialog.close();
  });
})();

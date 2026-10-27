// Компактная реализация: класс folded добавляется родителю поста (.one-post),
// а скрытие элементов выполняется через CSS-стили.
var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var post = e.target.parentElement;
        var folded = post.classList.toggle("folded");
        e.target.innerHTML = folded ? "развернуть" : "свернуть";
    });
}

$(function() {
    $('code').each(function(i, block) {
        hljs.highlightBlock(block);
    });

    var left = $("#left-container");
    var hljsDefault = $(".hljs").html();
    var hljsContents = $(".hljs")
        .contents()
        .filter(function() {
            // var nv = this.nodeValue && this.nodeValue.replace(/\s+/g, "");
            var nv = this.nodeValue && this.nodeValue.trim();
            return this.nodeType === 3 && nv;
        });

    $(".nav li, h2.l, p.l, i.l, .avatar").mouseenter(function() {
        var content = $(this).text().trim();
        hljsContents.each(function(index, elem) {
            if(elem.nodeValue === content) {
                var prevSibling = $(elem.previousSibling);
                var nextSibling = $(elem.nextSibling);
                left.animate({
                    scrollTop: prevSibling.position().top - 100
                }, 300);

                $(elem).wrap("<span class='hovered'>");
            }
        });
    });

    $(".nav li, h2.l, p.l, i.l, .avatar").mouseleave(function() {
        var content = $(this).text().trim();
        hljsContents.each(function(index, elem) {
            if(elem.nodeValue === content) {
                $(elem).unwrap();
            }
        });
    })

    $("article.animated").each(function(index, elem) {
        var seconds = index / 3;
        seconds = seconds + "s";
        $(this).css("animation-delay", seconds);
    });
});

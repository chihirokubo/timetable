// https://gist.github.com/kylebarrow/1042026
// Mobile Safari in standalone mode
if (('standalone' in window.navigator) && window.navigator.standalone) {
    window.addEventListener('load', function() {
        var links = document.links,
            link,
            i;
        for (i = 0; i < links.length; i++) {
            // Don't do this for javascript: links
            if (!~(link = links[i]).href.toLowerCase().indexOf('javascript')) {
                if('href' in link && link.href.indexOf('http') !== -1 && link.href.indexOf(document.location.host) !== -1)
                {
                    link.addEventListener('click', function(event) {
                        event.preventDefault();
                        document.location.href = this.href;
                    }, false);
                }
            }
        }
    }, false);
}


    // localstorageにtokenをsetする
    function set() {

        // Javascriptでランダムな文字列を生成する方法
        // https://qiita.com/ryounagaoka/items/4736c225bdd86a74d59c
        var email = document.form_login.email.value;

        // ローカルストレージにtokenを保存
        localStorage.setItem("email", email);
    }

    // localstorageにtokenをgetして、value欄に表示する
    function get() {
        // ローカルストレージからtokenを取得
        var email = localStorage.getItem("email");

        // token: 欄に取得したtokenを表示
        document.getElementById("token_value").innerText = email;
    }

    // localstorageからtokenを削除する
    function remove() {
        // ローカルストレージからtokenを削除
        localStorage.removeItem("token");

        get();
    }

//    window.onload = function () {
//       get();
//    }


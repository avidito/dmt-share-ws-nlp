function classify_title(title){
    var url = new URL("https://dmt-share.et.r.appspot.com/classify");
    url.searchParams.set("title", "hello");

    var Http = new XMLHttpRequest();
    Http.open("GET", url);
    Http.send();
    Http.onreadystatechange = (e) => {
        // console.log(Http.responseText)
        return Http.responseText
    }
}

const favouriteQuote = document.querySelector(".js-quote-list");

function getStoragedQuotes() {
  const storageKeys = Object.keys(localStorage).filter((key) =>
    key.includes("quote_")
  );

  let storageQuotesObjs;

  if (storageKeys) {
    storageQuotesObjs = storageKeys.map((key) => JSON.parse(localStorage.getItem(key)));
    console.log(storageQuotesObjs)
    favouriteQuote.insertAdjacentHTML("beforeend", favouriteMarkup(storageQuotesObjs))
  }

  
}

getStoragedQuotes();

// <li class="js-li-favourite" data-quote-id="{{ quote.id }}">
//     <a href="{{ quote.get_absolute_url }}">{{ quote.text }}</a>
//     <a href="{% url 'main:author_detail' quote.author.id %}">{{ quote.author }}</a>
//     <div class="js-quote-favourite">&#9734</div>
//     <p>------------------------------------</p>
// </li>

function favouriteMarkup(storagedQuoted) {
  return storagedQuoted
  .map(({ quoteId, hrefQuote, textQuote, hrefAuthor, textAuthor }) => {
    return `<li class="js-li-favourite" data-quote-id="${quoteId}">
<a href="${hrefQuote}">${textQuote}</a>
<a href="${hrefAuthor}">${textAuthor}</a>
<p>------------------------------------</p>
</li>`;
  })
  .join(""); 
}

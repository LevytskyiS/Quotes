// favourite function
const favouriteQuote = document.querySelector(".js-quote-list");

favouriteQuote.addEventListener("click", onClickFavouriteQuote);

// На первый клик делаем звездочку желтой,
// на второй - обратно черной
function onClickFavouriteQuote(evt) {
  if (
    evt.target.style.color === "gold" &&
    evt.target.classList.contains("js-quote-favourite")
  ) {
    evt.target.style = "";
    const quoteId = evt.target.closest("li").dataset.quoteId;
    localStorage.removeItem(`quote_${quoteId}`);
    return;
  }

  if (evt.target.classList.contains("js-quote-favourite")) {
    evt.target.style.color = "gold";
    // Извлекаем всю информацию о цитате
    quoteRetrieved = getQuoteObject(evt);
    localStorage.setItem(
      `quote_${quoteRetrieved.quoteId}`,
      JSON.stringify(quoteRetrieved)
    );
    return;
  }
}

function getQuoteObject(evt) {
  // Извлекаем всю информацию о цитате и возвращаем объект
  // для дальнейшей записи в локальное хранилище
  const closestParent = evt.target.closest("li");
  const aTags = closestParent.querySelectorAll("a");
  const quoteId = closestParent.dataset.quoteId;
  const hrefQuote = aTags[0].href;
  const textQuote = aTags[0].innerText;
  const hrefAuthor = aTags[1].href;
  const textAuthor = aTags[1].innerText;
  return {
    quoteId,
    hrefQuote,
    textQuote,
    hrefAuthor,
    textAuthor,
  };
}

const quotesFavourite = document.querySelectorAll(".js-li-favourite");

function getQuoteId() {
  for (let i = 0; i < quotesFavourite.length; i++) {
    const dataQuoteId = quotesFavourite[i].dataset.quoteId;
    const storageQuoteId = localStorage.getItem(`quote_${dataQuoteId}`);
    if (storageQuoteId) {
      const quoteId = JSON.parse(storageQuoteId).quoteId;
      const goldDiv = quotesFavourite[i].querySelector(".js-quote-favourite");
      goldDiv.style.color = "gold";
    }
  }
}

getQuoteId();

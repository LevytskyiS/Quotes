// favourite function
const favouriteQuote = document.querySelector(".js-quote-list");

favouriteQuote.addEventListener("click", onClickFavouriteQuote);

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
    const quoteId = evt.target.closest("li").dataset.quoteId;
    localStorage.setItem(
      `quote_${quoteId}`,
      JSON.stringify({ quoteId: quoteId })
    );
    return;
  }
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

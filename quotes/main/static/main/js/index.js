const voteBtn = document.querySelector(".js-vote-up");

voteBtn.addEventListener("click", onClickVote);

function onClickVote(evt) {
  const { target } = evt;
  const quoteId = document.querySelector(".js-quote-vote").dataset.quoteId
  console.log(quoteId)
  if (target.value === "submit") {
    const value = 1;
    passData(value, quoteId)
    console.log("Passed a vote")
  }
}

function passData(value, quoteId) {
    let url = "/vote_up/"

    fetch(url, {
        method: "POST",
        headers:{
            "Content-Type":"application/json",
            "X-CSRFToken": csrftoken,
        },
        body:JSON.stringify({"value": value, "quoteId": quoteId})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log("Data: ", data)
        location.reload()
    })
}

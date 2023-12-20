const voteBtn = document.querySelector(".js-vote-up")

voteBtn.addEventListener("click", onClickVote)

function onClickVote(evt) {
    const target = evt.target
    console.log(target)
}
const cards = document.querySelectorAll('.card');
let hasFlipeedCard = false
let fisrtCard,secondCard;
let lockboard = false

function flipCard(){
    if(lockboard) return;
    if(this === fisrtCard) return;

    this.classList.add('flip')
    if(!hasFlipeedCard){
        hasFlipeedCard = true;
        fisrtCard = this;
        return;
    }
    hasFlipeedCard = false;
    secondCard = this;

    checekMatch()
}

function checekMatch(){
    if(fisrtCard.dataset.card === secondCard.dataset.card){
        disableCard()
        return
    }

    unFlipCard()
}
function disableCard(){
    fisrtCard.removeEventListener('click', flipCard)
    secondCard.removeEventListener('click', flipCard)

    resetBoard()
}

function unFlipCard(){
    lockboard = true

    setTimeout( () => {
        secondCard.classList.remove("flip")
        fisrtCard.classList.remove("flip")

        resetBoard()
    },1500)
}

function resetBoard(){
    [hasFlipeedCard,lockboard] = [false,false];
    [fisrtCard,secondCard] = [null,null]
}

(function shuffler(){
    cards.forEach( (card) =>{
        let randomPosition = Math.floor(Math.random() * 12);
        card.style.order = randomPosition;
    })
})();


cards.forEach((card) => {
    card.addEventListener('click', flipCard)
});